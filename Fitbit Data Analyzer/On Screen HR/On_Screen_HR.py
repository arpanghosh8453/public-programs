import requests, sys
from datetime import date, datetime
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import qtawesome as qta
import keyboard


FITBIT_LANGUAGE = 'en_US'
f = open('C:/Users/Arpan Ghosh/fitbit_access_token.txt', 'r')
FITBIT_ACCESS_TOKEN = f.read()
f.close()
STEPS_GOAL = 8000
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
}

QProgressBar::chunk {
    border-radius: 6px;
    background-color: #61f5a3;
}
"""

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HR Monitor")
        self.setWindowOpacity(0.7)
        self.move(0,915)
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
        self.styling_green_shoe = qta.icon('mdi.shoe-print', color='#61f5a3')
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
        self.step_progressbar.setValue(0)
        self.step_progressbar.setTextVisible(False)
        self.step_progressbar.setStyleSheet(DEFAULT_STYLE)
        self.last_update_label = QLabel("                         Last Update Time : -- : -- : -- ")
        self.last_update_label.setStyleSheet('QLabel {background-color: black; color: #f3f980; text-align:center;}')
        self.last_update_label.setFont(small_font)
        #self.last_update_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.Low_hr_button, 0, 0)
        layout.addWidget(self.Avg_hr_button, 0, 1)
        layout.addWidget(self.High_hr_button, 0, 2)
        layout.addWidget(self.steps_button,1,0)
        layout.addWidget(self.step_progressbar,1,1,1,3)
        layout.addWidget(self.last_update_label, 2,0,1,3)
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
        return (0,0,0,"00:00")

    data = response.json()

    if 'activities-heart-intraday' in data:
        for value in data['activities-heart-intraday']['dataset']:
            points.append(value['value'])
            points_time.append(value['time'])

    last_update = points_time[-1]
    avg = sum(points[-16:-1])/15
    high = max(points[-16:-1])
    low = min(points[-16:-1])

    return (high,avg,low,last_update)

def fetch_steps(date):
    try:
        response = requests.get('https://api.fitbit.com/1/user/-/' + 'activities' + '/' + 'steps' + '/date/'+date+'/1d.json', 
            headers={'Authorization': 'Bearer ' + FITBIT_ACCESS_TOKEN, 'Accept-Language': FITBIT_LANGUAGE})
        response.raise_for_status()
    except Exception as err:
        print("\nHTTP request failed: %s \n" % (err))

    data = response.json()
    return int(data['activities-steps'][0]['value'])


def update():

    high,avg,low,last_update = fetch_HR(date.today().__str__())

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

    window.last_update_label.setText("                         Last Update Time : "+last_update)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

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

    step_count = fetch_steps(date.today().__str__())
    step_percent = round(step_count*100//STEPS_GOAL)
    window.steps_button.setText(" "+str(step_percent)+"%")

    if step_count >= STEPS_GOAL:
        window.step_progressbar.setValue(100)
        window.steps_button.setIcon(window.styling_green_shoe)
        window.steps_button.setStyleSheet('QPushButton {background-color: black; color: #61f5a3;}')
        window.step_progressbar.setStyleSheet(COMPLETE_STYLE)
    else:
        window.step_progressbar.setValue(step_percent)

    print("\nLast Script run :",current_time,"|","Last Update :",last_update)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    keyboard.add_hotkey('ctrl + alt + q', window.close)
    window.show()
    timer = QTimer()
    timer.timeout.connect(update)
    timer.setInterval(120000)
    timer.start()
    sys.exit(app.exec_())