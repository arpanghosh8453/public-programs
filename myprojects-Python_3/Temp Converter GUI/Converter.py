# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Arpan Ghosh\Desktop\converter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep

class Ui_window(object):
    i1 = 'Celsius'
    i2 = 'Celsius'
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(1005, 584)
        window.setFixedSize(1005, 584)
        window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        window.setWindowIcon(QtGui.QIcon(r"C:\\Users\Arpan Ghosh\Desktop\\e.png"))
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(50, 80, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(window)
        self.textEdit.setGeometry(QtCore.QRect(420, 80, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.comboBox = QtWidgets.QComboBox(window)
        self.comboBox.setGeometry(QtCore.QRect(830, 90, 125, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setCurrentText("")
        self.comboBox.setDuplicatesEnabled(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['Celsius','Fahrenheit','Kelvin'])
        self.label_2 = QtWidgets.QLabel(window)
        self.label_2.setGeometry(QtCore.QRect(30, 270, 331, 101))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QLabel(window)
        self.textEdit_2.setGeometry(QtCore.QRect(420, 280, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        #self.textEdit_2.setDisabled(True)
        self.comboBox_2 = QtWidgets.QComboBox(window)
        self.comboBox_2.setGeometry(QtCore.QRect(830, 290, 125, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(['Celsius','Fahrenheit','Kelvin'])
        self.comboBox_2.setCurrentText('Fahrenheit')
        self.pushButton = QtWidgets.QPushButton(window)
        self.pushButton.setGeometry(QtCore.QRect(40, 460, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color:rgb(151, 220, 132)")
        self.pushButton.clicked.connect(self.convert)
        self.checkBox = QtWidgets.QCheckBox(window)
        self.checkBox.setGeometry(QtCore.QRect(420, 469, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.loop)
        self.pushButton_2 = QtWidgets.QPushButton(window)
        self.pushButton_2.setGeometry(QtCore.QRect(662, 457, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setBold(True)
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color:rgb(230, 118, 81)")
        self.pushButton_2.clicked.connect(self.reset)
        self.label_3 = QtWidgets.QLabel(window)
        self.label_3.setGeometry(QtCore.QRect(900, 560, 101, 16))
        self.label_3.setObjectName("label_3")


        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Temperature Converter"))
        self.label.setText(_translate("window", "Enter the Temperature"))
        self.label_2.setText(_translate("window", "Result"))
        self.pushButton.setText(_translate("window", "Convert"))
        self.checkBox.setText(_translate("window", " Real-Time"))
        self.pushButton_2.setText(_translate("window", "Reset"))
        self.label_3.setText(_translate("window", "© Arpan Ghosh"))

    def reset(self,window):
        self.comboBox.setCurrentText('Celsius')
        self.comboBox_2.setCurrentText('Fahrenheit')
        self.checkBox.setChecked(False)
        self.textEdit_2.setText("")
        self.textEdit.setText("")
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter)

    def convert(self, window):
        self.i1 = self.comboBox.currentText()
        self.i2 = self.comboBox_2.currentText()
        try:
            inp = float(self.textEdit.toPlainText())
        except ValueError as E:
            print(E)
            self.textEdit_2.setText("Invalid Input !")
            return 0
        if self.i1 == 'Celsius':
            if self.i2 == 'Celsius':
                result = inp
            elif self.i2 == 'Kelvin':
                result = inp+273.15
            elif self.i2 == 'Fahrenheit':
                result = 9*inp/5+32
        elif self.i1 == 'Fahrenheit':
            if self.i2 == 'Celsius':
                result = ((inp-32)/9)*5
            elif self.i2 == 'Kelvin':
                result = (((inp-32)/9)*5)+273.15
            elif self.i2 == 'Fahrenheit':
                result= inp
        elif self.i1 =='Kelvin':
            if self.i2 == 'Celsius':
                result = inp-273.15
            elif self.i2 == 'Kelvin':
                result = inp
            elif self.i2 == 'Fahrenheit':
                result = 9*(inp-273.15)/5+32

        self.textEdit_2.setText(str(round(result,8)))


    def loop(self,window):
        if self.checkBox.isChecked():
            self.timer = QtCore.QTimer()
            self.timer.setInterval(0.5)
            self.timer.timeout.connect(lambda : self.convert(window))
            self.timer.start()
        else:
            self.timer.stop()
        return 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

