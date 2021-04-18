import requests, sys, os, pytz, time
from datetime import datetime, date, timedelta
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
import pandas as pd
import datetime as DT
import xmltodict # for GPS xml analysis

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

filehandle = open("D:/docker_volumes/database_update_log.txt", "a")

filehandle.write("\n\n########################  Script start time : " + str(datetime.now()) + "  ############################\n\n")
print("\n\n########################  Script start time : " + str(datetime.now()) + "  ############################\n\n")

print("\nWorking : Writting log to D:/docker_volumes/database_update_log.txt\n")

def fetch_data(category, type, date_var):
    try:
        response = requests.get('https://api.fitbit.com/1/user/-/' + category + '/' + type + '/date/'+date_var+'/1d.json', 
            headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        filehandle.write("\nHTTP request failed: %s \n" % (err))
        print("\nHTTP request failed: %s \n" % (err))
        sys.exit()

    data = response.json()
    filehandle.write("\nGot " + type + " for "+ date_var +" from Fitbit\n")
    print("\nGot " + type + " for "+ date_var +" from Fitbit\n")

    for day in data[category.replace('/', '-') + '-' + type]:
        points.append({
                "measurement": type,
                "time": LOCAL_TIMEZONE.localize(datetime.fromisoformat(day['dateTime'])).astimezone(pytz.utc).isoformat(),
                "fields": {
                    "value": float(day['value'])
                }
            })

def fetch_hourly_steps(date):
    try:
        response = requests.get('https://api.fitbit.com/1/user/-/activities/steps/date/' + date + '/1d/1min.json', 
            headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        filehandle.write("\nHTTP request failed: %s \n" % (err))
        print("\nHTTP request failed: %s \n" % (err))
        sys.exit()

    data = response.json()
    filehandle.write("\n Got daily hourly steps for "+date+" from Fitbit \n")
    print("\n Got daily hourly steps for "+date+" from Fitbit \n")

    if 'activities-steps-intraday' in data:
        for value in data['activities-steps-intraday']['dataset']:
            time = datetime.fromisoformat(date + "T" + value['time'])
            utc_time = LOCAL_TIMEZONE.localize(time).astimezone(pytz.utc).isoformat()
            points.append({
                    "measurement": "hourly_steps",
                    "time": utc_time,
                    "fields": {
                        "value": float(value['value'])
                    }
                })
                
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


def fetch_heartrate(date):
    try:
        response = requests.get('https://api.fitbit.com/1/user/-/activities/heart/date/' + date + '/1d/1sec.json', 
            headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        filehandle.write("\nHTTP request failed: %s \n" % (err))
        print("\nHTTP request failed: %s \n" % (err))
        sys.exit()

    data = response.json()
    filehandle.write("\nGot heartrates for "+date+" from Fitbit\n")
    print("\nGot heartrates for "+date+" from Fitbit\n")

    for day in data['activities-heart']:
        if 'restingHeartRate' in day['value']:
            points.append({
                    "measurement": "restingHeartRate",
                    "time": datetime.fromisoformat(day['dateTime']),
                    "fields": {
                        "value": float(day['value']['restingHeartRate'])
                    }
                })

        if 'heartRateZones' in day['value']:
            for zone in day['value']['heartRateZones']:
                if 'caloriesOut' in zone and 'min' in zone and 'max' in zone and 'minutes' in zone:
                    points.append({
                            "measurement": "heartRateZones",
                            "time": datetime.fromisoformat(day['dateTime']),
                            "tags": {
                                "zone": zone['name']
                            },
                            "fields": {
                                "caloriesOut": float(zone['caloriesOut']),
                                "min": float(zone['min']),
                                "max": float(zone['max']),
                                "minutes": float(zone['minutes'])
                            }
                        })
                elif 'min' in zone and 'max' in zone and 'minutes' in zone:
                    points.append({
                            "measurement": "heartRateZones",
                            "time": datetime.fromisoformat(day['dateTime']),
                            "tags": {
                                "zone": zone['name']
                            },
                            "fields": {
                                "min": float(zone['min']),
                                "max": float(zone['max']),
                                "minutes": float(zone['minutes'])
                            }
                        })

    if 'activities-heart-intraday' in data:
        for value in data['activities-heart-intraday']['dataset']:
            time = datetime.fromisoformat(date + "T" + value['time'])
            utc_time = LOCAL_TIMEZONE.localize(time).astimezone(pytz.utc).isoformat()
            points.append({
                    "measurement": "heartrate",
                    "time": utc_time,
                    "fields": {
                        "value": float(value['value'])
                    }
                })

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
            params={'beforeDate': date, 'sort':'desc', 'limit':6, 'offset':0})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        filehandle.write("\nHTTP request failed: %s \n" % (err))
        print("\nHTTP request failed: %s \n" % (err))
        sys.exit()

    data = response.json()
    filehandle.write("\nGot activities from Fitbit for before_date: "+date+"\n")
    print("\nGot activities from Fitbit for before_date: "+date+"\n")

    for activity in data['activities']:
        fields = {}

        if 'activeDuration' in activity:
            fields['activeDuration'] = int(activity['activeDuration'])
        if 'averageHeartRate' in activity:
            fields['averageHeartRate'] = int(activity['averageHeartRate'])
        if 'calories' in activity:
            fields['calories'] = int(activity['calories'])
        if 'duration' in activity:
            fields['duration'] = int(activity['duration'])
        if 'distance' in activity:
            fields['distance'] = float(activity['distance'])
            fields['distanceUnit'] = activity['distanceUnit']
        if 'pace' in activity:
            fields['pace'] = float(activity['pace'])
        if 'speed' in activity:
            fields['speed'] = float(activity['speed'])
        if 'elevationGain' in activity:
            fields['elevationGain'] = int(activity['elevationGain'])
        if 'steps' in activity:
            fields['steps'] = int(activity['steps'])
        if 'tcxLink' in activity:
            gps_track_list = get_gps(activity['tcxLink'], activity['activityName'], activity['logId'])
            if len(gps_track_list) != 0:
                filehandle.write("\nGot GPS from Fitbit for log id: "+str(activity['logId'])+"\n")
                print("\nGot GPS from Fitbit for log id: "+str(activity['logId'])+"\n")
                points += gps_track_list

        for level in activity['activityLevel']:
            if level['name'] == 'sedentary':
                fields[level['name'] + "Minutes"] = int(level['minutes'])
            else:
                fields[level['name'] + "ActiveMinutes"] = int(level['minutes'])


        time = datetime.fromisoformat(activity['startTime'].strip("Z"))
        utc_time = time.astimezone(pytz.utc).isoformat()
        points.append({
            "measurement": "activity",
            "time": utc_time,
            "tags": {
                "activityName": activity['activityName']
            },
            "fields": fields
        })

try:
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    #Requires admin user privilage
    #client.create_database(INFLUXDB_DATABASE)
    client.switch_database(INFLUXDB_DATABASE)
except InfluxDBClientError as err:
    filehandle.write("\nInfluxDB connection failed: %s \n" % (err))
    print("\nInfluxDB connection failed: %s \n" % (err))
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

try:
    response = requests.get('https://api.fitbit.com/1/user/-/devices.json', 
        headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    filehandle.write("\nHTTP request failed: %s \n" % (err))
    print("\nHTTP request failed: %s \n" % (err))
    sys.exit()

data = response.json()

filehandle.write("\nGot devices from Fitbit for current datetime "+str(datetime.today())+"\n")
print("\nGot devices from Fitbit for current datetime "+str(datetime.today())+"\n")

for device in data:
    points.append({
        "measurement": "deviceBatteryLevel",
        "time": LOCAL_TIMEZONE.localize(datetime.fromisoformat(device['lastSyncTime'])).astimezone(pytz.utc).isoformat(),
        "tags": {
            "id": device['id'],
            "deviceVersion": device['deviceVersion'],
            "type": device['type'],
            "mac": device['mac'],
        },
        "fields": {
            "value": float(device['batteryLevel'])
        }
    })

end = date.today()
start = end - timedelta(days=1)

try:
    response = requests.get('https://api.fitbit.com/1.2/user/-/sleep/date/' + start.isoformat() + '/' + end.isoformat() + '.json',
        headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    filehandle.write("\nHTTP request failed: %s \n" % (err))
    print("\nHTTP request failed: %s \n" % (err))
    sys.exit()

data = response.json()
filehandle.write("\nGot sleep sessions from Fitbit\n")
print("\nGot sleep sessions from Fitbit\n")

for day in data['sleep']:
    time = datetime.fromisoformat(day['startTime'])
    utc_time = LOCAL_TIMEZONE.localize(time).astimezone(pytz.utc).isoformat()
    if day['type'] == 'stages':
        points.append({
            "measurement": "sleep",
            "time": utc_time,
            "fields": {
                "duration": int(day['duration']),
                "efficiency": int(day['efficiency']),
                "is_main_sleep": bool(day['isMainSleep']),
                "minutes_asleep": int(day['minutesAsleep']),
                "minutes_awake": int(day['minutesAwake']),
                "time_in_bed": int(day['timeInBed']),
                "minutes_deep": int(day['levels']['summary']['deep']['minutes']),
                "minutes_light": int(day['levels']['summary']['light']['minutes']),
                "minutes_rem": int(day['levels']['summary']['rem']['minutes']),
                "minutes_wake": int(day['levels']['summary']['wake']['minutes']),
            }
        })
    else:
        points.append({
            "measurement": "sleep",
            "time": utc_time,
            "fields": {
                "duration": int(day['duration']),
                "efficiency": int(day['efficiency']),
                "is_main_sleep": bool(day['isMainSleep']),
                "minutes_asleep": int(day['minutesAsleep']),
                "minutes_awake": int(day['minutesAwake']),
                "time_in_bed": int(day['timeInBed']),
                "minutes_deep": 0,
                "minutes_light": int(day['levels']['summary']['asleep']['minutes']),
                "minutes_rem": int(day['levels']['summary']['restless']['minutes']),
                "minutes_wake": int(day['levels']['summary']['awake']['minutes']),
            }
        })
    
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


same_date = (date.today()).isoformat()
previous_date = (date.today() - timedelta(days=1)).isoformat()
next_date = (date.today() + timedelta(days=1)).isoformat()

#Previous day logging
fetch_data('activities', 'steps', previous_date )
fetch_data('activities', 'distance', previous_date)
fetch_data('activities', 'floors', previous_date)
fetch_data('activities', 'elevation', previous_date)
fetch_data('activities', 'distance', previous_date)
fetch_data('activities', 'minutesSedentary', previous_date)
fetch_data('activities', 'minutesLightlyActive', previous_date)
fetch_data('activities', 'minutesFairlyActive', previous_date)
fetch_data('activities', 'minutesVeryActive', previous_date)
fetch_data('activities', 'calories', previous_date)
fetch_data('activities', 'activityCalories', previous_date)
fetch_data('body', 'weight', previous_date)
fetch_data('body', 'fat', previous_date)
fetch_data('body', 'bmi', previous_date)
fetch_data('foods/log', 'water', previous_date)
fetch_data('foods/log', 'caloriesIn', previous_date)
fetch_heartrate(previous_date)
fetch_hourly_steps(previous_date)
fetch_activities(same_date) #Special one requires same date for previous day one as the argument is afterdate

print("\n----------------------------Previous day logging done-------------------------------\n")

#Same day logging
fetch_data('activities', 'steps', same_date )
fetch_data('activities', 'distance', same_date)
fetch_data('activities', 'floors', same_date)
fetch_data('activities', 'elevation', same_date)
fetch_data('activities', 'distance', same_date)
fetch_data('activities', 'minutesSedentary', same_date)
fetch_data('activities', 'minutesLightlyActive', same_date)
fetch_data('activities', 'minutesFairlyActive', same_date)
fetch_data('activities', 'minutesVeryActive', same_date)
fetch_data('activities', 'calories', same_date)
fetch_data('activities', 'activityCalories', same_date)
fetch_data('body', 'weight', same_date)
fetch_data('body', 'fat', same_date)
fetch_data('body', 'bmi', same_date)
fetch_data('foods/log', 'water', same_date)
fetch_data('foods/log', 'caloriesIn', same_date)
fetch_heartrate(same_date)
fetch_hourly_steps(same_date)
fetch_activities(next_date) #Special one requires next date for same day one as the argument is afterdate

points.append({"measurement": "last_database_update", "time": LOCAL_TIMEZONE.localize(datetime.now()).astimezone(pytz.utc).isoformat(), "fields": {"value": 1}})

try:
    client.write_points(points)
except InfluxDBClientError as err:
    filehandle.write("\nUnable to write points to InfluxDB: %s \n" % (err))
    print("\nUnable to write points to InfluxDB: %s \n" % (err))
    sys.exit()

filehandle.write("\nSuccessfully wrote %s data points to InfluxDB\n" % (len(points)))
print("Successfully wrote %s data points to InfluxDB" % (len(points)))
filehandle.close()
