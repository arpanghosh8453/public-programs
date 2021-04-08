import requests, sys, os, pytz, time
from datetime import datetime, date, timedelta
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
import psutil

INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = 'arpan'
INFLUXDB_PASSWORD = '#Password#1'
INFLUXDB_DATABASE = 'laptop'
LOCAL_TIMEZONE = pytz.timezone('Asia/Calcutta')

filehandle = open("D:/docker_volumes/database_update_log.txt", "a")
filehandle.write("\n########################  CPU Logging started : " + str(datetime.now()) + "  ############################\n")

try:
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    client.create_database(INFLUXDB_DATABASE)
    client.switch_database(INFLUXDB_DATABASE)
except InfluxDBClientError as err:
    filehandle.write("\nInfluxDB connection failed for CPU logging: %s \n" % (err))
    sys.exit()

while True:
    try:
        client.write_points([{"measurement": "CPU_usage", "time": LOCAL_TIMEZONE.localize(datetime.now()).astimezone(pytz.utc).isoformat(), "fields": {"value": psutil.cpu_percent()}}])
        print('The CPU usage is: ', psutil.cpu_percent())
    except InfluxDBClientError as err:
        filehandle.write("\nUnable to write points to InfluxDB: %s \n" % (err))
        sys.exit()
    time.sleep(1)