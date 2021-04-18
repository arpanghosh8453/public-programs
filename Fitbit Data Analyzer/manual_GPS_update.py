import requests, sys, os, pytz, time
from datetime import datetime, date, timedelta
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
import pandas as pd
import datetime as DT
import xmltodict

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

#after_date = input("Enter after date (yyyy-mm-dd format ) : ")
after_date = input("Enter last(after) date (yyyy-mm-dd format ) : ")

print("\n=====================Starting Update====================\n")

def get_gps(tcx_url,activity_name,logid):
    
    header = {'Authorization': 'Bearer {}'.format(FITBIT_ACCESS_TOKEN)}
    response = requests.get(tcx_url, headers=header)
    data_dict = xmltodict.parse(response.content)
    track_list = []
    if 'Lap' in data_dict['TrainingCenterDatabase']['Activities']['Activity']:
        if type(data_dict['TrainingCenterDatabase']['Activities']['Activity']['Lap']) is list:
            for lap_entry in data_dict['TrainingCenterDatabase']['Activities']['Activity']['Lap']:
                for entry in lap_entry['Track']['Trackpoint']:
                    utc_time = LOCAL_TIMEZONE.localize(datetime.fromisoformat(entry['Time'][0:23])).astimezone(pytz.utc).isoformat()
                    track_list.append({
                                    "measurement": "GPS_track",
                                    "time": utc_time,
                                    "fields": {
                                        "lat": float(entry['Position']['LatitudeDegrees']),
                                        "long": float(entry['Position']['LongitudeDegrees']),
                                        "alt": float(entry['AltitudeMeters']),
                                        "activity_name": activity_name,
                                        "id": logid

                                    }
                                })
        else:    
            for entry in data_dict['TrainingCenterDatabase']['Activities']['Activity']['Lap']['Track']['Trackpoint']:
                utc_time = LOCAL_TIMEZONE.localize(datetime.fromisoformat(entry['Time'][0:23])).astimezone(pytz.utc).isoformat()
                track_list.append({
                                "measurement": "GPS_track",
                                "time": utc_time,
                                "fields": {
                                    "lat": float(entry['Position']['LatitudeDegrees']),
                                    "long": float(entry['Position']['LongitudeDegrees']),
                                    "alt": float(entry['AltitudeMeters']),
                                    "activity_name": activity_name,
                                    "id": logid

                                }
                            })
    return track_list

def fetch_activities(date):
    global points
    try:
        response = requests.get('https://api.fitbit.com/1/user/-/activities/list.json',
            headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE},
            params={'beforeDate': date, 'sort':'desc', 'limit':50, 'offset':0})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("HTTP request failed: %s" % (err))
        sys.exit()

    data = response.json()
    print("Got activities from Fitbit for before_date: "+date)

    for activity in data['activities']:

        if 'tcxLink' in activity:
            gps_track_list = get_gps(activity['tcxLink'], activity['activityName'], activity['logId'])
            if len(gps_track_list) != 0:
                print("Got GPS from Fitbit for log id: "+str(activity['logId']))
                points += gps_track_list

try:
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    #Requires admin user privilage
    #client.create_database(INFLUXDB_DATABASE)
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
    f = open('C:/Users/Arpan Ghosh/.fitbit-refreshtoken', "r+")
    f.write(refresh_token)
    f.close()

fetch_activities(after_date)

try:
    client.write_points(points)
    #print(points)

except InfluxDBClientError as err:
    print("Unable to write points to InfluxDB: %s" % (err))
    sys.exit()

print("Successfully wrote %s data points to InfluxDB" % (len(points)))
points = []
print("\n=============================== O ===============================\n")
