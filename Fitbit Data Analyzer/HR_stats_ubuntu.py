#!/usr/bin/env python
# coding: utf-8

# In[90]:


FITBIT_LANGUAGE = 'en_US'
import requests, sys, os
import pandas as pd
from datetime import datetime, date
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#plt.style.use('fivethirtyeight')

f = open('/home/arpan/Documents/HR_API', 'r')
FITBIT_ACCESS_TOKEN = f.read().rstrip("\n")
f.close()


# In[78]:


def fetch_HR(date):

    points = []
    points_time = []

    try:
        response = requests.get('https://api.fitbit.com/1/user/-/activities/heart/date/' + date + '/1d/1min/time/00:00/23:59.json', headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
        response.raise_for_status()
        json_data = response.json()
        innerday_HR = json_data['activities-heart-intraday']['dataset']
        
        time_list , HR_value_list = [], []

        for entry in innerday_HR:
            time_list.append(datetime.strptime(date+" "+ entry['time'], '%Y-%m-%d %H:%M:%S'))
            HR_value_list.append(entry['value'])
            
        df = pd.DataFrame({'datetime':time_list, 'HR':HR_value_list})
        df = df.set_index('datetime')
        summary_df = (df['HR'].resample('1Min').mean())
        
        return summary_df
        
    except Exception as err:
        print("\nHTTP request failed: %s \n" % (err))
        return None



# In[87]:
def fetch_steps(date):

    points = []
    points_time = []

    try:
        response = requests.get('https://api.fitbit.com/1/user/-/activities/steps/date/' + date + '/1d/1min/time/00:00/23:59.json', headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
        response.raise_for_status()
        json_data = response.json()
        innerday_steps = json_data['activities-steps-intraday']['dataset']
        
        time_list , steps_value_list = [], []

        for entry in innerday_steps:
            time_list.append(datetime.strptime(date+" "+ entry['time'], '%Y-%m-%d %H:%M:%S'))
            steps_value_list.append(entry['value'])
            
        df = pd.DataFrame({'datetime':time_list, 'steps':steps_value_list})
        df = df.set_index('datetime')
        summary_df = (df['steps'].resample('2Min').mean())
        
        return summary_df
        
    except Exception as err:
        print("\nHTTP request failed: %s \n" % (err))
        return None


# In[103]:


def animate(i):
    
    summary_df_HR = fetch_HR(date.today().__str__())
    summary_df_steps = fetch_steps(date.today().__str__())
    
    plt.cla()

    #plt.plot(summary_df)

    fig = plt.figure(1)

    fig.suptitle('Health Data', fontsize=8)

    ax = plt.subplot(2,1,1)
    summary_df_HR.plot.area(ylim=(50,130) ,xlim=(datetime.strptime(date.today().__str__()+" "+ "06:00:00", '%Y-%m-%d %H:%M:%S'), datetime.strptime(date.today().__str__()+" "+ "23:30:00", '%Y-%m-%d %H:%M:%S')))
    plt.axhline(y=100, color='r', linestyle='-')
    ax.set_title("Heart Rate")
    ax.legend()
    
    ax2 = plt.subplot(2,1,2)
    summary_df_steps.plot.area(ylim=(0,130), color = 'green', xlim=(datetime.strptime(date.today().__str__()+" "+ "06:00:00", '%Y-%m-%d %H:%M:%S'), datetime.strptime(date.today().__str__()+" "+ "23:30:00", '%Y-%m-%d %H:%M:%S')))
    plt.axhline(y=50, color='r', linestyle='-')
    ax2.set_title("Step Count")
    ax2.legend()

    print("Updated",datetime.now())


# In[104]:



ani = FuncAnimation(plt.gcf(), animate, interval=600000)

plt.tight_layout()

plt.show()
# In[ ]:




