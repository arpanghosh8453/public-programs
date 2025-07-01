# %% [markdown]
# ## Import required modules

# %%
import requests, random, string, time, sys, re, os, glob, pyzipper, shutil, pytz, base64
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urlextract import URLExtract
import pandas as pd
from datetime import datetime, timedelta
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBClientError
from dotenv import dotenv_values

REDIRECT_URI = 'http://localhost/8080'
INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = base64.b64decode(dotenv_values('C:/Users/thisi/OneDrive/Desktop/Python codes/.env')['INFLUX_USERNAME']).decode('utf-8')
INFLUXDB_PASSWORD = base64.b64decode(dotenv_values('C:/Users/thisi/OneDrive/Desktop/Python codes/.env')['INFLUX_USER_PASSWORD']).decode('utf-8')
username = base64.b64decode(dotenv_values('C:/Users/thisi/OneDrive/Desktop/Python codes/.env')['HUAMI_USERNAME']).decode('utf-8')
password = base64.b64decode(dotenv_values('C:/Users/thisi/OneDrive/Desktop/Python codes/.env')['HUAMI_PASSWORD']).decode('utf-8')
INFLUXDB_DATABASE = 'amazfit'
DOWNLOAD_DIR = "D:\\Downloads\\huami-temp-zip"

# %% [markdown]
# ## Temp Email creation

# %%

API = 'https://www.1secmail.com/api/v1/'
domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
domain = random.choice(domainList)

def generateUserName(l):
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(l))
    return username

def extract():
    getUserName = re.search(r'login=(.*)&',newMail).group(1)
    getDomain = re.search(r'domain=(.*)', newMail).group(1)
    return [getUserName, getDomain]

def print_statusline(msg: str):
    last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
    print(' ' * last_msg_length, end='\r')
    print(msg, end='\r')
    sys.stdout.flush()
    print_statusline.last_msg = msg

def deleteMail():
    url = 'https://www.1secmail.com/mailbox'
    data = {
        'action': 'deleteMailbox',
        'login': f'{extract()[0]}',
        'domain': f'{extract()[1]}'
    }

    print_statusline("Disposing your email address - " + mail + '\n')
    req = requests.post(url, data=data)

def checkMails():
    reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
    req = requests.get(reqLink).json()
    length = len(req)
    if length == 0:
        return (False,{})
    else:
        print(length,"messages found!")
        idList = []
        for i in req:
            for k,v in i.items():
                if k == 'id':
                    mailId = v
                    idList.append(mailId)

        for i in idList:
            msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
            req = requests.get(msgRead).json()
        return (True,req)
        

try:
    userInput2 = generateUserName(25)
    newMail = f"{API}?login={userInput2}&domain={domain}"
    reqMail = requests.get(newMail)
    mail = f"{extract()[0]}@{extract()[1]}"
    print("\nYour temporary email is " + mail +"\n")
    gotmessage = False

except(KeyboardInterrupt):
    deleteMail()
    print("\nProgramme Interrupted")

# %% [markdown]
# ## Login automation

# %%
print("Automating login and data export from user.huami.com....")

MaxDelay = 8

prefs = {"download.default_directory" : DOWNLOAD_DIR}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('chromedriver',options=chrome_options)
# Launch the browser and open the github URL in your web driver.
driver.get(" https://user.huami.com/privacy2/index.html?loginPlatform=web&platform_app=com.huami.watch.hmwatchmanager&v=4.0.17")

WebDriverWait(driver, MaxDelay).until(EC.presence_of_element_located((By.CLASS_NAME, 'gdpr-operation-output')))

driver.find_element(By.CLASS_NAME, "gdpr-operation-output").click()

WebDriverWait(driver, MaxDelay).until(EC.presence_of_element_located((By.ID, 'hm_login_registration')))

driver.find_element(By.ID, "hm_login_registration").send_keys(username)
# find password input field and insert password as well
driver.find_element(By.ID, "hm_login_password").send_keys(password)
# click login button
driver.find_element(By.CSS_SELECTOR , ".ant-btn.ant-btn-default.ant-btn-lg.hm-login-form-login.hm-login-form-button").click()

WebDriverWait(driver, MaxDelay).until(EC.presence_of_element_located((By.CLASS_NAME, 'gdpr-operation-output')))

driver.find_element(By.CLASS_NAME, "gdpr-operation-output").click()

WebDriverWait(driver, MaxDelay).until(EC.presence_of_element_located((By.CLASS_NAME, 'gdpr-confirm-footer-btn')))

