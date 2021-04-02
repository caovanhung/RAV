from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtCore import Qt, pyqtSignal, QTimer

from pypylon import pylon
import cv2
import sys
import os
import configparser

from Detection_1DCode.M_1Dcode.I_1Dcode import Ui_Class_1Dcode

from Detection_1DCode.DlogDC.Main_DlogDC_1Dcode import Class_DlogDC_1Dcode
from Detection_1DCode.DlogJC.Main_DlogJC_1Dcode import Class_DlogJC_1Dcode
from Detection_1DCode.DlogRDS.Main_DlogReadData_1Dcode import Class_DlogReadData_1Dcode
from Detection_1DCode.DlogER.Main_DlogER_1Dcode import Class_DlogER_1Dcode

from Detection_1DCode.XLA.roi import MyLabel, class_DeCode1D

from Detection_1DCode.ActionFile import ActionFile

var_dirFileOS = os.getcwd()
var_dirFileOS = var_dirFileOS.rstrip()
var_dirFileOS = var_dirFileOS.replace("/Detection_1DCode","")
var_dirFileConfig = var_dirFileOS + "/" + "config"



#camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

class Class_1Dcode(QDialog):
    var_signal_ER_Cancel_1Dcode = pyqtSignal()
    var_signal_OK_1Dcode = pyqtSignal()
    def __init__(self, parent, *args):
        super(Class_1Dcode, self).__init__(*args)
        self.var_Ui_1Dcode = Ui_Class_1Dcode()
        self.var_Ui_1Dcode.setupUi(self)

        self.roi_position = MyLabel()
        self.file = ActionFile(var_dirFileConfig)

        self.var_UiDlog_DC_1D = Class_DlogDC_1Dcode(self)
        self.var_UiDlog_JC_1D = Class_DlogJC_1Dcode(self)
        self.var_UiDlog_RD_1D = Class_DlogReadData_1Dcode(self)
        self.var_UiDlog_ER_1Dcode =Class_DlogER_1Dcode(self)


        self.var_screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.var_sizeGbox=self.var_Ui_1Dcode.groupBox.frameGeometry()
        self.var_sizeFrame=self.var_Ui_1Dcode.frame_3.frameGeometry()


        #Action in Main
        self.var_Ui_1Dcode.btn_OK_1Dcode.clicked.connect(self.func_OkAddTool_1D)

        self.var_Ui_1Dcode.btn_Cancel_1Dcode.clicked.connect(self.func_CancelAddTool_1D)

        self.var_Ui_1Dcode.btn_DetectionCondition_1Dcode.clicked.connect(self.func_open_DlogDC_1D)
        self.var_Ui_1Dcode.btn_JudgmentConditions_1Dcode.clicked.connect(self.func_open_DlogJC_1D)
        self.var_Ui_1Dcode.btn_ReadDataSetting_1Dcode.clicked.connect(self.func_open_DlogRD_1D)
        self.var_Ui_1Dcode.btn_AutoTurning_1Dcode.clicked.connect(self.func_decode1D)



         #Action in Main_DlogDC
        self.var_UiDlog_DC_1D.var_signal_DC.connect(self.func_updateSetting_DC)
        self.var_UiDlog_DC_1D.var_Ui_DC_1Dcode.btn_Cancel_DC_TableSetting.clicked.connect(self.var_UiDlog_DC_1D.func_close_DC_1Dcode)
        self.var_UiDlog_DC_1D.var_Ui_DC_1Dcode.btn_Ok_DC_TableSetting.clicked.connect(self.var_UiDlog_DC_1D.func_closeAndSave_DC_1Dcode)

        #Action in Main_DlogRD
        self.var_UiDlog_RD_1D.var_Ui_RD_1Dcode.btn_Cancel_DlogReadData_1D.clicked.connect(self.var_UiDlog_RD_1D.func_close_RD_1Dcode)
        self.var_UiDlog_RD_1D.var_Ui_RD_1Dcode.btn_Ok_DlogReadData_1D.clicked.connect(self.var_UiDlog_RD_1D.func_closeAndSave_RD_1Dcode)

        #Action in Main_DlogJC
        self.var_UiDlog_JC_1D.var_Ui_JC_1Dcode.btn_Cancel_JC_TableSetting.clicked.connect(self.var_UiDlog_JC_1D.func_close_JC_1Dcode)
        self.var_UiDlog_JC_1D.var_Ui_JC_1Dcode.btn_Ok_JC_TableSetting.clicked.connect(self.var_UiDlog_JC_1D.func_closeAndSave_JC_1Dcode)


        #Action in Main_DlogER
        self.var_UiDlog_ER_1Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.tmp_with_ER_1Dcode   =int(0.8*(self.var_sizeGbox.width()-10))
        self.tmp_hight_ER_1Dcode   =int(0.8*self.var_sizeFrame.height())
        self.var_UiDlog_ER_1Dcode.setGeometry(self.var_screen.width()-self.tmp_with_ER_1Dcode,self.var_screen.height()*0.2+self.var_sizeFrame.y()+int(0.1*self.var_sizeFrame.height()),self.tmp_with_ER_1Dcode,self.tmp_hight_ER_1Dcode )
        self.var_UiDlog_ER_1Dcode.var_signal_ER_Ok_1Dcode.connect(self.func_Signal_ER_Ok_1D)
        self.var_UiDlog_ER_1Dcode.var_signal_ER_Cancel_1Dcode.connect(self.func_Signal_ER_Cancel_1D)

