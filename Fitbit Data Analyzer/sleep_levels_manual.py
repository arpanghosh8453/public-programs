import requests, sys, os, pytz
from datetime import datetime, date, timedelta
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError

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

#start_date = '2021-04-01'
#end_date = '2021-04-05'

print("\n=====================Manual influxdb update====================\n")

start_date = input("Enter start date (yyyy-mm-dd format ) : ")
end_date = input("Enter end date + 1 (yyyy-mm-dd format ) : ")

print("\n=====================Starting Update====================\n")

def process_levels(levels):
    if not levels:
        return
    unsorted_list = levels
    sorted_list = sorted(unsorted_list, key=lambda k: k['dateTime_obj']) 
    data_added_list = []
    for item in sorted_list:
        data_added_list.append(item)
        if item["short"]:
            insert_item = {}
            prev_item = data_added_list[-2]
            insert_item["level"] = prev_item["level"]
            newtime = item["dateTime_obj"] + timedelta(0,item["seconds"])
            insert_item["dateTime"] = newtime.strftime("%Y-%m-%dT%H:%M:%S.%f")
            insert_item["seconds"] = item["seconds"]
            insert_item["short"] = True
            data_added_list.append(insert_item)

    for level in data_added_list:
        sleep_type = level['level']
        if sleep_type == "asleep":
            sleep_type = "light"
        if sleep_type == "restless":
            sleep_type = "rem"
        if sleep_type == "awake":
            sleep_type = "wake"

        time = datetime.fromisoformat(level['dateTime'])
        utc_time = LOCAL_TIMEZONE.localize(time).astimezone(pytz.utc).isoformat()
        if 'short' in level:
            flag = level['short']
        else:
            flag = True
        points.append({
                "measurement": "sleep_levels",
                "time": utc_time,
                "fields": {
                    "seconds": int(level['seconds']),
                    "sleep_type": sleep_type,
                    "short" : flag
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
    if os.path.isfile('.fitbit-refreshtoken'):
        f = open(".fitbit-refreshtoken", "r")
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
    f = open(".fitbit-refreshtoken", "w+")
    f.write(refresh_token)
    f.close()

    
#Sleep logs

print("\n=====================Updating sleep log database====================\n")

try:
    response = requests.get('https://api.fitbit.com/1.2/user/-/sleep/date/' + start_date + '/' + end_date + '.json',
        headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print("HTTP request failed: %s" % (err))
    sys.exit()

data = response.json()
print("Got sleep sessions from Fitbit")

for day in data['sleep']:
    time = datetime.fromisoformat(day['startTime'])
    utc_time = LOCAL_TIMEZONE.localize(time).astimezone(pytz.utc).isoformat()
    
    longdata = []
    shortdata = []
    if 'data' in day['levels']:
        longdata = day['levels']['data']
        for entry in longdata:
            dtobj = datetime.strptime(entry["dateTime"], "%Y-%m-%dT%H:%M:%S.%f")
            entry["dateTime_obj"] = dtobj
            entry["short"] = False
    
    if 'shortData' in day['levels']:
        shortdata = day['levels']['shortData']
        for entry in shortdata:
            dtobj = datetime.strptime(entry["dateTime"], "%Y-%m-%dT%H:%M:%S.%f")
            entry["dateTime_obj"] = dtobj
            entry["short"] = True
    
    process_levels(longdata + shortdata)

    sleep_end_time = LOCAL_TIMEZONE.localize(datetime.fromisoformat(day['endTime'])).astimezone(pytz.utc).isoformat()

    points.append({
            "measurement": "sleep_levels",
            "time": sleep_end_time,
            "fields": {
                "seconds": 1800,
                "sleep_type": "wake",
                "short" : False
            }
        })

print("\n=====================Sleep logs updated====================\n")

try:
    client.write_points(points)
except InfluxDBClientError as err:
    print("Unable to write points to InfluxDB: %s" % (err))
    sys.exit()

print("Successfully wrote %s data points to InfluxDB" % (len(points)))

print("\n=============================== O ===============================\n")
