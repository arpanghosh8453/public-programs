import requests, sys, time
from datetime import date, datetime
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import qtawesome as qta
from win10toast import ToastNotifier
import keyboard


FITBIT_LANGUAGE = 'en_US'
f = open('C:/Users/Arpan Ghosh/fitbit_access_token.txt', 'r')
FITBIT_ACCESS_TOKEN = f.read()
f.close()

STEPS_GOAL = 8000
STEPS_FULL = 10000
ACTIVITY_PERCENTAGE_GOAL = 50

DEFAULT_STYLE = """
QProgressBar{
    min-height: 6px;
    max-height: 6px;
    border-radius: 4px;
}

QProgressBar::chunk {
    border-radius: 6px;
    background-color: red;
}
"""

COMPLETE_STYLE = """
QProgressBar{
    min-height: 6px;
    max-height: 6px;
    border-radius: 4px;
}ṭ

QProgressBar::chunk {
    border-radius: 6px;
    background-color: #61f5a3;
}
"""

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HR Monitor")
        self.setWindowOpacity(0.6)
        self.move(0,880)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setWindowFlags(Qt.Window|Qt.X11BypassWindowManagerHint|Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint|Qt.ToolTip)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.pressing = False
        # Create a QGridLayout instance
        layout = QGridLayout()
        myfont = QFont('Roboto', 10)
        myfont.setBold(True)
        small_font = QFont('Roboto', 6)
        small_font.setBold(True)
        # Add widgets to the layout
        self.styling_icon_normal = qta.icon('ei.heart',color='#f3f980')
        self.styling_icon_low = qta.icon('ei.heart-alt',color='#61f5a3')
        self.styling_icon_high = qta.icon('fa5s.heart-broken',color='#fb697c')
        self.styling_icon_missing = qta.icon('mdi.heart-off', color='#8fc9f8')
        self.styling_shoe = qta.icon('mdi.shoe-print', color='white')
        self.styling_running = qta.icon('fa5s.running', color='white')
        self.styling_green_shoe = qta.icon('mdi.shoe-print', color='#61f5a3')
        self.styling_green_running = qta.icon('fa5s.running', color='#61f5a3')
        self.Low_hr_button = QPushButton(self.styling_icon_low, "LHR")
        self.Low_hr_button.setStyleSheet('QPushButton {background-color: black; color: #61f5a3;}')
        self.Low_hr_button.setFont(myfont)
        self.Avg_hr_button = QPushButton(self.styling_icon_normal, "HR")
        self.Avg_hr_button.setStyleSheet('QPushButton {background-color: black; color: #f3f980;}')
        self.Avg_hr_button.setFont(myfont)
        self.High_hr_button = QPushButton(self.styling_icon_high, "HHR")
        self.High_hr_button.setStyleSheet('QPushButton {background-color: black; color: #fb697c;}')
        self.High_hr_button.setFont(myfont)
        self.steps_button = QPushButton(self.styling_shoe, "Steps")
        self.steps_button.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.steps_button.setFont(myfont)
        self.step_progressbar = QProgressBar(minimum=0, maximum=100)
        self.step_progressbar.setTextVisible(False)
        self.step_progressbar.setStyleSheet(DEFAULT_STYLE)
        self.activity_button = QPushButton(self.styling_running, "Acts")
        self.activity_button.setStyleSheet('QPushButton {background-color: black; color: white;}')
        self.activity_button.setFont(myfont)
        self.activity_progressbar = QProgressBar(minimum=1, maximum=100)
        self.activity_progressbar.setTextVisible(False)
        self.activity_progressbar.setStyleSheet(DEFAULT_STYLE)
        self.step_progressbar.setValue(0)
        self.activity_progressbar.setValue(0)
        self.last_update_label = QLabel("                         Last Update Time : -- : -- : -- ")
        self.last_update_label.setStyleSheet('QLabel {background-color: black; color: #f3f980; text-align:center;}')
        self.last_update_label.setFont(small_font)
        #self.last_update_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.Low_hr_button, 0, 0)
        layout.addWidget(self.Avg_hr_button, 0, 1)
        layout.addWidget(self.High_hr_button, 0, 2)
        layout.addWidget(self.steps_button,1,0)
        layout.addWidget(self.step_progressbar,1,1,1,3)
        layout.addWidget(self.activity_button,2,0)
        layout.addWidget(self.activity_progressbar,2,1,2,3)
        layout.addWidget(self.last_update_label, 3,0,3,3)
        # Set the layout on the application's window
        self.setLayout(layout)