########################################################################################################################################################
    #Fun call from Main_fromMain.py
    def func_show_1Dcode(self):
        self.show()
        self.var_screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.var_sizeGbox=self.var_Ui_1Dcode.groupBox.frameGeometry()
        self.var_sizeFrame=self.var_Ui_1Dcode.frame_3.frameGeometry()
        ############ khoi tao ui ER EditRegion #############################
        self.var_UiDlog_ER_1Dcode =Class_DlogER_1Dcode(self)
        self.var_UiDlog_ER_1Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.tmp_with_ER_1Dcode   =int(0.8*(self.var_sizeGbox.width()-10))
        self.tmp_hight_ER_1Dcode   =int(0.8*self.var_sizeFrame.height())
        self.var_UiDlog_ER_1Dcode.setGeometry(self.var_screen.width()-self.tmp_with_ER_1Dcode,self.var_screen.height()*0.2+self.var_sizeFrame.y()+int(0.1*self.var_sizeFrame.height()),self.tmp_with_ER_1Dcode,self.tmp_hight_ER_1Dcode ) 
        self.var_UiDlog_ER_1Dcode.var_signal_ER_Ok_1Dcode.connect(self.func_Signal_ER_Ok_1D)
        self.var_UiDlog_ER_1Dcode.var_signal_ER_Cancel_1Dcode.connect(self.func_Signal_ER_Cancel_1D)
        self.var_UiDlog_ER_1Dcode.show()


    def func_decode1D(self):

        self.x_start = self.var_Ui_1Dcode.lab_showImage.x_start
        self.y_start = self.var_Ui_1Dcode.lab_showImage.y_start
        self.x_end = self.var_Ui_1Dcode.lab_showImage.x_end
        self.y_end = self.var_Ui_1Dcode.lab_showImage.y_end  
        self.codeType = self.var_Ui_1Dcode.comBox_CodeType_1Dcode.currentText() 

        self.process = class_DeCode1D(self.tmp_img_display,  self.x_start,  self.y_start,  self.x_end,  self.y_end)
        if self.x_start :
            self.var_resultDecode, self.showImage =  self.process.func_decode_1D(self.codeType)
            self.var_Ui_1Dcode.lab_ReadData_1Dcode.setText(self.var_resultDecode)
            self.var_Ui_1Dcode.lab_ReadData_1Dcode.setStyleSheet("color: rgb(0, 255, 0)")
        self.showImage = QtGui.QImage(self.tmp_img_display.data,self.tmp_img_display.shape[1],self.tmp_img_display.shape[0],QtGui.QImage.Format_RGB888)
        self.var_Ui_1Dcode.lab_showImage.setPixmap(QtGui.QPixmap.fromImage(self.showImage))

        self.func_saveData()
        self.func_saveImageProcessed(self.file.func_getNumToolConfig() ,self.tmp_img_display,self.x_start,self.y_start,self.x_end,self.y_end)
        self.func_saveImageRaw(self.file.func_getNumToolConfig() ,self.tmp_img_display)
        self.func_saveImageRawProcessed(self.file.func_getNumToolConfig() ,self.tmp_img_display)

    def func_loadDataSettingConfig(self):
        #update code type of DC
        self.var_Ui_1Dcode.comBox_CodeType_1Dcode.setCurrentText(self.config.get("DC", "CodeType"))
        self.var_Ui_1Dcode.lab_CodeResolution_1Dcode.setText(self.config.get("DC", "ValueCodeResulation"))
        #update ReadData of JC
        self.var_Ui_1Dcode.tedit_CopyReadData_1Dcode.setText(self.config.get("JC", "CopyFromReadData"))

    def func_CancelAddTool_1D(self):
        self.func_deleteFileSetting()
        self.close()

    def getSignal_OK(self):
        return  self.var_signal_OK_1Dcode

    # def creatSignal_OK(self):
    #     self.var_signal_OK_1Dcode.emit()

    def func_OkAddTool_1D(self):
        self.var_signal_OK_1Dcode.emit()

        # self.func_saveDataSetting_DC_1D()  
        # self.func_saveDataSetting_RD_1D()  
        # self.func_saveDataSetting_JC_1D()
        # self.func_saveDataSetting_ER_1D()  

        self.close()

    def func_saveData(self):
        self.x_start = self.var_Ui_1Dcode.lab_showImage.x_start
        self.y_start = self.var_Ui_1Dcode.lab_showImage.y_start
        self.x_end = self.var_Ui_1Dcode.lab_showImage.x_end
        self.y_end = self.var_Ui_1Dcode.lab_showImage.y_end 

        num = self.file.func_getNumToolConfig()
        num = self.file.func_convert_1to4Digit(num)
        dir_config = var_dirFileConfig + "/"+str(num)+".ini"
        dir_ImageRaw = var_dirFileOS + "/" + "ImageRaw"+"/"+str(num)+".jpg"
        dir_ImageProcessed = var_dirFileOS + "/" + "ImageProcessed"+"/"+str(num)+".jpg"
        dir_ImageRowProcessed = var_dirFileOS + "/" + "ImageRowProcessed"+"/"+str(num)+".jpg"

        self.config.set("PARAMETER", "x_start", str(self.x_start))
        self.config.set("PARAMETER", "y_start", str(self.y_start))
        self.config.set("PARAMETER", "x_end", str(self.x_end))
        self.config.set("PARAMETER", "y_end", str(self.y_end))
        self.config.set("Detection_1Dcode", "dir_config", str(dir_config))
        self.config.set("Detection_1Dcode", "dir_ImageRaw", str(dir_ImageRaw))
        self.config.set("Detection_1Dcode", "dir_ImageProcessed", str(dir_ImageProcessed))
        self.config.set("Detection_1Dcode", "dir_ImageRowProcessed", str(dir_ImageRowProcessed))
        self.config.write(open(var_dirFileConfig+ "/"+ str(num) + ".ini", "w"))

    def func_saveImageProcessed(self,NameImageSave,ImageOrigin, x_start, y_start, x_end, y_end ):
        NameImageSave = self.file.func_convert_1to4Digit(NameImageSave)
        dir = var_dirFileOS + "/" + "ImageRowProcessed"+"/"+str(NameImageSave)+".jpg"
        cv2.imwrite(dir, ImageOrigin[y_start:y_end, x_start:x_end])

    def func_saveImageRaw(self,NameImageSave,ImageOrigin):
        NameImageSave = self.file.func_convert_1to4Digit(NameImageSave)
        dir = var_dirFileOS + "/" + "ImageRaw"+"/"+str(NameImageSave)+".jpg"
        cv2.imwrite(dir, ImageOrigin)

    def func_saveImageRawProcessed(self,NameImageSave,ImageOrigin):
        NameImageSave = self.file.func_convert_1to4Digit(NameImageSave)
        dir = var_dirFileOS + "/" + "ImageProcessed"+"/"+str(NameImageSave)+".jpg"
        cv2.imwrite(dir, ImageOrigin)


    def func_deleteImageProcessed(self,NameImageDelete):
        NameImageDelete = self.file.func_convert_1to4Digit(NameImageDelete)
        dir = var_dirFileOS + "/" + "ImageRowProcessed"+"/"+str(NameImageDelete)+".jpg"
        os.remove(dir)
    def func_deleteImageRaw(self,NameImageDelete):
        NameImageDelete = self.file.func_convert_1to4Digit(NameImageDelete)
        dir = var_dirFileOS + "/" + "ImageRaw"+"/"+str(NameImageDelete)+".jpg"
        os.remove(dir)

    def func_deleteImageRawProcessed(self,NameImageDelete):
        NameImageDelete = self.file.func_convert_1to4Digit(NameImageDelete)
        dir = var_dirFileOS + "/" + "ImageProcessed"+"/"+str(NameImageDelete)+".jpg"
        os.remove(dir)

    def func_creatFileSetting(self):
        num = self.file.func_getNumToolConfig() + 1
        num = self.file.func_convert_1to4Digit(num)
        self.file.func_creadFileSettingStand(str(num)+".ini")

        self.config = configparser.ConfigParser()
        self.config.read(var_dirFileConfig + "/"+ str(num) + ".ini")

    def func_deleteFileSetting(self):
        num = self.file.func_getNumToolConfig() 
        num = self.file.func_convert_1to4Digit(num)
        self.file.deleteFile(str(num)+".ini")
        self.func_deleteImageProcessed(num)
        self.func_deleteImageRaw(num)
        self.func_deleteImageRawProcessed(num)

####################################################Func for DC####################################################
    
    #function update setting CodeType and ValueCodeResulation of DC(extend) for DC_1D
    def func_updateSetting_DC(self, var_CodeType_DC, var_ValueCodeResulation):
        self.var_CodeType_DC_1D = var_CodeType_DC   
        self.var_ValueCodeResulation_DC_1D = var_ValueCodeResulation
        self.var_Ui_1Dcode.lab_CodeResolution_1Dcode.setText(self.var_ValueCodeResulation_DC_1D)
        self.var_Ui_1Dcode.comBox_CodeType_1Dcode.setCurrentText(self.var_CodeType_DC_1D)

    #Function save setting Codetype_DC_1D into the setting_DC_1D.ini
    def func_saveDataSetting_DC_1D(self):
        self.var_UiDlog_DC_1D.func_loadDataSetup_DC()
        self.var_UiDlog_DC_1D.var_CodeType = self.var_Ui_1Dcode.comBox_CodeType_1Dcode.currentText()        
        self.var_UiDlog_DC_1D.func_saveDataSetting_DC()

    #Function open Dlog DC
    def func_open_DlogDC_1D(self):
        self.func_saveDataSetting_DC_1D()
        self.var_UiDlog_DC_1D.func_loadDataSetup_DC()
        self.var_UiDlog_DC_1D.func_insertDataSetup_Table_DC()
        self.var_UiDlog_DC_1D.func_show_DC_1Dcode()

    def func_getCodeType_1D(self):
        return self.config.get("DC", "CodeType")  

