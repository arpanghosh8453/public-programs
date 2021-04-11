import requests, sys, os, pytz, time
from datetime import datetime, date, timedelta
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
import pandas as pd
import datetime as DT

LOCAL_TIMEZONE = pytz.timezone('Asia/Calcutta')
FITBIT_LANGUAGE = 'en_US'
FITBIT_CLIENT_ID = ''
FITBIT_CLIENT_SECRET = ''
FITBIT_ACCESS_TOKEN = ''
FITBIT_INITIAL_CODE = ''
REDIRECT_URI = 'http://localhost/8080'
INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = 'database_username'
INFLUXDB_PASSWORD = 'database_password'
INFLUXDB_DATABASE = 'fitbit'
points = []


#dates variable assignment

#start_date = '2021-04-11'
#end_date = '2021-04-12'

print("\n=====================Manual influxdb update====================\n")

start_date = input("Enter start date (yyyy-mm-dd format ) : ")
end_date = input("Enter end date + 1 (yyyy-mm-dd format ) : ")

print("\n=====================Starting Update====================\n")




def fetch_hourly_steps(date):
    try:
        response = requests.get('https://api.fitbit.com/1/user/-/activities/steps/date/' + date + '/1d/1min.json', 
            headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("HTTP request failed: %s" % (err))
        sys.exit()

    data = response.json()
    print("\n\nGot daily steps for "+date+" from Fitbit\n\n")

    if 'activities-steps-intraday' in data:
        df = pd.DataFrame(data['activities-steps-intraday']['dataset'])
        df['datetime'] = pd.to_datetime(data['activities-steps'][0]['dateTime'] + ' ' + df['time'].astype(str))
        hourly_dict = eval(df.groupby(pd.to_datetime(df.datetime.dt.strftime('%Y-%m-%d %H'))).agg({'value':'sum'}).to_json())["value"]
        #print(hourly_dict)
        for key in hourly_dict.keys():
            time = DT.datetime.utcfromtimestamp(int(key)/1000)
            utc_time = LOCAL_TIMEZONE.localize(time).astimezone(pytz.utc).isoformat()
            points.append({
                    "measurement": "hourly_steps_sum",
                    "time": utc_time,
                    "fields": {
                        "value": hourly_dict[key],
                        "greater than 250" : hourly_dict[key] > 250
                    }
                })

try:
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    client.create_database(INFLUXDB_DATABASE)
    client.switch_database(INFLUXDB_DATABASE)
except InfluxDBClientError as err:
    print("InfluxDB connection failed: %s" % (err))
    sys.exit()

if not FITBIT_ACCESS_TOKEN:
    if os.path.isfile('C:/Users/Arpan Ghosh/.fitbit-refreshtoken'):
        f = open('C:/Users/Arpan Ghosh/.fitbit-refreshtoken', "r")
        token = f.read()
        f.close()
        response = requests.post('https://api.fitbit.com/oauth2/token',
            data={
                "client_id": FITBIT_CLIENT_ID,
                "grant_type": "refresh_token",
                "redirect_uri": REDIRECT_URI,
                "refresh_token": token
            }, auth=(FITBIT_CLIENT_ID, FITBIT_CLIENT_SECRET))
    else:
        response = requests.post('https://api.fitbit.com/oauth2/token',
            data={
                "client_id": FITBIT_CLIENT_ID,
                "grant_type": "authorization_code",
                "redirect_uri": REDIRECT_URI,
                "code": FITBIT_INITIAL_CODE
            }, auth=(FITBIT_CLIENT_ID, FITBIT_CLIENT_SECRET))

    response.raise_for_status()

    json = response.json()
    FITBIT_ACCESS_TOKEN = json['access_token']
    refresh_token = json['refresh_token']
    f = open('C:/Users/Arpan Ghosh/.fitbit-refreshtoken', "w+")
    f.write(refresh_token)
    f.close()


start = datetime.strptime(start_date, "%Y-%m-%d")
end = datetime.strptime(end_date, "%Y-%m-%d")

date_array = (start + timedelta(days=x) for x in range(0, (end-start).days))

day_list = []
for date_object in date_array:
    day_list.append(date_object.strftime("%Y-%m-%d"))

iteration_count = 0

for day_date in day_list:

    fetch_hourly_steps(day_date)

    try:
        client.write_points(points)
        #print(points)
    except InfluxDBClientError as err:
        print("Unable to write points to InfluxDB: %s" % (err))
        sys.exit()

    print("Successfully wrote %s data points to InfluxDB" % (len(points)))

    points = []

    print("\n=============================== O ===============================\n")

    iteration_count += 1
    if iteration_count % 100 == 0:
        print("\n--------------Assuming API limit reached : Pausing script for an hour-----------------\n")
        time.sleep(3660)
