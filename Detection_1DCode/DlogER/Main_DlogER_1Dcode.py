from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

from pypylon import pylon
import cv2
import sys
import os
import configparser

from Detection_1DCode.DlogER.Ui_DlogER.I_DlogER_1Dcode import Ui_Class_DlogER_1Dcode
from Detection_1DCode.ActionFile import ActionFile

var_dirFileOS = os.getcwd()
var_dirFileOS = var_dirFileOS.rstrip()
var_dirFileOS = var_dirFileOS.replace("/Detection_1DCode","")
var_dirFileConfig = var_dirFileOS + "/" + "config"

class Class_DlogER_1Dcode(QDialog):
    var_signal_ER_Ok_1Dcode = pyqtSignal(str,str)
    var_signal_ER_Cancel_1Dcode = pyqtSignal()
    def __init__(self, parent, *args):
        super(Class_DlogER_1Dcode, self).__init__(*args)
        self.var_Ui_ER_1Dcode=Ui_Class_DlogER_1Dcode()
        self.var_Ui_ER_1Dcode.setupUi(self)

        self.file = ActionFile(var_dirFileConfig)
        self.num = self.file.func_getNumToolConfig() + 1
        self.num = self.file.func_convert_1to4Digit(self.num)
        self.nameFileSetting = str(self.num) + ".ini"
        self.config = configparser.ConfigParser()
        self.config.read(var_dirFileConfig + "/"+ self.nameFileSetting)


        self.var_Ui_ER_1Dcode.btn_OK_editRegion_1Dcode.clicked.connect(self.func_createSignalOk_ER_1Dcode)
        self.var_Ui_ER_1Dcode.btn_Cancel_editRegion_1Dcode.clicked.connect(self.func_createSignalCancel_ER_1Dcode)   
    
    def func_createSignalOk_ER_1Dcode(self):
        self.var_InspectionRegion = self.var_Ui_ER_1Dcode.comBox_InspectionRegion_1Dcode.currentText()
        self.var_ReferencImage = self.var_Ui_ER_1Dcode.btn_referencImage_1Dcode.text()
        self.var_signal_ER_Ok_1Dcode.emit(self.var_InspectionRegion,self.var_ReferencImage )
        self.func_saveDataSetting_ER()
        self.func_closeDlogER()

    def func_createSignalCancel_ER_1Dcode(self):
        print("creat signal Cancel")
        self.var_signal_ER_Cancel_1Dcode.emit()
        #self.func_closeDlogER()

    def func_closeDlogER(self):
        self.close()

    def func_showDlogER(self):
        self.show()

    #Save data for Setting of DC
    def func_saveDataSetting_ER(self):
        self.file.updateDataFile(self.nameFileSetting,"ER","InspectionRegion", self.var_InspectionRegion)
        self.file.updateDataFile(self.nameFileSetting,"ER", "ReferencImage", self.var_ReferencImage)


    #Load data for Setup from file self.config of DC    
    def func_loadDataSetup_ER(self):
        self.config.read(var_dirFileConfig + "/"+ self.nameFileSetting)
        self.var_InspectionRegion = self.config.get("ER", "InspectionRegion")
        self.var_ReferencImage = self.config.get("ER", "ReferencImage")
