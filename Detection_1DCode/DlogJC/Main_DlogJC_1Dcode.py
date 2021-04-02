from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import configparser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from Detection_1DCode.DlogJC.Ui_DlogJC.I_DlogJC_1Dcode import Ui_Class_DlogJC_1Dcode

from Detection_1DCode.ActionFile import ActionFile


var_dirFileOS = os.getcwd()
var_dirFileOS = var_dirFileOS.rstrip()
var_dirFileOS = var_dirFileOS.replace("/Detection_1DCode","")
var_dirFileConfig = var_dirFileOS + "/" + "config"


class Class_DlogJC_1Dcode(QDialog):
    var_signal_JC = pyqtSignal(str)

    def __init__(self, parent, *args):
        super(Class_DlogJC_1Dcode, self).__init__(*args)
        self.var_Ui_JC_1Dcode = Ui_Class_DlogJC_1Dcode()
        self.var_Ui_JC_1Dcode.setupUi(self)

        self.file = ActionFile(var_dirFileConfig)
        self.num = self.file.func_getNumToolConfig() + 1
        self.num = self.file.func_convert_1to4Digit(self.num)
        self.nameFileSetting = str(self.num) + ".ini"

        self.config = configparser.ConfigParser()
        self.config.read(var_dirFileConfig + "/"+ self.nameFileSetting)


        self.var_Ui_JC_1Dcode.btn_Ok_JC_TableSetting.clicked.connect(self.func_createSignal_JC_1Dcode)

    #Get data setup from table_setting for singal-emit
    def func_createSignal_JC_1Dcode(self):

        self.var_rbtn_SingleOfConditi = self.var_Ui_JC_1Dcode.rbtn_SingleOfConditi_JC_TableSetting.isChecked()
        self.var_rbtn_MultiOfConditi = self.var_Ui_JC_1Dcode.rbtn_MultiOfConditi_JC_TableSetting.isChecked()
        #self.var_combox_DataRange = self.var_Ui_JC_1Dcode.combox_DataRange_JC_TableSetting.currentText()
        #self.var_lab_StartDigit = self.var_Ui_JC_1Dcode.lab_StartDigit_JC_TableSetting.text()
        #self.var_lab_RangeDigit = self.var_Ui_JC_1Dcode.lab_RangeDigit_JC_TableSetting.text()
        self.var_ledit_CopyFromReadData = self.var_Ui_JC_1Dcode.ledit_CopyFromReadData_JC_TableSetting.text()
        #self.var_lab_CollationResult = self.var_Ui_JC_1Dcode.lab_CollationResult_JC_TableSetting.text()
        self.var_ledit_UpperLimitLengData = self.var_Ui_JC_1Dcode.ledit_UpperLimitLengData_JC_TableSetting.text()
        self.var_ledit_LowerLimitLengData = self.var_Ui_JC_1Dcode.ledit_LowerLimitLengData_JC_TableSetting.text()
        self.var_ledit_UpperLimitPositX = self.var_Ui_JC_1Dcode.ledit_UpperLimitPositX_JC_TableSetting.text()
        self.var_ledit_UpperLimitPositY = self.var_Ui_JC_1Dcode.ledit_UpperLimitPositY_JC_TableSetting.text()
        self.var_ledit_LowerLimitPositX = self.var_Ui_JC_1Dcode.ledit_LowerLimitPositX_JC_TableSetting.text()
        self.var_ledit_LowerLimitPositY = self.var_Ui_JC_1Dcode.ledit_LowerLimitPositY_JC_TableSetting.text()
        self.var_ledit_UpperLimitDetecAngle = self.var_Ui_JC_1Dcode.ledit_UpperLimitDetecAngle_JC_TableSetting.text()
        self.var_ledit_LowerLimitDetecAngle = self.var_Ui_JC_1Dcode.ledit_LowerLimitDetecAngle_JC_TableSetting.text()


        self.var_signal_JC.emit(self.var_ledit_CopyFromReadData)


    #Show GUI of table setting DC_1D
    def func_show_JC_1Dcode(self):
        self.show()

    #Close GUI of table setting DC_1D
    def func_close_JC_1Dcode(self):      
        self.close()    

    #Close GUI of table setting DC_1D
    def func_closeAndSave_JC_1Dcode(self):
        self.func_createSignal_JC_1Dcode()
        self.func_saveDataSetting_JC()  
        self.close() 

    #Save data for Setting of JC
    def func_saveDataSetting_JC(self):
        self.file.updateDataFile(self.nameFileSetting,"JC", "SingleOfConditi", str(self.var_rbtn_SingleOfConditi))
        self.file.updateDataFile(self.nameFileSetting,"JC", "MultiOfConditi", str(self.var_rbtn_MultiOfConditi))
        #self.file.updateDataFile("0005.ini","JC", "DataRange", self.var_combox_DataRange)
        #self.file.updateDataFile("0005.ini","JC", "StartDigit", self.var_lab_StartDigit)
        #self.file.updateDataFile("0005.ini","JC", "RangeDigit", str(self.var_lab_RangeDigit))
        self.file.updateDataFile(self.nameFileSetting,"JC", "CopyFromReadData", self.var_ledit_CopyFromReadData)
        #self.file.updateDataFile("0005.ini","JC", "CollationResult", str(self.var_lab_CollationResult))
        self.file.updateDataFile(self.nameFileSetting,"JC", "UpperLimitLengData", self.var_ledit_UpperLimitLengData)
        self.file.updateDataFile(self.nameFileSetting,"JC", "LowerLimitLengData", self.var_ledit_LowerLimitLengData)
        self.file.updateDataFile(self.nameFileSetting,"JC", "UpperLimitPositX", self.var_ledit_UpperLimitPositX)
        self.file.updateDataFile(self.nameFileSetting,"JC", "UpperLimitPositY", self.var_ledit_UpperLimitPositY)
        self.file.updateDataFile(self.nameFileSetting,"JC", "LowerLimitPositX", self.var_ledit_LowerLimitPositX)
        self.file.updateDataFile(self.nameFileSetting,"JC", "LowerLimitPositY", self.var_ledit_LowerLimitPositY)
        self.file.updateDataFile(self.nameFileSetting,"JC", "UpperLimitDetecAngle", self.var_ledit_UpperLimitDetecAngle)
        self.file.updateDataFile(self.nameFileSetting,"JC", "LowerLimitDetecAngle", self.var_ledit_LowerLimitDetecAngle)


    #Load data for Setup from file self.config of JC    
    def func_loadDataSetup_JC(self):
        self.config.read(var_dirFileConfig + "/"+ self.nameFileSetting)

        self.var_rbtn_SingleOfConditi = self.config.get("JC", "SingleOfConditi")
        self.var_rbtn_MultiOfConditi = self.config.get("JC", "MultiOfConditi")
        #self.var_combox_DataRange = self.config.get("JC", "DataRange")
        #self.var_lab_StartDigit = self.config.get("JC", "StartDigit")
        #self.var_lab_RangeDigit = self.config.get("JC", "RangeDigit")
        self.var_ledit_CopyFromReadData = self.config.get("JC", "CopyFromReadData")
        #self.var_lab_CollationResult = self.config.get("JC", "CollationResult")
        self.var_ledit_UpperLimitLengData = self.config.get("JC", "UpperLimitLengData")
        self.var_ledit_LowerLimitLengData = self.config.get("JC", "LowerLimitLengData")
        self.var_ledit_UpperLimitPositX = self.config.get("JC", "UpperLimitPositX")
        self.var_ledit_UpperLimitPositY = self.config.get("JC", "UpperLimitPositY")
        self.var_ledit_LowerLimitPositX = self.config.get("JC", "LowerLimitPositX")
        self.var_ledit_LowerLimitPositY = self.config.get("JC", "LowerLimitPositY")
        self.var_ledit_UpperLimitDetecAngle = self.config.get("JC", "UpperLimitDetecAngle")
        self.var_ledit_LowerLimitDetecAngle = self.config.get("JC", "LowerLimitDetecAngle")


    #Setting for JC of Data load from file self.config
    def func_insertDataSetup_Table_JC(self):
        self.var_Ui_JC_1Dcode.ledit_CopyFromReadData_JC_TableSetting.setText(self.var_ledit_CopyFromReadData)
        self.var_Ui_JC_1Dcode.ledit_UpperLimitLengData_JC_TableSetting.setText(self.var_ledit_UpperLimitLengData)
        self.var_Ui_JC_1Dcode.ledit_LowerLimitLengData_JC_TableSetting.setText(self.var_ledit_LowerLimitLengData)
        self.var_Ui_JC_1Dcode.ledit_UpperLimitPositX_JC_TableSetting.setText(self.var_ledit_UpperLimitPositX)
        self.var_Ui_JC_1Dcode.ledit_UpperLimitPositY_JC_TableSetting.setText(self.var_ledit_UpperLimitPositY)
        self.var_Ui_JC_1Dcode.ledit_LowerLimitPositX_JC_TableSetting.setText(self.var_ledit_LowerLimitPositX)
        self.var_Ui_JC_1Dcode.ledit_LowerLimitPositY_JC_TableSetting.setText(self.var_ledit_LowerLimitPositY)
        self.var_Ui_JC_1Dcode.ledit_UpperLimitDetecAngle_JC_TableSetting.setText(self.var_ledit_UpperLimitDetecAngle)
        self.var_Ui_JC_1Dcode.ledit_LowerLimitDetecAngle_JC_TableSetting.setText(self.var_ledit_LowerLimitDetecAngle)

        if self.var_rbtn_SingleOfConditi == "False":
            self.var_Ui_JC_1Dcode.rbtn_SingleOfConditi_JC_TableSetting.setChecked(False)
        else:
            self.var_Ui_JC_1Dcode.rbtn_SingleOfConditi_JC_TableSetting.setChecked(True)

        if self.var_rbtn_MultiOfConditi == "False":
            self.var_Ui_JC_1Dcode.rbtn_MultiOfConditi_JC_TableSetting.setChecked(False)
        else:
            self.var_Ui_JC_1Dcode.rbtn_MultiOfConditi_JC_TableSetting.setChecked(True)


