import requests, sys, os, pytz, time, json
from datetime import datetime, date, timedelta
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError

INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = 'db_username'
INFLUXDB_PASSWORD = 'db_password'
INFLUXDB_DATABASE = 'weather'
LOCAL_TIMEZONE = pytz.timezone('Asia/Calcutta')
api_key = "API key"
city_name = "city location"


filehandle = open("D:/docker_volumes/database_update_log.txt", "a")
filehandle.write("\n########################  Weather Logging started : " + str(datetime.now()) + "  ############################\n")
filehandle.close()

try:
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    #Requires admin user privilage
    #client.create_database(INFLUXDB_DATABASE)
    client.switch_database(INFLUXDB_DATABASE)
except InfluxDBClientError as err:
    filehandle.write("\nInfluxDB connection failed for humidity logging: %s \n" % (err))
    sys.exit()

while True:
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    
    # json method of response object 
    # convert json format data into
    # python format data
    x = response.json()
    current_datetime = datetime.now()
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]
    
        try:
            client.write_points([
                {"measurement": "temperature", "time": LOCAL_TIMEZONE.localize(current_datetime).astimezone(pytz.utc).isoformat(), "fields": {"value": current_temperature - 273.15}},
                {"measurement": "pressure", "time": LOCAL_TIMEZONE.localize(current_datetime).astimezone(pytz.utc).isoformat(), "fields": {"value": current_pressure}},
                {"measurement": "humidity", "time": LOCAL_TIMEZONE.localize(current_datetime).astimezone(pytz.utc).isoformat(), "fields": {"value": current_humidiy}}
            ])
            print('temperature, pressure, humidity: ', current_temperature - 273.15, current_pressure, current_humidiy)
        except InfluxDBClientError as err:
            filehandle.write("\nUnable to write points to InfluxDB: %s \n" % (err))
            sys.exit()
        else:
            print(" City Not Found ")

    time.sleep(900)