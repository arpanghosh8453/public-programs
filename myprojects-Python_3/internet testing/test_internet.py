import requests, sys, socket
from datetime import date, datetime
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import qtawesome as qta

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Internet")
        self.setWindowOpacity(0.8)
        self.move(1810,980)
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
        self.styling_icon_true = qta.icon('fa5s.circle',color='#5CB323')
        self.styling_icon_false = qta.icon('fa5s.circle',color='#F70000')
        self.styling_icon_checking = qta.icon('fa5s.circle',color='#F7C600')
        self.Low_hr_button = QPushButton(self.styling_icon_false, "offline")
        self.Low_hr_button.setStyleSheet('QPushButton {background-color: black; color: #F70000;}')
        self.Low_hr_button.setFont(myfont)
        #self.last_update_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.Low_hr_button, 0, 0)
        # Set the layout on the application's window
        self.setLayout(layout)

def check_internet():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

def update():
    window.Low_hr_button.setIcon(window.styling_icon_checking)
    window.Low_hr_button.setText("checking")
    window.Low_hr_button.setStyleSheet('QPushButton {background-color: black; color: #F7C600;}')

    if check_internet():
        window.Low_hr_button.setIcon(window.styling_icon_true)
        window.Low_hr_button.setText("online")
        window.Low_hr_button.setStyleSheet('QPushButton {background-color: black; color: #5CB323;}')
    else:
        window.Low_hr_button.setIcon(window.styling_icon_false)
        window.Low_hr_button.setText("offline")
        window.Low_hr_button.setStyleSheet('QPushButton {background-color: black; color: #F70000;}')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    timer = QTimer()
    timer.timeout.connect(update)
    timer.setInterval(1000)
    timer.start()
    sys.exit(app.exec_())