#!/usr/bin/env python
# coding: utf-8

# <h2>HR analysis</h2>

# In[ ]:

#You need the following modues, if you don't have them, use pip install <module-name>
import requests
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


import datetime

#Update your start and end dates here in yyyy-mm-dd format 
start = datetime.datetime.strptime("2021-03-17", "%Y-%m-%d")
end = datetime.datetime.strptime("2021-03-22", "%Y-%m-%d")

date_array = (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
 
day_list = []
for date_object in date_array:
    day_list.append(date_object.strftime("%Y-%m-%d"))
    
print("day range : ",day_list)


# In[ ]:


df_all = pd.DataFrame()


# In[ ]:


# Implicit Grant Flow
#Enter your OAuth token in place
access_token = "OAuth token here"

header = {'Authorization': 'Bearer {}'.format(access_token)}

for single_day in day_list:
    response = requests.get("https://api.fitbit.com/1/user/-/activities/heart/date/"+ single_day +"/1d/1sec/time/00:00/23:59.json", headers=header).json()
    df = pd.DataFrame(response['activities-heart-intraday']['dataset'])
    date = pd.Timestamp(single_day).strftime('%Y-%m-%d')
    df = df.set_index(pd.to_datetime(date + ' ' + df['time'].astype(str)))
    #print(df)
    df_all = df_all.append(df, sort=True)
    
del df_all['time']


# In[ ]:


#Put the interval you want to take the average of the imported data from fitbit with 2-5 sec interval. Default 10 minute
summary_df = (df_all['value'].resample('10Min').mean())


# In[ ]:


plt.rcParams["figure.figsize"]=20,8

# Heart rate data summary [10min avg] from start date[2021-03-18] to end date[2021-03-21] 
#if you are using matplotlib directly in python ( py file ) then use plt.plot(summary_df,kind='area')
summary_df.plot.area()


# In[ ]:




