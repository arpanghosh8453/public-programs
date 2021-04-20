import requests, sys, os, pytz, time
from datetime import datetime, date, timedelta
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
import psutil
import subprocess
from win32api import GetLastInputInfo

INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = 'influxdb_username'
INFLUXDB_PASSWORD = 'influxdb_password'
INFLUXDB_DATABASE = 'laptop'
LOCAL_TIMEZONE = pytz.timezone('Asia/Calcutta')

filehandle = open("D:/docker_volumes/database_update_log.txt", "a")
filehandle.write("\n########################  CPU Logging started : " + str(datetime.now()) + "  ############################\n")

try:
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    #Requires admin user privilage
    #client.create_database(INFLUXDB_DATABASE)
    client.switch_database(INFLUXDB_DATABASE)
except InfluxDBClientError as err:
    filehandle.write("\nInfluxDB connection failed for CPU logging: %s \n" % (err))
    sys.exit()

last_input = GetLastInputInfo()

update_count = 0

process=subprocess.Popen(["powershell","Get-WinEvent -FilterHashtable @{Logname='System';ID=6006} | Select-Object TimeCreated | Sort-Object -Property TimeCreated | foreach {($_.TimeCreated.ToString('s'))}"],stdout=subprocess.PIPE)
result=process.communicate()[0].decode('utf-8').replace('\r','').split('\n')[-2]
shutdown_datetime = datetime.fromisoformat(result)

try:
    client.write_points([{"measurement": "user_activity", "time": LOCAL_TIMEZONE.localize(shutdown_datetime).astimezone(pytz.utc).isoformat(), "fields": {"value": 'off'}}])
    print("shotdown logged at : ",shutdown_datetime)
except InfluxDBClientError as err:
    filehandle.write("\nUnable to write shutdown points to InfluxDB: %s \n" % (err))


while True:
    try:
        client.write_points([{"measurement": "CPU_usage", "time": LOCAL_TIMEZONE.localize(datetime.now()).astimezone(pytz.utc).isoformat(), "fields": {"value": psutil.cpu_percent()}}])
        print('The CPU usage is: ', psutil.cpu_percent())
    except InfluxDBClientError as err:
        filehandle.write("\nUnable to write CPU points to InfluxDB: %s \n" % (err))

    if update_count % 5 == 0:
        if GetLastInputInfo() == last_input:
            print('CurrentState = idle')
            current_state = 'idle'
        else:
            last_input = GetLastInputInfo()
            print('CurrentState = active')
            current_state = 'active'
        try:
            client.write_points([{"measurement": "user_activity", "time": LOCAL_TIMEZONE.localize(datetime.now()).astimezone(pytz.utc).isoformat(), "fields": {"value": current_state}}])
        except InfluxDBClientError as err:
            filehandle.write("\nUnable to write user activity points to InfluxDB: %s \n" % (err))

    time.sleep(1)

    update_count += 1
