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
                ui.data_.to_csv(fileName,index=False,sep='\t',encoding="ISO-8859-1")
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
            self.Open_Button = QtWidgets.QPushButton(Dialog)
            self.Open_Button.setObjectName("Open_Button")
            self.verticalLayout_2.addWidget(self.Open_Button)
            self.Open_Button.clicked.connect(self.save_info)

            self.retranslateUi(Dialog)
            QtCore.QMetaObject.connectSlotsByName(Dialog) 

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Open_Button.setText(_translate("Dialog", "Save"))

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
        self.Open_Button = QtWidgets.QPushButton(Dialog)
        self.Open_Button.setGeometry(QtCore.QRect(690, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Open_Button.setFont(font)
        self.Open_Button.setObjectName("Open_Button")
        self.Default_Button = QtWidgets.QPushButton(Dialog)
        self.Default_Button.setGeometry(QtCore.QRect(820, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Default_Button.setFont(font)
        self.Default_Button.setObjectName("Default_Button")
        self.Copyright_label = QtWidgets.QLabel(Dialog)
        self.Copyright_label.setGeometry(QtCore.QRect(880, 560, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Copyright_label.setFont(font)
        self.Copyright_label.setObjectName("Copyright_label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(20, 130, 1041, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.DateSelection_GroupBox = QtWidgets.QGroupBox(Dialog)
        self.DateSelection_GroupBox.setGeometry(QtCore.QRect(20, 150, 391, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DateSelection_GroupBox.setFont(font)
        self.DateSelection_GroupBox.setObjectName("DateSelection_GroupBox")
        self.dateEdit = QtWidgets.QDateEdit(self.DateSelection_GroupBox)
        self.dateEdit.setGeometry(QtCore.QRect(210, 40, 131, 31))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.DateSelection_GroupBox)
        self.dateEdit_2.setGeometry(QtCore.QRect(210, 100, 131, 31))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_3 = QtWidgets.QLabel(self.DateSelection_GroupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 40, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.DateSelection_GroupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 100, 81, 21))
        self.label_4.setObjectName("label_4")
        self.GroupBy_GroupBox = QtWidgets.QGroupBox(Dialog)
        self.GroupBy_GroupBox.setGeometry(QtCore.QRect(440, 150, 211, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GroupBy_GroupBox.setFont(font)
        self.GroupBy_GroupBox.setObjectName("GroupBy_GroupBox")
        self.year_radioButton = QtWidgets.QRadioButton(self.GroupBy_GroupBox)
        self.year_radioButton.setGeometry(QtCore.QRect(70, 40, 121, 21))
        self.year_radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.year_radioButton.setObjectName("radioButton")
        self.month_radioButton = QtWidgets.QRadioButton(self.GroupBy_GroupBox)
        self.month_radioButton.setGeometry(QtCore.QRect(70, 90, 121, 21))
        self.month_radioButton.setChecked(True)
        self.month_radioButton.setObjectName("month_radioButton")
        self.week_radioButton = QtWidgets.QRadioButton(self.GroupBy_GroupBox)
        self.week_radioButton.setGeometry(QtCore.QRect(70, 140, 121, 21))
        self.week_radioButton.setObjectName("week_radioButton")
        self.day_radioButton = QtWidgets.QRadioButton(self.GroupBy_GroupBox)
        self.day_radioButton.setGeometry(QtCore.QRect(70, 190, 121, 21))
        self.day_radioButton.setObjectName("day_radioButton")
        self.DataSelection_GroupBox = QtWidgets.QGroupBox(Dialog)
        self.DataSelection_GroupBox.setGeometry(QtCore.QRect(740, 160, 221, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DataSelection_GroupBox.setFont(font)
        self.DataSelection_GroupBox.setObjectName("DataSelection_GroupBox")
        self.label_5 = QtWidgets.QLabel(self.DataSelection_GroupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.DataSelection_GroupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 141, 21))
        self.label_6.setObjectName("label_6")
        self.spinBox = QtWidgets.QSpinBox(self.DataSelection_GroupBox)
        self.spinBox.setGeometry(QtCore.QRect(170, 40, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.DataSelection_GroupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(170, 90, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(170, 340, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.Calculate_Button = QtWidgets.QPushButton(Dialog)
        self.Calculate_Button.setGeometry(QtCore.QRect(480, 460, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Calculate_Button.setFont(font)
        self.Calculate_Button.setObjectName("Calculate_Button")
        self.Graph_Button = QtWidgets.QPushButton(Dialog)
        self.Graph_Button.setGeometry(QtCore.QRect(710, 510, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Graph_Button.setFont(font)
        self.Graph_Button.setObjectName("Graph_Button")
        self.summary_Button = QtWidgets.QPushButton(Dialog)
        self.summary_Button.setGeometry(QtCore.QRect(710, 330, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.summary_Button.setFont(font)
        self.summary_Button.setObjectName("summary_Button")
        self.details_Button = QtWidgets.QPushButton(Dialog)
        self.details_Button.setGeometry(QtCore.QRect(710, 420, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.details_Button.setFont(font)
        self.details_Button.setObjectName("details_Button")
        self.clear_Button = QtWidgets.QPushButton(Dialog)
        self.clear_Button.setGeometry(QtCore.QRect(950, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clear_Button.setFont(font)
        self.clear_Button.setObjectName("clear_Button")
        self.credit_Checkbox = QtWidgets.QCheckBox(Dialog)
        self.credit_Checkbox.setGeometry(QtCore.QRect(920, 400, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.credit_Checkbox.setFont(font)
        self.credit_Checkbox.setChecked(True)
        self.credit_Checkbox.setObjectName("checkBox")
        self.debit_Checkbox = QtWidgets.QCheckBox(Dialog)
        self.debit_Checkbox.setGeometry(QtCore.QRect(920, 450, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.debit_Checkbox.setFont(font)
        self.debit_Checkbox.setChecked(True)
        self.debit_Checkbox.setObjectName("debit_Checkbox")
        self.savings_Checkbox = QtWidgets.QCheckBox(Dialog)
        self.savings_Checkbox.setGeometry(QtCore.QRect(920, 500, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.savings_Checkbox.setFont(font)
        self.savings_Checkbox.setObjectName("savings_Checkbox")
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
        self.grid_Checkbox = QtWidgets.QCheckBox(Dialog)
        self.grid_Checkbox.setGeometry(QtCore.QRect(920, 350, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grid_Checkbox.setFont(font)
        self.grid_Checkbox.setChecked(True)
        self.grid_Checkbox.setObjectName("grid_Checkbox")
        self.other_bank_Checkbox = QtWidgets.QCheckBox(Dialog)
        self.other_bank_Checkbox.setGeometry(QtCore.QRect(690, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.other_bank_Checkbox.setFont(font)
        self.other_bank_Checkbox.setObjectName("other_bank_Checkbox")
        self.convert_Button = QtWidgets.QPushButton(Dialog)
        self.convert_Button.setGeometry(QtCore.QRect(820, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.convert_Button.setFont(font)
        self.convert_Button.setObjectName("convert_Button")
        self.Open_Button.clicked.connect(self.get_file_name)
        self.Default_Button.clicked.connect(self.find_default)
        self.Calculate_Button.clicked.connect(self.calculate)
        self.Graph_Button.clicked.connect(self.graph_plot)
        self.summary_Button.clicked.connect(self.show_summary_table)
        self.details_Button.clicked.connect(self.show_details)
        self.clear_Button.clicked.connect(self.clear)
        self.convert_Button.clicked.connect(self.convert_german)
        self.other_bank_Checkbox.stateChanged.connect(self.check_german)
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
        self.Open_Button.setText(_translate("Dialog", "Open"))
        self.Default_Button.setText(_translate("Dialog", "Default"))
        self.Copyright_label.setText(_translate("Dialog", "Developed by Arpan Ghosh"))
        self.DateSelection_GroupBox.setTitle(_translate("Dialog", "Date Selection"))
        self.label_3.setText(_translate("Dialog", "Start Date"))
        self.label_4.setText(_translate("Dialog", "End Date"))
        self.GroupBy_GroupBox.setTitle(_translate("Dialog", " Group By"))
        self.year_radioButton.setText(_translate("Dialog", "Year"))
        self.month_radioButton.setText(_translate("Dialog", "Month"))
        self.week_radioButton.setText(_translate("Dialog", "Week"))
        self.day_radioButton.setText(_translate("Dialog", "Day"))
        self.DataSelection_GroupBox.setTitle(_translate("Dialog", "Data Selection"))
        self.label_5.setText(_translate("Dialog", "Skip Top Rows"))
        self.label_6.setText(_translate("Dialog", "Skip Bottom Rows"))
        self.label_7.setText(_translate("Dialog", "Log Record"))
        self.Calculate_Button.setText(_translate("Dialog", "Calculate"))
        self.Graph_Button.setText(_translate("Dialog", "Graph"))
        self.summary_Button.setText(_translate("Dialog", "Summary"))
        self.details_Button.setText(_translate("Dialog", "Details"))
        self.clear_Button.setText(_translate("Dialog", "Clear"))
        self.credit_Checkbox.setText(_translate("Dialog", " Credit"))
        self.debit_Checkbox.setText(_translate("Dialog", "Debit"))
        self.savings_Checkbox.setText(_translate("Dialog", "Savings"))
        self.grid_Checkbox.setText(_translate("Dialog", "Grid"))
        self.other_bank_Checkbox.setText(_translate("Dialog", " Sparda Bank"))
        self.convert_Button.setText(_translate("Dialog", "Convert"))

    def get_file_name(self):
        self.clear()
        self.filename = QFileDialog.getOpenFileName(None, 'Open file', expanduser('~'),"Excel files (*.xls , *.csv)")
        self.textBrowser_2.setText(self.filename[0])
        if self.filename[0]:
            self.textBrowser.append("successfully Located File : "+self.filename[0]+'\n')
            self.Default_Button.setEnabled(True)
            if self.other_bank_Checkbox.isChecked():
                f_handle = open(self.filename[0],'r')
                raw_data = f_handle.read()
                if raw_data.startswith('Txn Date	Value Date	Description	Credit	Debit') == False:
                    self.auto_convert()
                else:
                    self.textBrowser.append("Converted file Identified !\n")
        if self.filename[0]:
            if self.other_bank_Checkbox.isChecked():
                if raw_data.startswith('Txn Date	Value Date	Description	Credit	Debit'):
                    self.textBrowser_2.setText(self.filename[0])
                else:
                    self.textBrowser_2.setText(" [CONVERTED] "+self.filename[0])
            self.find_default()
        else:
            self.textBrowser.append("No File Chosen !\n")
            self.Default_Button.setEnabled(False)
            self.year_radioButton.setEnabled(False)
            self.month_radioButton.setEnabled(False)
            self.week_radioButton.setEnabled(False)
            self.day_radioButton.setEnabled(False)
            self.Calculate_Button.setEnabled(False)
            self.Graph_Button.setEnabled(False)
            self.summary_Button.setEnabled(False)
            self.details_Button.setEnabled(False)
            self.credit_Checkbox.setEnabled(False)
            self.debit_Checkbox.setEnabled(False)
            self.savings_Checkbox.setEnabled(False)
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

            data = pandas.read_csv(file_path,sep = '\t',skiprows=skip_r,skipfooter=skip_f,engine='python',encoding="ISO-8859-1")
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
            self.month_radioButton.setChecked(True)
            self.spinBox.setValue(skip_r)
            self.spinBox_2.setValue(skip_f)
            self.textBrowser.append('Default Values are now set \n')
            
        except Exception as e:
            self.textBrowser.append("ERROR : "+str(e)+'\n')
            self.textBrowser.append('Warning : Default File format is not matching [may need conversion to proper format] !\n\nUnable to set Default Values ! Try Manual Adjustments \n\n(Make sure you give a valid date range and proper top and bottom skip row values including newline characters.)\n\nThen Try the Calculate button\n')

        self.year_radioButton.setEnabled(True)
        self.month_radioButton.setEnabled(True)
        self.week_radioButton.setEnabled(True)
        self.day_radioButton.setEnabled(True)
        self.dateEdit.setEnabled(True)
        self.dateEdit_2.setEnabled(True)
        self.spinBox.setEnabled(True)
        self.spinBox_2.setEnabled(True)
        self.Calculate_Button.setEnabled(True)
        self.credit_Checkbox.setEnabled(True)
        self.debit_Checkbox.setEnabled(True)
        self.savings_Checkbox.setEnabled(True)
        

    def clear(self):
        self.Default_Button.setEnabled(False)
        self.year_radioButton.setEnabled(False)
        self.month_radioButton.setEnabled(False)
        self.week_radioButton.setEnabled(False)
        self.day_radioButton.setEnabled(False)
        self.Calculate_Button.setEnabled(False)
        self.Graph_Button.setEnabled(False)
        self.summary_Button.setEnabled(False)
        self.details_Button.setEnabled(False)
        self.credit_Checkbox.setEnabled(False)
        self.debit_Checkbox.setEnabled(False)
        self.savings_Checkbox.setEnabled(False)
        self.grid_Checkbox.setEnabled(False)
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
            data = pandas.read_csv(self.filename[0],sep = '\t',skiprows=skip_r,skipfooter=skip_f,engine='python',encoding="ISO-8859-1")
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
            if self.year_radioButton.isChecked():
                data_gb = data.groupby('year')
                self.choice = 'Y'
            elif self.month_radioButton.isChecked():
                data_gb = data.groupby('year_month')
                self.choice = 'M'
            elif self.week_radioButton.isChecked():
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
            self.Graph_Button.setEnabled(True)
            self.grid_Checkbox.setEnabled(True)
            self.summary_Button.setEnabled(True)
            self.details_Button.setEnabled(True)
            self.textBrowser.append('Calculations Successfully Performed\n')

        except Exception as e:
            self.textBrowser.append("ERROR : "+str(e)+'\nYour data is not Supported for calculation !\n')

    def graph_plot(self):
        self.calculate()
        sort_out = ['key','key_']
        if self.credit_Checkbox.isChecked():
            sort_out.append('credit')
        if self.debit_Checkbox.isChecked():
            sort_out.append('debit')
        if self.savings_Checkbox.isChecked():
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
        if self.grid_Checkbox.isChecked():
            plt.grid()
        plt.show()
        self.textBrowser.append('Graph Displayed.\n')
        #self.Graph_Button.setEnabled(False)
        #self.grid_Checkbox.setEnabled(False)
    
    def show_summary_table(self):
        self.calculate()
        sort_out = ['key','key_']
        if self.credit_Checkbox.isChecked():
            sort_out.append('credit')
        if self.debit_Checkbox.isChecked():
            sort_out.append('debit')
        if self.savings_Checkbox.isChecked():
            sort_out.append('saving')
        self.data_ = self.summary[sort_out]
        self.data_window = Show_data()
        self.data_window.show()
        self.textBrowser.append('Summary Table Displayed.\n')
        #self.summary_Button.setEnabled(False)
        return self.data_window

    def show_details(self):
        self.calculate()
        self.info_Dialog = QtWidgets.QDialog()
        self.info_window = Show_info()
        self.info_window.setupUi(self.info_Dialog)
        self.info_Dialog.show()
        return self.info_window

    def check_german(self):
        if self.other_bank_Checkbox.isChecked():
            #self.convert_Button.setEnabled(True)
            self.spinBox.setValue(11)
            self.spinBox_2.setValue(1)
            self.spinBox_2.setEnabled(True)
            self.spinBox.setEnabled(True)
            self.textBrowser.append("Sparda Bank is checked : open button expects sparda bank satatement format.\n\nYou may need to adjust the skip row values before pressing 'Open' button otherwise auto-conversion may fail.\n")
        else:
            self.convert_Button.setEnabled(False)
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
            self.data_ = pandas.read_csv(filename_1,sep=';',engine='python',encoding="ISO-8859-1",names = ['Txn Date','Value Date','Description','amount','EUR','NONE'],skiprows = self.spinBox.value(),skipfooter = self.spinBox_2.value())
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
                self.textBrowser.append('Unable to save '+save_name+" : FILE ALREADY EXISTS !\n\nAborting Auto conversion , please try convert button to convert and save manually then open that file usinf 'open' button.\n")
                self.textBrowser_2.setText('')
                self.filename = ['','']
            else:
                self.data_.to_csv(save_name,encoding="ISO-8859-1",index=False,sep='\t')
                self.textBrowser.append('File written as "'+save_name+' And Loading from that file\n')
                self.filename = [save_name,'']

        except Exception as e:
            self.textBrowser.append("ERROR : "+str(e)+"\nAuto-conversion is not supporting ( Already converted or Unknown format ) \n\nPlease try manual conversion button, save and then open it IN CASE OF FURTHUS ERRORS ONLY\n")
            #raise e
        self.convert_Button.setEnabled(True)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.Default_Button.setEnabled(False)
    ui.year_radioButton.setEnabled(False)
    ui.month_radioButton.setEnabled(False)
    ui.week_radioButton.setEnabled(False)
    ui.day_radioButton.setEnabled(False)
    ui.Calculate_Button.setEnabled(False)
    ui.Graph_Button.setEnabled(False)
    ui.summary_Button.setEnabled(False)
    ui.details_Button.setEnabled(False)
    ui.credit_Checkbox.setEnabled(False)
    ui.debit_Checkbox.setEnabled(False)
    ui.savings_Checkbox.setEnabled(False)
    ui.dateEdit.setEnabled(False)
    ui.dateEdit_2.setEnabled(False)
    #ui.spinBox.setEnabled(False)
    #ui.spinBox_2.setEnabled(False)
    ui.grid_Checkbox.setEnabled(False)
    ui.convert_Button.setEnabled(False)
    ui.other_bank_Checkbox.setChecked(GERMAN_VERSION)
    Dialog.show()
    sys.exit(app.exec_())