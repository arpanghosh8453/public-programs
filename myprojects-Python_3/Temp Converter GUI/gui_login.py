from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys,os,hashlib
from os.path import expanduser

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.access_level = 'NONE'
        self.file_store_location = expanduser("~")
        self.setObjectName("LOGIN")
        self.resize(1116, 666)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 80, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(570, 40, 20, 611))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setGeometry(QtCore.QRect(220, 70, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        #font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 210, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        #font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 420, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.user_login)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 540, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.admin_login)
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(290, 300, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.toogle)
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(750, 20, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(670, 290, 361, 61))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        #font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(770, 100, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(670, 150, 361, 61))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        #font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(670, 220, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(780, 370, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(670, 420, 361, 61))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        #font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 540, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.register)
        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setGeometry(QtCore.QRect(830, 230, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.toogle_2)
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(510, 0, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.checkBox_3 = QtWidgets.QCheckBox(self)
        self.checkBox_3.setGeometry(QtCore.QRect(890, 550, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")

        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("LOGIN", "LOGIN"))
        self.label.setText(_translate("LOGIN", "USERNAME"))
        self.label_2.setText(_translate("LOGIN", "PASSWORD"))
        self.pushButton.setText(_translate("LOGIN", "User Login"))
        self.pushButton_2.setText(_translate("LOGIN", "Admin Login"))
        self.checkBox.setText(_translate("LOGIN", "  Show Characters"))
        self.label_3.setText(_translate("LOGIN", "User Registration"))
        self.label_4.setText(_translate("LOGIN", "New Username"))
        self.label_5.setText(_translate("LOGIN", "New Password"))
        self.label_6.setText(_translate("LOGIN", "Admin Password"))
        if os.path.exists(self.file_store_location+"\\login_data.txt"):
            self.pushButton_3.setText(_translate("LOGIN", "De-Register"))
        else:
            self.pushButton_3.setText(_translate("LOGIN", "Register"))
        self.checkBox_2.setText(_translate("LOGIN", "  Show Characters"))
        self.label_7.setText(_translate("LOGIN", "© Arpan Ghosh"))
        self.checkBox_3.setText(_translate("LOGIN", " Premium Member"))




    def toogle(self):
        if self.checkBox.isChecked():
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def toogle_2(self):
        if self.checkBox_2.isChecked():
            self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)


    def admin_login(self):
        if self.lineEdit.text() == '@arpanghosh' and self.lineEdit_2.text() == 'arpanghosh8453':
            self.access_level = 'ADMIN'
            self.showdialog(QMessageBox.Information,"Admin Access Granted Successfully !","Username and password matched : You are an registered admin. Welcome ! .")
            self.accept()
        else:
            self.access_level = 'NONE'
            self.showdialog(QMessageBox.Warning,"Admin Access Not Granted !","Username or password not matched : You are not an admin. Please try other ways .")

    def user_login(self):
        if os.path.exists(self.file_store_location+"\\login_data.txt"):
            f = open(self.file_store_location+"\\login_data.txt",'r')
            data = f.read()
            f.close()
            match = data.split('\n')
        else:
            self.showdialog(QMessageBox.Warning,"File Not Found !","Username or password is not valid : You are not registered. Please contact admin Arpan ghosh to register as a new user .")
            self.access_level = 'NONE'
        if hashlib.sha256(self.lineEdit.text().encode('utf-8')).hexdigest() == match[0] and hashlib.sha256(self.lineEdit_2.text().encode('utf-8')).hexdigest() == match[1]:
            self.showdialog(QMessageBox.Information,"User Access Granted Successfully !","Username and password matched : You are an registered User. Welcome ! .")
            self.access_level = 'USER'
            self.accept()
        elif hashlib.sha256(self.lineEdit.text().encode('utf-8')).hexdigest() == match[0] and hashlib.sha256((self.lineEdit_2.text()+'premium').encode('utf-8')).hexdigest() == match[1]:
            self.showdialog(QMessageBox.Information,"Premium User Access Granted Successfully !","Username and password matched : You are an registered Premium User. Welcome ! .")
            self.access_level = 'PREMIUM'
            self.accept()
        else:
            self.showdialog(QMessageBox.Warning,"User Access Not Granted !","Username or password not matched with registred user : You are not an user. Please try other ways .")
            self.access_level = 'NONE'

    def register(self):
        if os.path.exists(self.file_store_location+"\\login_data.txt"):
            if self.lineEdit_5.text() == 'arpanghosh8453':
                os.remove(self.file_store_location+"\\login_data.txt")
                self.showdialog(QMessageBox.Information,"User Successfully De-Registered  !","To Re-register , Contact Admin Arpan Ghosh")
                self.pushButton_3.setText(QtCore.QCoreApplication.translate("LOGIN", "Register"))
            else:
                self.showdialog(QMessageBox.Warning,"Unable to De-Register !","Wrong Admin Password : To De-register , Contact Admin Arpan Ghosh")
        else:
            if self.lineEdit_5.text() == 'arpanghosh8453':
                username = self.lineEdit_4.text()
                password = self.lineEdit_3.text()
                if username == '' or password == '':
                    self.showdialog(QMessageBox.Warning,"Unable To Register !","Username and Password must be provided : You are not registered. To register, Contact Admin Arpan Ghosh")
                    return 0
                if self.checkBox_3.isChecked():
                    password = password+'premium'
                f = open(self.file_store_location+"\\login_data.txt",'w')
                f.write(hashlib.sha256(username.encode('utf-8')).hexdigest()+'\n'+hashlib.sha256(password.encode('utf-8')).hexdigest())
                f.close()
                if self.checkBox_3.isChecked():
                    self.showdialog(QMessageBox.Information,"Premium User Successfully Registered!","Username and password Saved  : You are an registered Premium User now . Please proceed to Login .")
                else:
                    self.showdialog(QMessageBox.Information,"User Successfully Registered!","Username and password Saved  : You are an registered User now . Please proceed to Login .")
                self.pushButton_3.setText(QtCore.QCoreApplication.translate("LOGIN", "De-Register"))
            else:
                self.showdialog(QMessageBox.Warning,"Unable To Register !","Admin password is not correct : You are not registered. To register, Contact Admin Arpan Ghosh")

    def showdialog(self,icon,text,details):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText("LOGIN STATUS")
        msg.setInformativeText(text)
        msg.setWindowTitle("Login")
        msg.setDetailedText(details)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msg.buttonClicked.connect(msgbtn)
        retval = msg.exec_()



#-------------------------------------IMPORT SYNTAX-------------------------------------------
'''
if __name__ == '__main__':
    #---------------------for login form-----------------------------
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = gui_login.Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        #--------Main Dialog opens-----------------------
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        if login.access_level == 'USER': # access level check
            ui.checkBox.setEnabled(False)
        Dialog.show()
        sys.exit(app.exec_())
    else:
        pass
'''