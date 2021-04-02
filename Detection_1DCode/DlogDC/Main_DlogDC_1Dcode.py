from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import configparser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from Detection_1DCode.DlogDC.Ui_DlogDC.I_DlogDC_1Dcode import Ui_Class_DlogDC_1Dcode

from Detection_1DCode.ActionFile import ActionFile


var_dirFileOS = os.getcwd()
var_dirFileOS = var_dirFileOS.rstrip()
var_dirFileOS = var_dirFileOS.replace("/Detection_1DCode","")
var_dirFileConfig = var_dirFileOS + "/" + "config"

class Class_DlogDC_1Dcode(QDialog):
    var_signal_DC = pyqtSignal(str,str)

    def __init__(self, parent, *args):
        super(Class_DlogDC_1Dcode, self).__init__(*args)
        self.var_Ui_DC_1Dcode=Ui_Class_DlogDC_1Dcode()
        self.var_Ui_DC_1Dcode.setupUi(self)

        self.file = ActionFile(var_dirFileConfig)
        self.num = self.file.func_getNumToolConfig() + 1
        self.num = self.file.func_convert_1to4Digit(self.num)
        self.nameFileSetting = str(self.num) + ".ini"
        self.config = configparser.ConfigParser()
        self.config.read(var_dirFileConfig + "/"+ self.nameFileSetting)


        self.var_Ui_DC_1Dcode.btn_Ok_DC_TableSetting.clicked.connect(self.func_createSignal_DC_1Dcode)

    #Get data setup from table_setting for singal-emit
    def func_createSignal_DC_1Dcode(self):
        self.var_CodeType = self.var_Ui_DC_1Dcode.combox_CodeType_DC_TableSetting.currentText()
        self.var_ReferecContrast = self.var_Ui_DC_1Dcode.combox_ReferenceConstrast_DC_TableSetting.currentText()
        self.var_CodeColor = self.var_Ui_DC_1Dcode.combox_CodeColor_DC_TableSetting.currentText()
        self.var_ScaleVariation = self.var_Ui_DC_1Dcode.combox_ScaleVariation_DC_TableSetting.currentText()

        self.var_checkCodeResulation = self.var_Ui_DC_1Dcode.cbox_CodeResulation_DC_TableSetting.checkState()
        self.var_checkReferenContrast = self.var_Ui_DC_1Dcode.cbox_ReferenceConstrast_DC_TableSetting.checkState()
        self.var_checkNumberReadDigit = self.var_Ui_DC_1Dcode.cbox_NumberOfReadDigit_DC_TableSetting.checkState()      
        self.var_checkCodeColor = self.var_Ui_DC_1Dcode.cbox_CodeColor_DC_TableSetting.checkState()
        self.var_checkBaseAngle = self.var_Ui_DC_1Dcode.cbox_BaseAngle_DC_TableSetting.checkState()
        self.var_checkEnableCheckDigit = self.var_Ui_DC_1Dcode.cbox_EnableCheckDigit_DC_TableSetting.checkState()

        self.var_ValueCodeResulation = self.var_Ui_DC_1Dcode.ledit_CodeResulation_DC_TableSetting.text()
        self.var_ValueMinNumberReadDigit = self.var_Ui_DC_1Dcode.ledit_MinNumberReadDigit_DC_TableSetting.text()
        self.var_ValueMaxNumberReadDigit = self.var_Ui_DC_1Dcode.ledit_MaxNumberReadDigit_DC_TableSetting.text()
        self.var_ValueBaseAngle = self.var_Ui_DC_1Dcode.ledit_BaseAngle_DC_TableSetting.text()
        self.var_ValueTimeOut = self.var_Ui_DC_1Dcode.ledit_TimeOut_DC_TableSetting.text()
        
        self.var_signal_DC.emit(self.var_CodeType, self.var_ValueCodeResulation)