driver.find_element(By.CLASS_NAME, "gdpr-confirm-footer-btn").click()

WebDriverWait(driver, MaxDelay).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-picker-input input")))

checkboxes = driver.find_elements(By.CSS_SELECTOR, ".ant-checkbox input[type='checkbox']")

for checkbox in checkboxes:
    checkbox.click()

dateboxes = driver.find_elements(By.CSS_SELECTOR, ".ant-picker-input input")

current_date = datetime.now().strftime('%Y-%m-%d')
past_date = datetime.now() - timedelta(days=7)
past_date_str = past_date.strftime('%Y-%m-%d')

dateboxes[0].send_keys(past_date_str)
dateboxes[1].send_keys(current_date)

driver.find_element(By.CLASS_NAME, "gdpr-export-data-footer-confirm").click()

WebDriverWait(driver, MaxDelay).until(EC.presence_of_element_located((By.CLASS_NAME, "gdpr-code-image")))

driver.find_element(By.CSS_SELECTOR, ".gdpr-email-input > .ant-input").send_keys(mail)

capcha = driver.find_element(By.CLASS_NAME, "gdpr-code-image").get_attribute("innerText").replace("\n", "")

driver.find_element(By.CSS_SELECTOR, ".gdpr-code-input > .ant-input").send_keys(capcha)

driver.find_element(By.CLASS_NAME, "gdpr-email-footer-confirm").click()

# %% [markdown]
# ## Extract zip file link from email and dispose email

# %%
print("Waiting for email...")

while not gotmessage:
        gotmessage, contents = checkMails()
        if gotmessage:
                deleteMail()
        else:
                time.sleep(5)

extractor = URLExtract()
urls = extractor.find_urls(contents['body'])
zipfileurl = urls[0]
print(zipfileurl)

# %% [markdown]
# ## Download zip file

# %%
print("Downloading zip file....")

driver.get(zipfileurl)
WebDriverWait(driver, MaxDelay).until(EC.presence_of_element_located((By.CLASS_NAME, "gdpr-download-data-desc")))
time.sleep(2)
zippassword = driver.find_element(By.CLASS_NAME, "gdpr-download-data-desc").get_attribute("innerText").split(":")[1].strip()
driver.find_element(By.CLASS_NAME, "gdpr-download-data-export").click()
time.sleep(3)

# %% [markdown]
# ## Extract zip file and quit driver

# %%
zip_file = sorted(glob.glob(DOWNLOAD_DIR+"\*.zip"), key=os.path.getmtime)[-1]
extracted_path = zip_file[:-4]

print("Extracting",zip_file,"with password",zippassword,"...")

with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
    extracted_zip.extractall(pwd=str.encode(zippassword), path=extracted_path)

driver.quit()

# %% [markdown]
# ## Write data to influxdb

# %%
print("Connecting to influxdb...")

try:
    client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    client.switch_database(INFLUXDB_DATABASE)
except InfluxDBClientError as err:
    print("\nInfluxDB connection failed: %s \n" % (err))

# %%
master_folder = extracted_path

default_paths = {'hr_path': glob.glob(f"{master_folder}/HEARTRATE_AUTO/*")[0], 
                 'steps_path': glob.glob(f"{master_folder}/ACTIVITY_MINUTE/*")[0], 
                 'sleep_path': glob.glob(f"{master_folder}/SLEEP/*")[0]
                }

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
    print("\nHR data updated to database")
except InfluxDBClientError as err:
    print("\nUnable to write points to InfluxDB: %s \n" % (err))

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
    print("\nSteps data updated to database")
except InfluxDBClientError as err:
    print("\nUnable to write points to InfluxDB: %s \n" % (err))

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
        "fields": {"state": 1},
    }
    for row in sleep_data.itertuples()
]

sleep_periods += [
    {
        "measurement": "sleep_periods",
        "time": datetime.strptime(row.stop,'%Y-%m-%d %H:%M:%S%z'),
        "fields": {"state": 0},
    }
    for row in sleep_data.itertuples()
]

try:
    client.write_points(sleep_points)
    client.write_points(sleep_periods)
    print("\nSleep data updated to database")
except InfluxDBClientError as err:
    print("\nUnable to write points to InfluxDB: %s \n" % (err))



# %% [markdown]
# ## Clean up zip file

# %%
print("\nCleaning up zip files...")

shutil.rmtree(DOWNLOAD_DIR)
os.makedirs(DOWNLOAD_DIR)

print("\nAll Done!")

# %%



