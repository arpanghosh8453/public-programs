from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QTableView, QFileDialog
import os
import os.path
from os.path import expanduser
import matplotlib.pyplot as plt
import pandas
from PyQt5.QtCore import QAbstractTableModel, Qt

GERMAN_VERSION = True

class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df = pandas.DataFrame(), parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.iloc[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()


class Show_data(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=None)
        vLayout = QtWidgets.QVBoxLayout(self)
        hLayout = QtWidgets.QHBoxLayout()
        self.loadBtn = QtWidgets.QPushButton("Save File", self)
        vLayout.addLayout(hLayout)
        self.pandasTv = QtWidgets.QTableView(self)
        hLayout.addWidget(self.pandasTv)
        #self.pandasTv.setEnabled(False)
        vLayout.addWidget(self.loadBtn)
        self.loadBtn.clicked.connect(self.saveFile)
        self.pandasTv.setSortingEnabled(True)
        model = PandasModel(ui.data_)
        self.pandasTv.setModel(model)

    def saveFile(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(None, "Save Data to file", ".", "CSV file (*.csv)")[0]
        if fileName:
            try:
                ui.data_.to_csv(fileName,index=False,sep='\t',encoding='utf-8')
                ui.textBrowser.append('File Saved Successfully !\n')
            except:
                ui.textBrowser.append('File is Already open by another Process or Permission Denied to location : Unable to save !\n')
        else:
            ui.textBrowser.append('No file chosen : Unable to save !\n')     


class Show_info(object):
    def setupUi(self, Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(700, 500)
            Dialog.setFixedSize(700,500)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            Dialog.setWindowIcon(icon)
            self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.verticalLayout = QtWidgets.QVBoxLayout()
            self.verticalLayout.setObjectName("verticalLayout")
            self.textBrowser = QtWidgets.QTextBrowser(Dialog)
            self.textBrowser.setOpenExternalLinks(True)
            self.textBrowser.setOpenLinks(True)
            self.textBrowser.setObjectName("textBrowser")
            font = QtGui.QFont()
            font.setPointSize(11)
            self.textBrowser.setFont(font)
            self.textBrowser.setText('\nQuick Look :\n\n'+ui.info+'\n')
            self.verticalLayout.addWidget(self.textBrowser)
            self.verticalLayout_2.addLayout(self.verticalLayout)
            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.setObjectName("pushButton")
            self.verticalLayout_2.addWidget(self.pushButton)
            self.pushButton.clicked.connect(self.save_info)

            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog) 

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Save"))

    def save_info(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(None, "Save Info to file", ".", "Text file (*.txt)")[0]
        if fileName:
            try:
                fhandle = open(fileName,'w')
                fhandle.write(ui.info)
                fhandle.close()
                ui.textBrowser.append('File Saved Successfully !\n')
            except Exception as e:
                ui.textBrowser.append("ERROR : "+str(e)+'File is Already open by another Process or permission denied : Unable to save !\n')
        else:
            ui.textBrowser.append('No file chosen : Unable to save !\n')


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1079, 590)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(690, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(880, 560, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 130, 1041, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 150, 391, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(210, 40, 131, 31))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit_2.setGeometry(QtCore.QRect(210, 100, 131, 31))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 40, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 100, 81, 21))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 150, 211, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(70, 40, 121, 21))
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 90, 121, 21))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(70, 140, 121, 21))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(70, 190, 121, 21))
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(740, 160, 221, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 141, 21))
        self.label_6.setObjectName("label_6")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox.setGeometry(QtCore.QRect(170, 40, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_2.setGeometry(QtCore.QRect(170, 90, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(170, 340, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 510, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(710, 330, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(710, 420, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(950, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(920, 400, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(920, 450, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(920, 500, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 370, 361, 192))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(130, 20, 531, 100))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(920, 350, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(690, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(820, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton.clicked.connect(self.get_file_name)
        self.pushButton_2.clicked.connect(self.find_default)
        self.pushButton_3.clicked.connect(self.calculate)
        self.pushButton_4.clicked.connect(self.graph_plot)
        self.pushButton_5.clicked.connect(self.show_summary_table)
        self.pushButton_8.clicked.connect(self.show_details)
        self.pushButton_9.clicked.connect(self.clear)
        self.pushButton_6.clicked.connect(self.convert_german)
        self.checkBox_5.stateChanged.connect(self.check_german)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser_2.setFont(font)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bank Balance Analyser (German version)"))
        self.label.setText(_translate("Dialog", "File Name"))
        self.pushButton.setText(_translate("Dialog", "Open"))
        self.pushButton_2.setText(_translate("Dialog", "Default"))
        self.label_2.setText(_translate("Dialog", "Developed by Arpan Ghosh"))
        self.groupBox.setTitle(_translate("Dialog", "Date Selection"))
        self.label_3.setText(_translate("Dialog", "Start Date"))
        self.label_4.setText(_translate("Dialog", "End Date"))
        self.groupBox_2.setTitle(_translate("Dialog", " Group By"))
        self.radioButton.setText(_translate("Dialog", "Year"))
        self.radioButton_2.setText(_translate("Dialog", "Month"))
        self.radioButton_3.setText(_translate("Dialog", "Week"))
        self.radioButton_4.setText(_translate("Dialog", "Day"))
        self.groupBox_3.setTitle(_translate("Dialog", "Data Selection"))
        self.label_5.setText(_translate("Dialog", "Skip Top Rows"))
        self.label_6.setText(_translate("Dialog", "Skip Bottom Rows"))
        self.label_7.setText(_translate("Dialog", "Log Record"))
        self.pushButton_3.setText(_translate("Dialog", "Calculate"))
        self.pushButton_4.setText(_translate("Dialog", "Graph"))
        self.pushButton_5.setText(_translate("Dialog", "Summary"))
        self.pushButton_8.setText(_translate("Dialog", "Details"))
        self.pushButton_9.setText(_translate("Dialog", "Clear"))
        self.checkBox.setText(_translate("Dialog", " Credit"))
        self.checkBox_2.setText(_translate("Dialog", "Debit"))
        self.checkBox_3.setText(_translate("Dialog", "Savings"))
        self.checkBox_4.setText(_translate("Dialog", "Grid"))
        self.checkBox_5.setText(_translate("Dialog", " Sparda Bank"))
        self.pushButton_6.setText(_translate("Dialog", "Convert"))

    def get_file_name(self):
        self.filename = QFileDialog.getOpenFileName(None, 'Open file', expanduser('~'),"Excel files (*.xls , *.csv)")
        self.textBrowser_2.setText(self.filename[0])
        if self.filename[0]:
            self.textBrowser.append("successfully Located File : "+self.filename[0]+'\n')
            self.pushButton_2.setEnabled(True)
            if self.checkBox_5.isChecked():
                self.auto_convert()
        if self.filename[0]:
            if self.checkBox_5.isChecked():
                self.textBrowser_2.setText(" [CONVERTED] "+self.filename[0])
            self.find_default()
        else:
            self.textBrowser.append("No File Chosen !\n")
            self.pushButton_2.setEnabled(False)
            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)
            self.radioButton_3.setEnabled(False)
            self.radioButton_4.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.checkBox_2.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.dateEdit.setEnabled(False)
            self.dateEdit_2.setEnabled(False)
            #self.spinBox.setEnabled(False)
            #self.spinBox_2.setEnabled(False)

    def to_float(self,value):
        try:
            if type(value) == str:
                value = value.replace(',','')
            f_ = float(value)
            return f_
        except Exception:
            return 0.0
        


    def find_default(self):
        try:
            file_path = self.filename[0]
            f = open(file_path,'r')
            my_list = f.read().split('\n')
            skip_r = 18
            for text in my_list:
                if text.startswith('Txn Date'):
                    skip_r = my_list.index(text)
                    break
            if skip_r == 0:
                skip_f = 0
            else:
                skip_f = 3

            data = pandas.read_csv(file_path,sep = '\t',skiprows=skip_r,skipfooter=skip_f,engine='python',encoding='utf8')
            #data = pandas.read_excel(file_path,skiprows=skip_r,skipfooter=skip_f)
            try:
                data['Debit'] = data['        Debit']
            except KeyError:
                self.textBrowser.append('Debit Spacing Already fixed\n')
            try:
                data['Txn Date'] = data['Txn Date'].apply(lambda x: datetime.strptime(x, '%d %b %Y'))
                data['Value Date'] = data['Value Date'].apply(lambda x: datetime.strptime(x, '%d %b %Y'))
            except:
                data['Txn Date'] = data['Txn Date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
                data['Value Date'] = data['Value Date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
            start_date = str(data['Txn Date'].min().date())
            end_date = str(data['Txn Date'].max().date())
            data['Credit'] = data['Credit'].apply(lambda x: self.to_float(x))
            data['Debit'] = data['Debit'].apply(lambda x: self.to_float(x))
            #self.dateEdit.setDateTime(QtCore.QDateTime.fromString(start_date, 'yyyy-mm-dd'))
            #self.dateEdit_2.setDateTime(QtCore.QDateTime.fromString(end_date, "yyyy-mm-dd"))
            l = start_date.split('-')
            self.dateEdit.setDate(QtCore.QDate(int(l[0]),int(l[1]),int(l[2])))
            l = end_date.split('-')
            self.dateEdit_2.setDate(QtCore.QDate(int(l[0]),int(l[1]),int(l[2])))
            self.radioButton_2.setChecked(True)
            self.spinBox.setValue(skip_r)
            self.spinBox_2.setValue(skip_f)
            self.textBrowser.append('Default Values are now set \n')
            
        except Exception as e:
            self.textBrowser.append("ERROR : "+str(e)+'\n')
            self.textBrowser.append('Warning : Default File format is not matching [may need conversion to proper format] !\n\nUnable to set Default Values ! Try Manual Adjustments \n\n(Make sure you give a valid date range and proper top and bottom skip row values including newline characters.)\n\nThen Try the Calculate button\n')

        self.radioButton.setEnabled(True)
        self.radioButton_2.setEnabled(True)
        self.radioButton_3.setEnabled(True)
        self.radioButton_4.setEnabled(True)
        self.dateEdit.setEnabled(True)
        self.dateEdit_2.setEnabled(True)
        self.spinBox.setEnabled(True)
        self.spinBox_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.checkBox.setEnabled(True)
        self.checkBox_2.setEnabled(True)
        self.checkBox_3.setEnabled(True)
        

    def clear(self):
        self.pushButton_2.setEnabled(False)
        self.radioButton.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.checkBox.setEnabled(False)
        self.checkBox_2.setEnabled(False)
        self.checkBox_3.setEnabled(False)
        self.checkBox_4.setEnabled(False)
        self.dateEdit.setEnabled(False)
        self.dateEdit_2.setEnabled(False)
        #self.spinBox.setEnabled(False)
        #self.spinBox_2.setEnabled(False)
        self.textBrowser.setText('')
        self.textBrowser_2.setText('')
        self.check_german()

    def calculate(self):
        skip_r = self.spinBox.value()
        skip_f = self.spinBox_2.value()
        try:
            data = pandas.read_csv(self.filename[0],sep = '\t',skiprows=skip_r,skipfooter=skip_f,engine='python',encoding='utf8')
            try:
                data['Debit'] = data['        Debit']
            except KeyError:
                self.textBrowser.append("Looks like Debit spacing already adjusted !\n")
            data['Credit'] = data['Credit'].apply(lambda x: self.to_float(x))
            data['Debit'] = data['Debit'].apply(lambda x: self.to_float(x))
            data.sort_values("Value Date",ascending = True, inplace = True) 
            data.reset_index(drop = True)
            try:
                data['Txn Date'] = data['Txn Date'].apply(lambda x: datetime.strptime(x, '%d %b %Y'))
                data['Value Date'] = data['Value Date'].apply(lambda x: datetime.strptime(x, '%d %b %Y'))
            except:
                data['Txn Date'] = data['Txn Date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
                data['Value Date'] = data['Value Date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
            start_date = str(self.dateEdit.date().toPyDate())
            end_date = str(self.dateEdit_2.date().toPyDate())
            data['year_month_date'] = data['Value Date'].dt.to_period("D")
            data['year_month'] = data['Value Date'].dt.to_period("M")
            data['year'] = data['Value Date'].dt.to_period("Y")
            data['week'] = data['Value Date'].dt.year.apply(str)+'_'+data['Value Date'].dt.week.apply(str)
            condition_1 = data['year_month_date']>=pandas.Period(start_date,'D')
            condition_2 = data['year_month_date']<=pandas.Period(end_date,'D')
            data = data[condition_1 & condition_2]
            if self.radioButton.isChecked():
                data_gb = data.groupby('year')
                self.choice = 'Y'
            elif self.radioButton_2.isChecked():
                data_gb = data.groupby('year_month')
                self.choice = 'M'
            elif self.radioButton_3.isChecked():
                data_gb = data.groupby('week')
                self.choice = 'W'
            else:
                data_gb = data.groupby('year_month_date')
                self.choice = 'D'
            credit,debit,saving,key_list = [],[],[],[]
            Total_C = 0
            Total_D = 0
            count = 0
            for key,df in data_gb:
                C = sum(df['Credit'].apply(lambda x: 0 if (x == ' ') else x).tolist())
                D = sum(df['Debit'].apply(lambda x: 0 if (x == ' ') else x).tolist())
                Total_C += C
                Total_D += D
                count += 1
                credit.append(C)
                debit.append(D)
                saving.append(C-D)
                key_list.append(key)
            summary = pandas.DataFrame({'key':key_list,'credit':credit,'debit':debit,'saving':saving})
            if self.choice == 'W':
                summary['key_year'] = summary['key']
                summary['key_week'] = summary['key']
                summary['key_year'] = summary['key_year'].apply(lambda x : int(x.split('_')[0]))
                summary.key_year = summary.key_year.astype(int)
                summary['key_week'] = summary['key_week'].apply(lambda x : int(x.split('_')[1]))
                summary.key_week = summary.key_week.astype(int)
                summary = summary.sort_values(['key_year','key_week'])
                summary = summary.drop(columns=['key_week', 'key_year'])
            else:
                summary = summary.sort_values('key',ascending = False)

            if self.choice == 'W':
                summary['key_'] = summary['key']
                what = 'week'
            elif self.choice == 'M':
                summary['key_'] = summary['key'].apply(lambda x : x.strftime("%Y-%b"))
                what = 'month'
            elif self.choice == 'Y':
                summary['key_'] = summary['key'].apply(lambda x : x.strftime("%Y"))
                what = 'year'
            elif self.choice == 'D':
                summary['key_'] = summary['key'].apply(lambda x : x.strftime("%Y-%b-%d"))
                what = 'day'
            self.summary = summary
            self.Max_C = data[data.Credit == data.Credit.max()]
            self.Max_D = data[data.Debit == data.Debit.max()]
            self.info = "Total Credit over the given Period : "+str(round(Total_C,3))+'\n'+"Total Debit over the given Period : "+str(round(Total_D,3))+'\n'+"Average Credit per "+what+" Over the given period : "+str(round((Total_C/count),3))+'\n'+"Average Debit per "+what+" Over the given period :"+str(round(Total_D/count,3))+'\n'+"Average Retention per "+what+" Over the given period : "+str(round((Total_C-Total_D)/count,3))+'\n'+"Standard Deviation of Credit : "+str(round(summary.credit.std(ddof=0),4))+'\n'+"Standard Deviation of Debit : "+str(round(summary.debit.std(ddof=0),4))+'\n'
            self.info += "Maximum Credit of "+str(self.Max_C['Credit'].to_list()[0])+" was caused on "+str(self.Max_C['Value Date'].to_list()[0])+" because "+str(self.Max_C['Description'].to_list()[0])+'\n'+"Maximum Debit of "+str(self.Max_D['Debit'].to_list()[0])+" was caused on "+str(self.Max_D['Value Date'].to_list()[0])
            self.info += " because "+str(self.Max_D['Description'].to_list()[0])+'\n'
            self.summary = summary
            self.pushButton_4.setEnabled(True)
            self.checkBox_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            self.textBrowser.append('Calculations Successfully Performed\n')

        except Exception as e:
            self.textBrowser.append("ERROR : "+str(e)+'\nYour data is not Supported for calculation !\n')

    def graph_plot(self):
        self.calculate()
        sort_out = ['key','key_']
        if self.checkBox.isChecked():
            sort_out.append('credit')
        if self.checkBox_2.isChecked():
            sort_out.append('debit')
        if self.checkBox_3.isChecked():
            sort_out.append('saving')
        if self.choice != 'W':
            ax = self.summary[sort_out].plot(kind = 'bar',x = 'key',title = 'Bank data Analyser by Arpan Ghosh',logy = False)
        else:
            ax = self.summary[sort_out].plot(kind = 'bar',title = 'Bank data Analyser by Arpan Ghosh',logy = False)
        ax.set_xticklabels(self.summary['key_'])
        if self.choice == 'W':
            ax.set_xlabel("Year_Week-number")
        elif self.choice == 'M':
            ax.set_xlabel("Year_Month-name")
        elif self.choice == 'Y':
            ax.set_xlabel("Year")
        elif self.choice == 'D':
            ax.set_xlabel("Date")
        ax.set_ylabel("Amount")
        if self.checkBox_4.isChecked():
            plt.grid()
        plt.show()
        self.textBrowser.append('Graph Displayed.\n')
        #self.pushButton_4.setEnabled(False)
        #self.checkBox_4.setEnabled(False)
    
    def show_summary_table(self):
        self.calculate()
        sort_out = ['key','key_']
        if self.checkBox.isChecked():
            sort_out.append('credit')
        if self.checkBox_2.isChecked():
            sort_out.append('debit')
        if self.checkBox_3.isChecked():
            sort_out.append('saving')
        self.data_ = self.summary[sort_out]
        self.data_window = Show_data()
        self.data_window.show()
        self.textBrowser.append('Summary Table Displayed.\n')
        #self.pushButton_5.setEnabled(False)
        return self.data_window

    def show_details(self):
        self.calculate()
        self.info_Dialog = QtWidgets.QDialog()
        self.info_window = Show_info()
        self.info_window.setupUi(self.info_Dialog)
        self.info_Dialog.show()
        return self.info_window

    def check_german(self):
        if self.checkBox_5.isChecked():
            #self.pushButton_6.setEnabled(True)
            self.spinBox.setValue(11)
            self.spinBox_2.setValue(1)
            self.spinBox_2.setEnabled(True)
            self.spinBox.setEnabled(True)
            self.textBrowser.append("Sparda Bank is checked : open button expects sparda bank satatement format.\n\nYou may need to adjust the skip row values before pressing 'Open' button otherwise auto-conversion may fail.\n")
        else:
            self.pushButton_6.setEnabled(False)
            self.spinBox.setValue(0)
            self.spinBox_2.setValue(0)
            #self.spinBox_2.setEnabled(False)
            #self.spinBox.setEnabled(False)
            self.textBrowser.append("Sparda Bank is Unchecked : open button expects SBI bank statement format\n")

    def convert_german(self):

        def fix_date(string):
            lst = string.split('.')
            return pandas.Timestamp(int(lst[2]),int(lst[1]),int(lst[0]))

        def amount_splitter(value,credit = True):
            value = value.replace('.','')
            value = value.replace(',','.')
            value = float(value)
            if credit:
                if value > 0:
                    return value
                else:
                    return 0.00
            else:
                if value > 0:
                    return 0.00
                else:
                    return -value

        
        try:
            filename_1 = QFileDialog.getOpenFileName(None, 'Open file', expanduser('~'),"CSV files (*.csv )")[0]
            if filename_1:
                self.data_ = pandas.read_csv(filename_1,sep=';',engine='python',names = ['Txn Date','Value Date','Description','amount','EUR','NONE'],skiprows = self.spinBox.value(),skipfooter = self.spinBox_2.value())
                del self.data_['NONE']
                del self.data_['EUR']
                self.data_['Txn Date'] = self.data_['Txn Date'].apply(lambda x : fix_date(x))
                self.data_['Value Date'] = self.data_['Value Date'].apply(lambda x : fix_date(x))
                self.data_['Credit'] = self.data_['amount'].apply(lambda x : amount_splitter(x,True))
                self.data_['Debit'] = self.data_['amount'].apply(lambda x : amount_splitter(x,False))
                del self.data_['amount']
                self.textBrowser.append('\nConversion Successful !\n')
                self.data_window = Show_data()
                self.data_window.show()
                return self.data_window
            else:
                self.textBrowser.append("No file chosen !\n")
        except Exception as e:
            self.textBrowser.append("ERROR : "+str(e)+'\nEither your file is not Supported for Convertion or skip row values are not correct (Default values are not being supported) !\n')

    def auto_convert(self):
        def fix_date(string):
            lst = string.split('.')
            return pandas.Timestamp(int(lst[2]),int(lst[1]),int(lst[0]))

        def amount_splitter(value,credit = True):
            value = value.replace('.','')
            value = value.replace(',','.')
            value = float(value)
            if credit:
                if value > 0:
                    return value
                else:
                    return 0.00
            else:
                if value > 0:
                    return 0.00
                else:
                    return -value

        
        try:
            filename_1 = self.filename[0]
            self.data_ = pandas.read_csv(filename_1,sep=';',engine='python',encoding='utf8',names = ['Txn Date','Value Date','Description','amount','EUR','NONE'],skiprows = self.spinBox.value(),skipfooter = self.spinBox_2.value())
            del self.data_['NONE']
            del self.data_['EUR']
            self.data_['Txn Date'] = self.data_['Txn Date'].apply(lambda x : fix_date(x))
            self.data_['Value Date'] = self.data_['Value Date'].apply(lambda x : fix_date(x))
            self.data_['Credit'] = self.data_['amount'].apply(lambda x : amount_splitter(x,True))
            self.data_['Debit'] = self.data_['amount'].apply(lambda x : amount_splitter(x,False))
            del self.data_['amount']
            self.textBrowser.append('Attempting to convert file autometically !\n')
            save_name = os.path.split(filename_1)[0]+'\\'+os.path.split(filename_1)[1].split('.')[0]+'_converted'+'.'+os.path.split(filename_1)[1].split('.')[1]
            if os.path.exists(save_name):
                self.textBrowser.append('\nUnable to save '+save_name+" : file already exists!\n\nAborting Auto conversion , please try convert button to convert and save .\n")
                self.textBrowser_2.setText('')
                self.filename = ['','']
            else:
                self.data_.to_csv(save_name,encoding='utf-8',index=False,sep='\t')
                self.textBrowser.append('File written as "'+save_name+' And Loading from that file\n')
                self.filename = [save_name,'']

        except Exception as e:
            self.textBrowser.append("Auto-conversion is not supporting ( Already converted or Unknown format ) \n\nPlease try manual conversion button, save and then open it IN CASE OF FURTHUS ERRORS ONLY\n")

        self.pushButton_6.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.pushButton_2.setEnabled(False)
    ui.radioButton.setEnabled(False)
    ui.radioButton_2.setEnabled(False)
    ui.radioButton_3.setEnabled(False)
    ui.radioButton_4.setEnabled(False)
    ui.pushButton_3.setEnabled(False)
    ui.pushButton_4.setEnabled(False)
    ui.pushButton_5.setEnabled(False)
    ui.pushButton_8.setEnabled(False)
    ui.checkBox.setEnabled(False)
    ui.checkBox_2.setEnabled(False)
    ui.checkBox_3.setEnabled(False)
    ui.dateEdit.setEnabled(False)
    ui.dateEdit_2.setEnabled(False)
    #ui.spinBox.setEnabled(False)
    #ui.spinBox_2.setEnabled(False)
    ui.checkBox_4.setEnabled(False)
    ui.pushButton_6.setEnabled(False)
    ui.checkBox_5.setChecked(GERMAN_VERSION)
    Dialog.show()
    sys.exit(app.exec_())