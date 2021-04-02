from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import configparser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

from Detection_1DCode.DlogRDS.Ui_DlogRDS.I_DlogReadData_1Dcode import Ui_Class_DlogReadData_1Dcode
from Detection_1DCode.ActionFile import ActionFile

var_dirFileOS = os.getcwd()
var_dirFileOS = var_dirFileOS.rstrip()
var_dirFileOS = var_dirFileOS.replace("/Detection_1DCode","")
var_dirFileConfig = var_dirFileOS + "/" + "config"


class Class_DlogReadData_1Dcode(QDialog):
    #var_signal_RD = pyqtSignal(str,str)

    def __init__(self, parent, *args):
        super(Class_DlogReadData_1Dcode, self).__init__(*args)
        self.var_Ui_RD_1Dcode = Ui_Class_DlogReadData_1Dcode()
        self.var_Ui_RD_1Dcode.setupUi(self)

        self.file = ActionFile(var_dirFileConfig)
        self.num = self.file.func_getNumToolConfig() + 1
        self.num = self.file.func_convert_1to4Digit(self.num)
        self.nameFileSetting = str(self.num) + ".ini"

        self.config = configparser.ConfigParser()
        self.config.read(var_dirFileConfig + "/"+ self.nameFileSetting)


        self.var_Ui_RD_1Dcode.btn_Ok_DlogReadData_1D.clicked.connect(self.func_createSignal_RD_1Dcode)


####################################################Func for DC####################################################
    #Show GUI of table setting DC_1D
    def func_show_RD_1Dcode(self):
        self.show()

    #Close GUI of table setting DC_1D
    def func_close_RD_1Dcode(self):      
        self.close()   

    #Close GUI of table setting DC_1D
    def func_closeAndSave_RD_1Dcode(self):
        self.func_createSignal_RD_1Dcode()
        self.func_saveDataSetting_RD()  
        self.close() 

    #Get data setup from table_setting for singal-emit
    def func_createSignal_RD_1Dcode(self):
        self.var_ValueStartDigit = self.var_Ui_RD_1Dcode.ledit_StartDigit_ReadData_1D.text()
        self.var_ValueLengReadData = self.var_Ui_RD_1Dcode.ledit_LengReadData_ReadData_1D.text()


        self.var_checkSplitData = self.var_Ui_RD_1Dcode.cbox_SplitData_ReadData_1D.checkState()
        self.var_checkOutFixLeng = self.var_Ui_RD_1Dcode.cbox_OutFixLeng_ReadData_1D.checkState()
        self.var_checkCallTextError = self.var_Ui_RD_1Dcode.cbox_CallTextError_ReadData_1D.checkState()      
        self.var_checkOutSymbleIdentifier = self.var_Ui_RD_1Dcode.cbox_OutSymbleIdentifier_ReadData_1D.checkState()      


        self.var_ValueFillingCharac = self.var_Ui_RD_1Dcode.ledit_FillingCharac_ReadData_1D.text()
        self.var_ValueCallTextError = self.var_Ui_RD_1Dcode.ledit_callTextError_ReadData_1D.text()

        #self.var_signal_RD.emit(self.var_ValueStartDigit, self.var_ValueLengReadData)


    #Save data for Setting of JC
    def func_saveDataSetting_RD(self):
        self.file.updateDataFile(self.nameFileSetting ,"RD", "var_ValueStartDigit", self.var_ValueStartDigit)
        self.file.updateDataFile(self.nameFileSetting ,"RD", "var_ValueLengReadData", self.var_ValueLengReadData)
        self.file.updateDataFile(self.nameFileSetting ,"RD", "var_checkSplitData", str(self.var_checkSplitData))
        self.file.updateDataFile(self.nameFileSetting ,"RD", "var_checkOutFixLeng", str(self.var_checkOutFixLeng))
        self.file.updateDataFile(self.nameFileSetting ,"RD", "var_checkCallTextError", str(self.var_checkCallTextError))
        self.file.updateDataFile(self.nameFileSetting ,"RD", "var_checkOutSymbleIdentifier", str(self.var_checkOutSymbleIdentifier))
        self.file.updateDataFile(self.nameFileSetting ,"RD", "var_ValueFillingCharac", self.var_ValueFillingCharac)
        self.file.updateDataFile(self.nameFileSetting ,"RD", "var_ValueCallTextError", self.var_ValueCallTextError)

    #Load data for Setup from file self.config of JC    
    def func_loadDataSetup_RD(self):
        self.config.read(var_dirFileConfig + "/"+ self.nameFileSetting)

        self.var_ValueStartDigit = self.config.get("RD", "var_ValueStartDigit")
        self.var_ValueLengReadData = self.config.get("RD", "var_ValueLengReadData")
        self.var_checkSplitData = self.config.get("RD", "var_checkSplitData")
        self.var_checkOutFixLeng = self.config.get("RD", "var_checkOutFixLeng")
        self.var_checkCallTextError = self.config.get("RD", "var_checkCallTextError")
        self.var_checkOutSymbleIdentifier = self.config.get("RD", "var_checkOutSymbleIdentifier")
        self.var_ValueFillingCharac = self.config.get("RD", "var_ValueFillingCharac")
        self.var_ValueCallTextError = self.config.get("RD", "var_ValueCallTextError")



    #Setting for JC of Data load from file self.config
    def func_insertDataSetup_Table_RD(self):
        self.var_Ui_RD_1Dcode.ledit_StartDigit_ReadData_1D.setText(self.var_ValueStartDigit)
        self.var_Ui_RD_1Dcode.ledit_LengReadData_ReadData_1D.setText(self.var_ValueLengReadData)
        self.var_Ui_RD_1Dcode.ledit_FillingCharac_ReadData_1D.setText(self.var_ValueFillingCharac)
        self.var_Ui_RD_1Dcode.ledit_callTextError_ReadData_1D.setText(self.var_ValueCallTextError)


        if self.var_checkSplitData == "False":
            self.var_Ui_RD_1Dcode.cbox_SplitData_ReadData_1D.setChecked(False)
        else:
            self.var_Ui_RD_1Dcode.cbox_SplitData_ReadData_1D.setChecked(True)

        if self.var_checkOutFixLeng == "False":
            self.var_Ui_RD_1Dcode.cbox_OutFixLeng_ReadData_1D.setChecked(False)
        else:
            self.var_Ui_RD_1Dcode.cbox_OutFixLeng_ReadData_1D.setChecked(True)

        if self.var_checkCallTextError == "False":
            self.var_Ui_RD_1Dcode.cbox_CallTextError_ReadData_1D.setChecked(False)
        else:
            self.var_Ui_RD_1Dcode.cbox_CallTextError_ReadData_1D.setChecked(True)

        if self.var_checkOutSymbleIdentifier == "False":
            self.var_Ui_RD_1Dcode.cbox_OutSymbleIdentifier_ReadData_1D.setChecked(False)
        else:
            self.var_Ui_RD_1Dcode.cbox_OutSymbleIdentifier_ReadData_1D.setChecked(True)