####################################################Func for DC####################################################
    #Show GUI of table setting DC_1D
    def func_show_DC_1Dcode(self):
        self.show()

    #Close GUI of table setting DC_1D
    def func_close_DC_1Dcode(self):      
        self.close()    

    #Close GUI of table setting DC_1D
    def func_closeAndSave_DC_1Dcode(self):
        self.func_createSignal_DC_1Dcode()
        self.func_saveDataSetting_DC()  
        self.close() 

    #Save data for Setting of DC
    def func_saveDataSetting_DC(self):
        # self.file.updateDataFile(self.nameFileSetting,"DC","CodeType", self.var_CodeType)
        # self.file.updateDataFile(self.nameFileSetting,"DC", "ReferecContrast", self.var_ReferecContrast)
        # self.file.updateDataFile(self.nameFileSetting,"DC", "CodeColor", self.var_CodeColor)
        # self.file.updateDataFile(self.nameFileSetting,"DC", "ScaleVariation", self.var_ScaleVariation)

        # self.file.updateDataFile(self.nameFileSetting,"DC", "checkCodeResulation", str(self.var_checkCodeResulation))
        # self.file.updateDataFile(self.nameFileSetting,"DC", "checkReferenContrast", str(self.var_checkReferenContrast))
        # self.file.updateDataFile(self.nameFileSetting,"DC", "checkNumberReadDigit", str(self.var_checkNumberReadDigit))
        # self.file.updateDataFile(self.nameFileSetting,"DC", "checkCodeColor", str(self.var_checkCodeColor))
        # self.file.updateDataFile(self.nameFileSetting,"DC", "checkBaseAngle", str(self.var_checkBaseAngle))
        # self.file.updateDataFile(self.nameFileSetting,"DC", "checkEnableCheckDigit", str(self.var_checkEnableCheckDigit))

        # self.file.updateDataFile(self.nameFileSetting,"DC", "ValueCodeResulation", self.var_ValueCodeResulation)
        # self.file.updateDataFile(self.nameFileSetting,"DC", "ValueMinNumberReadDigit", self.var_ValueMinNumberReadDigit)
        # self.file.updateDataFile(self.nameFileSetting,"DC", "ValueMaxNumberReadDigit", self.var_ValueMaxNumberReadDigit)
        # self.file.updateDataFile(self.nameFileSetting,"DC", "ValueBaseAngle", self.var_ValueBaseAngle)
        # self.file.updateDataFile(self.nameFileSetting,"DC", "ValueTimeOut", self.var_ValueTimeOut)


        self.config.set("DC", "CodeType", self.var_CodeType)
        self.config.set("DC", "ReferecContrast", self.var_ReferecContrast)
        self.config.set("DC", "CodeColor", self.var_CodeColor)
        self.config.set("DC", "ScaleVariation", self.var_ScaleVariation)
        self.config.set("DC", "checkCodeResulation", str(self.var_checkCodeResulation))
        self.config.set("DC", "checkReferenContrast", str(self.var_checkReferenContrast))
        self.config.set("DC", "checkNumberReadDigit",  str(self.var_checkNumberReadDigit))
        self.config.set("DC", "checkCodeColor", str(self.var_checkCodeColor))
        self.config.set("DC", "checkBaseAngle", str(self.var_checkBaseAngle))
        self.config.set("DC", "checkEnableCheckDigit", str(self.var_checkEnableCheckDigit))
        self.config.set("DC", "ValueCodeResulation", self.var_ValueCodeResulation)
        self.config.set("DC", "ValueMinNumberReadDigit", self.var_ValueMinNumberReadDigit)
        self.config.set("DC", "ValueMaxNumberReadDigit", self.var_ValueMaxNumberReadDigit)
        self.config.set("DC", "ValueBaseAngle", self.var_ValueBaseAngle)
        self.config.set("DC", "ValueTimeOut", self.var_ValueTimeOut)
        print(self.nameFileSetting)
        self.config.write(open(str(var_dirFileConfig) + "/"+ str(self.nameFileSetting), "w"))

    #Load data for Setup from file self.config of DC    
    def func_loadDataSetup_DC(self):
        self.config.read(var_dirFileConfig + "/"+ self.nameFileSetting)
        print(self.nameFileSetting)

        self.var_CodeType = self.config.get("DC", "CodeType")
        self.var_ReferecContrast = self.config.get("DC", "ReferecContrast")
        self.var_CodeColor = self.config.get("DC", "CodeColor")
        self.var_ScaleVariation = self.config.get("DC", "ScaleVariation")

        self.var_checkCodeResulation = self.config.get("DC", "checkCodeResulation")
        self.var_checkReferenContrast = self.config.get("DC", "checkReferenContrast")
        self.var_checkNumberReadDigit = self.config.get("DC", "checkNumberReadDigit")
        self.var_checkCodeColor = self.config.get("DC", "checkCodeColor")
        self.var_checkBaseAngle = self.config.get("DC", "checkBaseAngle")
        self.var_checkEnableCheckDigit = self.config.get("DC", "checkEnableCheckDigit")

        self.var_ValueCodeResulation = self.config.get("DC", "ValueCodeResulation")
        self.var_ValueMinNumberReadDigit = self.config.get("DC", "ValueMinNumberReadDigit")
        self.var_ValueMaxNumberReadDigit = self.config.get("DC", "ValueMaxNumberReadDigit")
        self.var_ValueBaseAngle = self.config.get("DC", "ValueBaseAngle")
        self.var_ValueTimeOut = self.config.get("DC", "ValueTimeOut")

    #Setting for DC of Data load from file self.config
    def func_insertDataSetup_Table_DC(self):
        self.var_Ui_DC_1Dcode.combox_CodeType_DC_TableSetting.setCurrentText(self.var_CodeType)
        self.var_Ui_DC_1Dcode.combox_ReferenceConstrast_DC_TableSetting.setCurrentText(self.var_ReferecContrast)
        self.var_Ui_DC_1Dcode.combox_CodeColor_DC_TableSetting.setCurrentText(self.var_CodeColor)
        self.var_Ui_DC_1Dcode.combox_ScaleVariation_DC_TableSetting.setCurrentText(self.var_ScaleVariation)

        self.var_Ui_DC_1Dcode.ledit_CodeResulation_DC_TableSetting.setText(self.var_ValueCodeResulation)
        self.var_Ui_DC_1Dcode.ledit_MinNumberReadDigit_DC_TableSetting.setText(self.var_ValueMinNumberReadDigit)
        self.var_Ui_DC_1Dcode.ledit_MaxNumberReadDigit_DC_TableSetting.setText(self.var_ValueMaxNumberReadDigit)
        self.var_Ui_DC_1Dcode.ledit_BaseAngle_DC_TableSetting.setText(self.var_ValueBaseAngle)
        self.var_Ui_DC_1Dcode.ledit_TimeOut_DC_TableSetting.setText(self.var_ValueTimeOut)


        if self.var_checkCodeResulation == "2":
            self.var_Ui_DC_1Dcode.cbox_CodeResulation_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_CodeResulation_DC_TableSetting.setChecked(False)

        if self.var_checkReferenContrast == "2":
            self.var_Ui_DC_1Dcode.cbox_ReferenceConstrast_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_ReferenceConstrast_DC_TableSetting.setChecked(False)

        if self.var_checkNumberReadDigit == "2":
            self.var_Ui_DC_1Dcode.cbox_NumberOfReadDigit_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_NumberOfReadDigit_DC_TableSetting.setChecked(False)        

        if self.var_checkCodeColor == "2":
            self.var_Ui_DC_1Dcode.cbox_CodeColor_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_CodeColor_DC_TableSetting.setChecked(False)

        if self.var_checkBaseAngle == "2":
            self.var_Ui_DC_1Dcode.cbox_BaseAngle_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_BaseAngle_DC_TableSetting.setChecked(False)

        if self.var_checkEnableCheckDigit == "2":
            self.var_Ui_DC_1Dcode.cbox_EnableCheckDigit_DC_TableSetting.setChecked(True)
        else:
            self.var_Ui_DC_1Dcode.cbox_EnableCheckDigit_DC_TableSetting.setChecked(False)