def fetch_HR(date):

    points = []
    points_time = []

    try:
        response = requests.get('https://api.fitbit.com/1/user/-/activities/heart/date/' + date + '/1d/1min.json', headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
        response.raise_for_status()
    except Exception as err:
        print("\nHTTP request failed: %s \n" % (err))
        return (None,None,None,"Failed",None)

    data = response.json()

    if 'activities-heart-intraday' in data:
        for value in data['activities-heart-intraday']['dataset']:
            points.append(value['value'])
            points_time.append(value['time'])

    last_update = points_time[-1]
    avg = sum(points[-16:-1])/15
    high = max(points[-16:-1])
    low = min(points[-16:-1])
    detailed_list = []

    for i in range(15):
        detailed_list.append(points_time[-16:-1][i]+" >> "+str(points[-16:-1][i]))
    detailed_str = "\n".join(detailed_list)

    #detailed = "\n".join(map(str,points[-16:-1]))

    return (high,avg,low,last_update,detailed_str)

def fetch_steps(date):
    try:
        response = requests.get('https://api.fitbit.com/1/user/-/' + 'activities' + '/' + 'steps' + '/date/'+date+'/1d.json', 
            headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
        response.raise_for_status()
    except Exception as err:
        print("\nHTTP request failed: %s \n" % (err))
        return None

    data = response.json()
    return int(data['activities-steps'][0]['value'])

def fetch_activity_percent(date):
    try:
        response = requests.get('https://api.fitbit.com/1/user/-/activities/date/'+date+'.json', 
            headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
        response.raise_for_status()
    except Exception as err:
        print("\nHTTP request failed: %s \n" % (err))
        return None

    data = response.json()
    sm = data['summary']["sedentaryMinutes"]
    fam = data['summary']["fairlyActiveMinutes"] 
    vam = data['summary']["veryActiveMinutes"]
    lam = data['summary']["lightlyActiveMinutes"]

    total = sm + vam + lam + fam
    active_total = (vam * 1.8) + (fam * 1.4) + lam
    activity_percent = round((active_total/total)*100)

    if activity_percent > 100:
        return 100
    else:
        return activity_percent
    
prev_detailed = ""

def update():


    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    global prev_detailed

    #HR Update
    high,avg,low,last_update,detailed_HR = fetch_HR(date.today().__str__())

    if high != None:
        if low < 65:
            window.Low_hr_button.setIcon(window.styling_icon_low)
            window.Low_hr_button.setStyleSheet('QPushButton {background-color: black; color: #61f5a3;}')
        elif low > 80:
            window.Low_hr_button.setIcon(window.styling_icon_high)
            window.Low_hr_button.setStyleSheet('QPushButton {background-color: black; color: #fb697c;}')
        else:
            window.Low_hr_button.setIcon(window.styling_icon_normal)
            window.Low_hr_button.setStyleSheet('QPushButton {background-color: black; color: #f3f980;}')

        window.Low_hr_button.setText(str(low))

        if high < 80:
            window.High_hr_button.setIcon(window.styling_icon_low)
            window.High_hr_button.setStyleSheet('QPushButton {background-color: black; color: #61f5a3;}')
        elif high > 100:
            window.High_hr_button.setIcon(window.styling_icon_high)
            window.High_hr_button.setStyleSheet('QPushButton {background-color: black; color: #fb697c;}')
        else:
            window.High_hr_button.setIcon(window.styling_icon_normal)
            window.High_hr_button.setStyleSheet('QPushButton {background-color: black; color: #f3f980;}')

        window.High_hr_button.setText(str(high))

        if avg < 70:
            window.Avg_hr_button.setIcon(window.styling_icon_low)
            window.Avg_hr_button.setStyleSheet('QPushButton {background-color: black; color: #61f5a3;}')
        elif avg > 90:
            window.Avg_hr_button.setIcon(window.styling_icon_high)
            window.Avg_hr_button.setStyleSheet('QPushButton {background-color: black; color: #fb697c;}')
        else:
            window.Avg_hr_button.setIcon(window.styling_icon_normal)
            window.Avg_hr_button.setStyleSheet('QPushButton {background-color: black; color: #f3f980;}')

        window.Avg_hr_button.setText(str(round(avg)))

        update_delay_mins = round((datetime.strptime(current_time , '%H:%M:%S') - datetime.strptime(last_update , '%H:%M:%S')).total_seconds()/60)

        window.last_update_label.setText("       Last Update Time : "+last_update+"    |   "+str(update_delay_mins)+" minutes ago")

        if (datetime.strptime(current_time , '%H:%M:%S') - datetime.strptime(last_update , '%H:%M:%S')).total_seconds() >= 1800:
            window.Low_hr_button.setText("LHR")
            window.Low_hr_button.setIcon(window.styling_icon_missing)
            window.Low_hr_button.setStyleSheet('QPushButton {background-color: black; color: #8fc9f8;}')
            window.High_hr_button.setText("HHR")
            window.High_hr_button.setIcon(window.styling_icon_missing)
            window.High_hr_button.setStyleSheet('QPushButton {background-color: black; color: #8fc9f8;}')
            window.Avg_hr_button.setText("HR")
            window.Avg_hr_button.setIcon(window.styling_icon_missing)
            window.Avg_hr_button.setStyleSheet('QPushButton {background-color: black; color: #8fc9f8;}')

    else:
        print("HR Update failed")
        window.last_update_label.setText("                         Last Update Time : "+"Update Failed")

    if last_update == "Failed":
        window.Low_hr_button.setText("LHR")
        window.Low_hr_button.setIcon(window.styling_icon_missing)
        window.Low_hr_button.setStyleSheet('QPushButton {background-color: black; color: #8fc9f8;}')
        window.High_hr_button.setText("HHR")
        window.High_hr_button.setIcon(window.styling_icon_missing)
        window.High_hr_button.setStyleSheet('QPushButton {background-color: black; color: #8fc9f8;}')
        window.Avg_hr_button.setText("HR")
        window.Avg_hr_button.setIcon(window.styling_icon_missing)
        window.Avg_hr_button.setStyleSheet('QPushButton {background-color: black; color: #8fc9f8;}')
    

    # Steps update
    step_count = fetch_steps(date.today().__str__())

    if step_count != None:
        step_percent = round(step_count*100//STEPS_FULL)
        window.steps_button.setText(" "+str(step_percent)+"%")

        if step_count >= STEPS_GOAL:
            if step_percent > 100:
                window.step_progressbar.setValue(100)
            else:
                window.step_progressbar.setValue(step_percent)
            window.steps_button.setIcon(window.styling_green_shoe)
            window.steps_button.setStyleSheet('QPushButton {background-color: black; color: #61f5a3;}')
            window.step_progressbar.setStyleSheet(COMPLETE_STYLE)
        else:
            window.step_progressbar.setValue(step_percent)
    else:
        print("Steps update failed")
        window.last_update_label.setText("                         Last Update Time : "+"Update Failed")

    # Activity Update
    activity_percent = fetch_activity_percent(date.today().__str__())
    if activity_percent != None:
        window.activity_button.setText(" "+str(activity_percent)+"%")
        window.activity_progressbar.setValue(activity_percent)

        if activity_percent >= ACTIVITY_PERCENTAGE_GOAL:
            window.activity_button.setIcon(window.styling_green_running)
            window.activity_button.setStyleSheet('QPushButton {background-color: black; color: #61f5a3;}')
            window.activity_progressbar.setStyleSheet(COMPLETE_STYLE)
        else:
            window.activity_button.setIcon(window.styling_running)
            window.activity_button.setStyleSheet('QPushButton {background-color: black; color: white;}')
            window.activity_progressbar.setStyleSheet(DEFAULT_STYLE)
    else:
        print("Activity update failed")
        window.last_update_label.setText("                         Last Update Time : "+"Update Failed")


    print("\nLast Script run :",current_time,"|","Last Update :",last_update)

    #Alert message
    '''
    if high != None:
        if prev_detailed != detailed_HR:
            if (low > 80 and high > 110) and avg > 95:
            #if (low > 65 and high > 90) and avg > 72:
                msg = QMessageBox()
                msg.setWindowTitle("HR Alert")
                msg.setIcon(QMessageBox.Warning)
                msg.setText("High Heart Rate")
                msg.setStandardButtons(QMessageBox.Ignore)
                msg.setDetailedText(detailed_HR)
                x = msg.exec_()

            prev_detailed = detailed_HR
    '''
    if high != None:
        if prev_detailed != detailed_HR:
            if (low > 80 and high > 110) and avg > 95:
                toast = ToastNotifier()
                toast.show_toast("HR Alert","High Heart Rate detected",duration=8,icon_path=r"D:\docker_volumes\On Screen HR\heart.ico", threaded = True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    keyboard.add_hotkey('alt + t', app.quit)
    #keyboard.add_hotkey('alt + u', update)
    update()
    window.show()
    timer = QTimer()
    timer.timeout.connect(update)
    timer.setInterval(120000)
    timer.start()
    sys.exit(app.exec_())