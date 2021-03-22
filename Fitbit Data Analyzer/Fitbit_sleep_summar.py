# <h2>Sleep analysis</h2>

# In[ ]:

#You need the following modues, if you don't have them, use pip install <module-name>
import requests
import pandas as pd
import matplotlib.pyplot as plt


access_token = "OAuth token here"

header = {'Authorization': 'Bearer {}'.format(access_token)}

response = requests.get("https://api.fitbit.com/1.2/user/-/sleep/date/2021-03-18/2021-03-21.json", headers=header).json()


# In[ ]:


combined_list = []
for i in range(len(response['sleep'])):
    result = response['sleep'][i]['levels']['summary']
    nice_dict = {'day':response['sleep'][i]['dateOfSleep'], 'deep_minutes':response['sleep'][i]['levels']['summary']['deep']['minutes'], 'light_minutes':response['sleep'][i]['levels']['summary']['light']['minutes'], 'rem_minutes':response['sleep'][i]['levels']['summary']['rem']['minutes'], 'wake_minutes':response['sleep'][i]['levels']['summary']['wake']['minutes']}
    combined_list.append(nice_dict)


# In[ ]:


sleep_df = pd.DataFrame(combined_list)


# In[ ]:


#Plotting data
sleep_df.set_index('day').plot(kind = 'bar')


# In[ ]: