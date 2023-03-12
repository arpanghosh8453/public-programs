# %%
import pandas as pd
from datetime import datetime
import pytz, os, glob
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
from dotenv import dotenv_values

REDIRECT_URI = 'http://localhost/8080'
INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = dotenv_values('C:/Users/thisi/OneDrive/Desktop/Python codes/.env')['INFLUX_USERNAME']
INFLUXDB_PASSWORD = dotenv_values('C:/Users/thisi/OneDrive/Desktop/Python codes/.env')['INFLUX_USER_PASSWORD']
INFLUXDB_DATABASE = 'amazfit'

try:
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    client.switch_database(INFLUXDB_DATABASE)
except InfluxDBClientError as err:
    print("\nInfluxDB connection failed: %s \n" % (err))

# %% [markdown]
# ## Folder Set

# %%
master_folder = "C:/Users/thisi/Downloads/6018253702_1678609836608" # Change this folder path to your unzipped master folder

default_paths = {'hr_path': glob.glob(f"{master_folder}/HEARTRATE_AUTO/*")[0], 
                 'steps_path': glob.glob(f"{master_folder}/ACTIVITY_MINUTE/*")[0], 
                 'sleep_path': glob.glob(f"{master_folder}/SLEEP/*")[0]
                }

# %% [markdown]
# ## Automatic Heart rate

# %%
def convert_single_dt(timestr):
    input_string = str(timestr)
    local_time = datetime.strptime(input_string, '%Y-%m-%d %H:%M')
    local_tz = pytz.timezone('Asia/Calcutta')
    local_time = local_tz.localize(local_time)
    gmt_tz = pytz.timezone('GMT')
    return local_time.astimezone(gmt_tz)

hr_data = pd.read_csv(default_paths['hr_path'])

hr_points = [
    {
        "measurement": "heartrate",
        "time": convert_single_dt(f"{row.date} {row.time}"),
        "fields": {"value": int(row.heartRate)},
    }
    for row in hr_data.itertuples()
]

try:
    client.write_points(hr_points)
except InfluxDBClientError as err:
    print("\nUnable to write points to InfluxDB: %s \n" % (err))

# %% [markdown]
# ## Activity Minutes ( steps )

# %%
steps_data = pd.read_csv(default_paths['steps_path'])

steps_points = [
    {
        "measurement": "activity",
        "time": convert_single_dt(f"{row.date} {row.time}"),
        "fields": {"steps": int(row.steps)},
    }
    for row in steps_data.itertuples()
]

try:
    client.write_points(steps_points)
except InfluxDBClientError as err:
    print("\nUnable to write points to InfluxDB: %s \n" % (err))

# %% [markdown]
# ## Sleep data

# %%
sleep_data = pd.read_csv(default_paths['sleep_path'], usecols=['date', 'start','stop','deepSleepTime','shallowSleepTime','wakeTime','REMTime'])

sleep_points = [
    {
        "measurement": "sleep",
        "time": convert_single_dt(f"{row.date} 05:30"),
        "fields": {"minutes_deep": int(row.deepSleepTime),
                   "minutes_light": int(row.shallowSleepTime),
                   "minutes_rem": int(row.REMTime),
                   "minutes_awake": int(row.wakeTime),
                   "total_duration": int((datetime.strptime(row.stop,'%Y-%m-%d %H:%M:%S%z') - datetime.strptime(row.start,'%Y-%m-%d %H:%M:%S%z')).total_seconds() / 60)
                   },
    }
    for row in sleep_data.itertuples()
]

sleep_periods = [
    {
        "measurement": "sleep_periods",
        "time": datetime.strptime(row.start,'%Y-%m-%d %H:%M:%S%z'),
        "fields": {"state": 'asleep'},
    }
    for row in sleep_data.itertuples()
]

sleep_periods += [
    {
        "measurement": "sleep_periods",
        "time": datetime.strptime(row.stop,'%Y-%m-%d %H:%M:%S%z'),
        "fields": {"state": 'awake'},
    }
    for row in sleep_data.itertuples()
]

try:
    client.write_points(sleep_points)
    client.write_points(sleep_periods)
except InfluxDBClientError as err:
    print("\nUnable to write points to InfluxDB: %s \n" % (err))


