import requests, sys, os, pytz, time, json
from datetime import datetime, date, timedelta
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError

INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = 'db_username'
INFLUXDB_PASSWORD = 'db_password'
INFLUXDB_DATABASE = 'db_name'
LOCAL_TIMEZONE = pytz.timezone('Asia/Calcutta')
api_key = "API key"
city_name = "City"


filehandle = open("D:/docker_volumes/database_update_log.txt", "a")
filehandle.write("\n########################  Weather Logging started : " + str(datetime.now()) + "  ############################\n")


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
    if x["cod"] == 200:

        y = x["main"]

        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        current_visibility = x["visibility"]
        current_wind = x["wind"]
    
        try:
            client.write_points([
                {"measurement": "temperature", "time": LOCAL_TIMEZONE.localize(current_datetime).astimezone(pytz.utc).isoformat(), "fields": {"value": current_temperature - 273.15}},
                {"measurement": "pressure", "time": LOCAL_TIMEZONE.localize(current_datetime).astimezone(pytz.utc).isoformat(), "fields": {"value": current_pressure}},
                {"measurement": "humidity", "time": LOCAL_TIMEZONE.localize(current_datetime).astimezone(pytz.utc).isoformat(), "fields": {"value": current_humidiy}},
                {"measurement": "visibility", "time": LOCAL_TIMEZONE.localize(current_datetime).astimezone(pytz.utc).isoformat(), "fields": {"value": current_visibility}},
                {"measurement": "wind", "time": LOCAL_TIMEZONE.localize(current_datetime).astimezone(pytz.utc).isoformat(), "fields": {"speed": current_wind["speed"], "deg": current_wind["deg"]}}
            ])
            print('temperature, pressure, humidity: ', current_temperature - 273.15, current_pressure, current_humidiy)
        except InfluxDBClientError as err:
            filehandle.write("\nUnable to write points to InfluxDB: %s \n" % (err))
            sys.exit()
    else:
        print(" Error : "+ str(x["cod"]) + " : " + str(x["message"]))
        filehandle.write(" Error : "+ str(x["cod"]) + " : " + str(x["message"]))


    time.sleep(900)

filehandle.close()