####################################################Func for RD####################################################


    #Function save setting Codetype_DC_1D into the setting_DC_1D.ini
    def func_saveDataSetting_RD_1D(self):
        self.var_UiDlog_RD_1D.func_loadDataSetup_RD()
        #self.var_UiDlog_JC_1D.var_ledit_CopyFromReadData = self.var_Ui_1Dcode.tedit_CopyReadData_1Dcode.text()        
        self.var_UiDlog_RD_1D.func_saveDataSetting_RD()

    #Function open Dlog RD
    def func_open_DlogRD_1D(self):
        self.func_saveDataSetting_RD_1D()
        self.var_UiDlog_RD_1D.func_loadDataSetup_RD()
        self.var_UiDlog_RD_1D.func_insertDataSetup_Table_RD()
        self.var_UiDlog_RD_1D.func_show_RD_1Dcode()

####################################################Func for JC####################################################
    
    #function update setting CodeType and ValueCodeResulation of DC(extend) for DC_1D
    def func_updateSetting_JC(self, var_ledit_CopyFromReadData_JC):
        self.var_ledit_CopyFromReadData_JC_1D = var_ledit_CopyFromReadData_JC   
        self.var_Ui_1Dcode.tedit_CopyReadData_1Dcode.setText(self.var_ledit_CopyFromReadData_JC_1D)

    #Function save setting Codetype_DC_1D into the setting_DC_1D.ini
    def func_saveDataSetting_JC_1D(self):
        self.var_UiDlog_JC_1D.func_loadDataSetup_JC()
        self.var_UiDlog_JC_1D.var_ledit_CopyFromReadData = self.var_Ui_1Dcode.tedit_CopyReadData_1Dcode.toPlainText()        
        self.var_UiDlog_JC_1D.func_saveDataSetting_JC()

    #Function open Dlog DC
    def func_open_DlogJC_1D(self):
        self.func_saveDataSetting_JC_1D()
        self.var_UiDlog_JC_1D.func_loadDataSetup_JC()
        self.var_UiDlog_JC_1D.func_insertDataSetup_Table_JC()
        self.var_UiDlog_JC_1D.func_show_JC_1Dcode()

################################################Func for ER#####################################################

    def func_Signal_ER_Cancel_1D(self):
        self.var_UiDlog_ER_1Dcode.func_closeDlogER()
        self.close()

    def func_Signal_ER_Ok_1D(self,var_InspectionRegion,var_ReferencImage):
        self.var_InspectionRegion_ER_1D = var_InspectionRegion
        self.var_ReferencImage_ER_1D = var_ReferencImage
        tmp_dirImage = var_dirFileOS + "/" + self.var_ReferencImage_ER_1D +".png"

        self.tmp_img_display=cv2.imread(tmp_dirImage,1)
        tmp_height, tmp_width, tmp_channel = self.tmp_img_display.shape
        tmp_step =  tmp_width*tmp_channel
        tmp_qImg = QImage(self.tmp_img_display.data, tmp_width, tmp_height, tmp_step, QImage.Format_RGB888)
        tmp_pixmap = QPixmap.fromImage(tmp_qImg)
        self.var_Ui_1Dcode.lab_showImage.setPixmap(QPixmap.fromImage(tmp_qImg))

        self.func_creatFileSetting()
        self.func_loadDataSettingConfig()

    def func_saveDataSetting_ER_1D(self):
        self.var_UiDlog_ER_1Dcode.func_loadDataSetup_ER()
        self.var_UiDlog_ER_1Dcode.func_saveDataSetting_ER()