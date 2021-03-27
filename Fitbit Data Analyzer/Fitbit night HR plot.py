#!/usr/bin/env python
# coding: utf-8

# In[37]:

#You need the following modues, if you don't have them, use pip install <module-name>
import requests
import pandas as pd
import datetime
from datetime import date
import matplotlib.pyplot as plt


# In[2]:


# Implicit Grant Flow
#Enter your OAuth token in place
#supposed to expire in 2021-03-27 - 12:40 PM - [GMT + 5:30 time zone]

access_token = "OAuth Token"


# <h2>Sleeping HR</h2>

# In[85]:


sleep_HR_date = str(date.today())


# In[86]:


splitted_date = sleep_HR_date.split('-')

year = int(splitted_date[0])
month = int(splitted_date[1])
day = int(splitted_date[2])

def parse(date):
    return "{}-{}-{}".format(date[6:], date[:2], date[3:5])

Previous_Date = datetime.datetime(year,month,day) - datetime.timedelta(days=1)
Previous_Date = parse(Previous_Date.strftime('%m/%d/%Y'))


# In[137]:


header = {'Authorization': 'Bearer {}'.format(access_token)}

response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+sleep_HR_date+"/1d/1min/time/00:00/08:00.json", headers=header).json()
response_2 = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+Previous_Date+"/1d/1min/time/22:30/23:59.json", headers=header).json()
prev_response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+Previous_Date+"/1d.json", headers=header).json()
sleep_response = requests.get("https://api.fitbit.com/1/user/-/sleep/date/"+sleep_HR_date+".json", headers=header).json()


# In[138]:


sleep_start_time = sleep_response['sleep'][0]['startTime']
sleep_end_time = sleep_response['sleep'][0]['endTime']


# In[139]:


df = pd.DataFrame(response['activities-heart-intraday']['dataset'])
df = df.set_index(pd.to_datetime(sleep_HR_date + ' ' + df['time'].astype(str)))
df2 = pd.DataFrame(response_2['activities-heart-intraday']['dataset'])
df2 = df2.set_index(pd.to_datetime(Previous_Date + ' ' + df2['time'].astype(str)))
del df['time']
del df2['time']
df = df2.append(df)

only_sleep_df = df[sleep_start_time:sleep_end_time]
# % calculation
above_resting = round((len(only_sleep_df[only_sleep_df["value"]>prev_response['activities-heart'][-1]['value']['restingHeartRate']])/len(only_sleep_df)) * 100)
below_resting = 100 - above_resting

print("Above resting HR :",above_resting,"% \n\n Below resting HR :",below_resting,"%")

# In[140]:


plt.rcParams["figure.figsize"]=16,4
plt.ylim((45,100))
plt.plot(df,label = 'Heart rate')
plt.axhline(y = prev_response['activities-heart'][-1]['value']['restingHeartRate'], color = 'r', linestyle = 'dashed', label = 'Resting HR')
plt.axvline(x = sleep_start_time, color = 'g', linestyle = 'dashed', label = "sleep start time")
plt.axvline(x = sleep_end_time, color = 'y', linestyle = 'dashed', label = 'sleep end time')
plt.title("HR Plot"+"\n\n"+"Above resting HR :"+str(above_resting)+"% & Below resting HR :"+str(below_resting)+"%")
plt.legend()
#plt.grid()
plt.show()


# In[ ]:
