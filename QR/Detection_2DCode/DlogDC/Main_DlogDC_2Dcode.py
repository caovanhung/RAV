from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from DlogDC.Ui_DlogDC.I_DlogDC_2Dcode import Ui_Class_DlogDC_2Dcode


class Class_DlogDC_2Dcode(QDialog):
    var_signal_DC_2Dcode = pyqtSignal()
    var_signalCancel_DC_2Dcode = pyqtSignal()
    def __init__(self, parent, *args):
        super(Class_DlogDC_2Dcode, self).__init__(*args)
        self.var_Ui_DC_2Dcode=Ui_Class_DlogDC_2Dcode()
        self.var_Ui_DC_2Dcode.setupUi(self)




        self.var_Ui_DC_2Dcode.btn_OK_DC_2Dcode.clicked.connect(self.func_createSignal_DC_2Dcode)

        self.var_Ui_DC_2Dcode.btn_Cancel_DC_2Dcode.clicked.connect(self.func_createSignalCancel_DC_2Dcode)

        self.var_Ui_DC_2Dcode.combox_CodeType_DC_2Dcode.currentIndexChanged.connect(self.func_typeCode_DC_2Dcode)
        self.var_Ui_DC_2Dcode.btn_AutoTuring_DC_2Dcode.clicked.connect(self.func_clickAutoTurning_DC_2Dcode)
        
        ######### code resolution #############
        self.var_Ui_DC_2Dcode.cbox_CodeResolution_DC_2Dcode.stateChanged.connect(self.func_clickCodeResolution_DC_2Dcode)
        self.var_Ui_DC_2Dcode.tedit_CodeResolution_DC_2Dcode.textChanged.connect(self.func_changeTextCodeResolution_DC_2Dcode)

        ########Reference Contrast#############
        self.var_Ui_DC_2Dcode.cbox_ReferenceContrast_DC_2Dcode.stateChanged.connect(self.func_clickReferenceContrast_DC_2Dcode)
        self.var_Ui_DC_2Dcode.comBox_ReferenceContrast_DC_2Dcode.currentIndexChanged.connect(self.func_changeComBoxReferenceContrast_DC_2Dcode)
        
        
        ##########    number cell ################
        self.var_Ui_DC_2Dcode.cbox_NumberCells_DC_2Dcode.stateChanged.connect(self.func_clickNumberCell_DC_2Dcode)
        self.var_Ui_DC_2Dcode.combox_NumberCell_DC_2Dcode.currentIndexChanged.connect(self.func_changeComboxNumberCell_DC_2Dcode)

        ##########    code color ################
        self.var_Ui_DC_2Dcode.cbox_CodeColor_DC_2Dcode.stateChanged.connect(self.func_clickCodeColor_DC_2Dcode)
        self.var_Ui_DC_2Dcode.combox_CodeColor_DC_2Dcode.currentIndexChanged.connect(self.func_changeComboxCodeColor_DC_2Dcode)


        ##########    mirrrored Reading  ################
        self.var_Ui_DC_2Dcode.cbox_MirroredReading_DC_2Dcode.stateChanged.connect(self.func_clickMirroredReading_DC_2Dcode)
        self.var_Ui_DC_2Dcode.combox_MirroredReading_DC_2Dcode.currentIndexChanged.connect(self.func_changeComboxMirroredReading_DC_2Dcode)


        ######### Base Angle  ##########################
        self.var_Ui_DC_2Dcode.cbox_BaseAngle_DC_2Dcode.stateChanged.connect(self.func_clickBaseAngle_DC_2Dcode)
        self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.textChanged.connect(self.func_changeTextBaseAngle_DC_2Dcode)

        ########## angle range ########################
        self.var_Ui_DC_2Dcode.tedit_AngleRange_DC_2Dcode.textChanged.connect(self.func_changeAngleRange_DC_2Dcode)

        ########## Scale Variation   #################
        self.var_Ui_DC_2Dcode.combox_ScaleVariation_DC_2Dcode.currentIndexChanged.connect(self.func_changeScaleVariation_DC_2Dcode)

        ##########Time Out ##########################
        self.var_Ui_DC_2Dcode.tedit_Timeout_DC_2Dcode.textChanged.connect(self.func_changeTimeOut_DC_2Dcode)        
        
      #  self.func_readData_DC_2Dcode()
    def func_getSignal_DC_2Dcode(self):
        return self.var_signal_DC_2Dcode


    def func_createSignalCancel_DC_2Dcode(self):
        self.var_signalCancel_DC_2Dcode.emit()
     #   self.var_dataSetting=self.var_dataSetting_orinal

        self.var_filedata_orinal = open(self.var_fileConfig, 'w')
        self.var_filedata_orinal.writelines(self.var_dataSetting_orinal)
        self.var_filedata_orinal.close()

       # print("cai dat",self.var_dataSetting_orinal)
       # self.func_wirteData_DC_2Dcode() 
        self.func_close_DC_2Dcode()
        

    
    def func_createSignal_DC_2Dcode(self):
        self.var_signal_DC_2Dcode.emit()
      #  print(self.var_dataSetting)


        

    def func_setConfigFile_DC_2Dcode(self,tmp_fileConfig):
       # print(tmp_fileConfig)
        self.var_fileConfig=tmp_fileConfig

#######  close function ######## 
    def func_close_DC_2Dcode(self):
        self.close()
######################## read data da luu #######


    def func_readData_DC_2Dcode(self):
        self.var_fileData_orinal=open(self.var_fileConfig,"r")
        self.var_dataSetting_orinal=self.var_fileData_orinal.readlines()
        self.var_fileData_orinal.close()



        self.var_fileData=open(self.var_fileConfig,"r")
        self.var_dataSetting=self.var_fileData.readlines()

        self.func_readTypeData_DC_2Dcode()
        self.func_readAutoTurning_DC_2Dcode()

        self.func_readCodeResolution_DC_2Dcode()
        self.func_readNumbeCell_DC_2Dcode()
        self.func_readReferenceContrast_DC_2Dcode()
        self.func_readcodeColor_DC_2Dcode()
        self.func_readMirroredReading_DC_2Dcode()
        self.func_readBaseAngle_DC_2Dcode()
        self.func_readAngleRange_DC_2Dcode()
        self.func_readScaleVariation_DC_2Dcode()
        self.func_readTimeout_DC_2Dcode()



        
    ########doc loai code##########
    def func_readTypeData_DC_2Dcode(self):
        self.tmp_line5=self.var_dataSetting[5]
     
        self.tmp_typeData=self.tmp_line5[2:len(self.tmp_line5)]
        self.tmp_typeData=self.tmp_typeData.rstrip()
        self.var_Ui_DC_2Dcode.combox_CodeType_DC_2Dcode.setCurrentText(self.tmp_typeData)

        
    ###### doc auto turning##########
    def func_readAutoTurning_DC_2Dcode(self):
        self.tmp_line6=self.var_dataSetting[6]  
        self.tmp_autoTuring=self.tmp_line6[2:len(self.tmp_line6)]
        self.tmp_autoTuring=self.tmp_autoTuring.rstrip()
        if (self.tmp_autoTuring=="1"):
            self.var_Ui_DC_2Dcode.btn_AutoTuring_DC_2Dcode.setStyleSheet("background-color: blue")
        else :
            self.var_Ui_DC_2Dcode.btn_AutoTuring_DC_2Dcode.setStyleSheet("background-color: white")
        

    
            
    ###### doc code resolution ############################
    def func_readCodeResolution_DC_2Dcode(self):            
        self.tmp_line8=self.var_dataSetting[8]
        self.tmp_line8=self.tmp_line8.rstrip()
      #  print(self.tmp_line8)
        if (len(self.tmp_line8)==1):
            self.var_Ui_DC_2Dcode.tedit_CodeResolution_DC_2Dcode.setEnabled(False)
            self.var_Ui_DC_2Dcode.cbox_CodeResolution_DC_2Dcode.setChecked(0)
            self.var_Ui_DC_2Dcode.tedit_CodeResolution_DC_2Dcode.setPlainText("")
        else :
            self.var_Ui_DC_2Dcode.tedit_CodeResolution_DC_2Dcode.setEnabled(True)
            self.tmp_codeResolution=self.tmp_line8[2]
            self.tmp_codeResolution=self.tmp_codeResolution.rstrip()
            if self.tmp_codeResolution =="0":
                self.var_Ui_DC_2Dcode.cbox_CodeResolution_DC_2Dcode.setChecked(0)
            else :
                self.var_Ui_DC_2Dcode.cbox_CodeResolution_DC_2Dcode.setChecked(1)
              #  print("da chay")
                self.tmp_codeResolution_Data=self.tmp_line8[3:len(self.tmp_line8)]
                self.tmp_codeResolution_Data=self.tmp_codeResolution_Data.rstrip()
                self.var_Ui_DC_2Dcode.tedit_CodeResolution_DC_2Dcode.setPlainText(self.tmp_codeResolution_Data)
                
                
    ###### doc Reference Contrast ############################
    def func_readReferenceContrast_DC_2Dcode(self): 
        self.tmp_line9=self.var_dataSetting[9]
        self.tmp_line9=self.tmp_line9.rstrip()

        if len(self.tmp_line9)==1:
            self.var_Ui_DC_2Dcode.comBox_ReferenceContrast_DC_2Dcode.setEnabled(False)
            self.var_Ui_DC_2Dcode.cbox_ReferenceContrast_DC_2Dcode.setChecked(0)
        else:
            self.var_Ui_DC_2Dcode.comBox_ReferenceContrast_DC_2Dcode.setEnabled(True)
            self.tmp_referenceContrast=self.tmp_line9[2]
            self.tmp_referenceContrast=self.tmp_numberCell.rstrip()            
            if (self.tmp_referenceContrast=="0"):        
                self.var_Ui_DC_2Dcode.cbox_ReferenceContrast_DC_2Dcode.setChecked(0)
            else :
                self.var_Ui_DC_2Dcode.cbox_ReferenceContrast_DC_2Dcode.setChecked(1)                
           #     print("da chay")
                self.tmp_referenceContrast_Data=self.tmp_line9[3:len(self.tmp_line9)]
                self.tmp_referenceContrast_Data=self.tmp_referenceContrast_Data.rstrip()
                self.var_Ui_DC_2Dcode.comBox_ReferenceContrast_DC_2Dcode.setCurrentText(self.tmp_referenceContrast_Data)
    ###### doc number Cell ############################
    def func_readNumbeCell_DC_2Dcode(self): 
        self.tmp_line10=self.var_dataSetting[10]
        self.tmp_line10=self.tmp_line10.rstrip()


        if len(self.tmp_line10)==1:
            self.var_Ui_DC_2Dcode.combox_NumberCell_DC_2Dcode.setEnabled(False)
            self.var_Ui_DC_2Dcode.cbox_NumberCells_DC_2Dcode.setChecked(0)
        else:
            self.var_Ui_DC_2Dcode.combox_NumberCell_DC_2Dcode.setEnabled(True)
            self.tmp_numberCell=self.tmp_line10[2]
            self.tmp_numberCell=self.tmp_numberCell.rstrip()            
            if (self.tmp_numberCell=="0"):        
                self.var_Ui_DC_2Dcode.cbox_NumberCells_DC_2Dcode.setChecked(0)
            else :
                self.var_Ui_DC_2Dcode.cbox_NumberCells_DC_2Dcode.setChecked(1)  
             #   print("da chay")
                self.tmp_numberCell_Data=self.tmp_line10[3:len(self.tmp_line10)]
                self.tmp_numberCell_Data=self.tmp_numberCell_Data.rstrip()
                self.var_Ui_DC_2Dcode.combox_NumberCell_DC_2Dcode.setCurrentText(self.tmp_numberCell_Data)



    ###### doc Code Color ############################
    def func_readcodeColor_DC_2Dcode(self): 
        self.tmp_line11=self.var_dataSetting[11]
        self.tmp_line11=self.tmp_line11.rstrip()

        

      #  print(self.tmp_numberCell)
        if len(self.tmp_line11)==1:
            self.var_Ui_DC_2Dcode.combox_CodeColor_DC_2Dcode.setEnabled(False)
            self.var_Ui_DC_2Dcode.cbox_CodeColor_DC_2Dcode.setChecked(0)
        else:
            self.var_Ui_DC_2Dcode.combox_CodeColor_DC_2Dcode.setEnabled(True)
            self.tmp_codeColor=self.tmp_line11[2]
            self.tmp_codeColor=self.tmp_codeColor.rstrip()            
            if (self.tmp_codeColor=="0"):        
                self.var_Ui_DC_2Dcode.cbox_CodeColor_DC_2Dcode.setChecked(0)
            else :
                self.var_Ui_DC_2Dcode.cbox_CodeColor_DC_2Dcode.setChecked(1)  

                self.tmp_codeColor_Data=self.tmp_line11[3:len(self.tmp_line11)]
                self.tmp_codeColor_Data=self.tmp_codeColor_Data.rstrip()
                self.var_Ui_DC_2Dcode.combox_CodeColor_DC_2Dcode.setCurrentText(self.tmp_codeColor_Data)


 

    ###### doc Mirrored Reading ############################
    def func_readMirroredReading_DC_2Dcode(self): 
        self.tmp_line12=self.var_dataSetting[12]  
        self.tmp_line12=self.tmp_line12.rstrip()

        

      #  print(self.tmp_numberCell)
        if len(self.tmp_line12)==1:
            self.var_Ui_DC_2Dcode.combox_MirroredReading_DC_2Dcode.setEnabled(False)
            self.var_Ui_DC_2Dcode.cbox_MirroredReading_DC_2Dcode.setChecked(0)
            

        else:
            self.var_Ui_DC_2Dcode.combox_MirroredReading_DC_2Dcode.setEnabled(True)
            self.tmp_mirroredReading=self.tmp_line12[2]
            self.tmp_mirroredReading=self.tmp_mirroredReading.rstrip()            
            if (self.tmp_mirroredReading=="0"):        
                self.var_Ui_DC_2Dcode.cbox_MirroredReading_DC_2Dcode.setChecked(0)
            else :
                self.var_Ui_DC_2Dcode.cbox_MirroredReading_DC_2Dcode.setChecked(1)
                
                self.tmp_mirroredReading_Data=self.tmp_line11[3:len(self.tmp_line12)]
                self.tmp_mirroredReading_Data=self.tmp_mirroredReading_Data.rstrip()
                self.var_Ui_DC_2Dcode.combox_MirroredReading_DC_2Dcode.setCurrentText(self.tmp_mirroredReading_Data)


    ###### doc Base Angle ############################
    def func_readBaseAngle_DC_2Dcode(self): 
        self.tmp_line13=self.var_dataSetting[13]  
        self.tmp_line13=self.tmp_line13.rstrip()
        if len(self.tmp_line13)==1:
            self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.setEnabled(False)
            self.var_Ui_DC_2Dcode.cbox_BaseAngle_DC_2Dcode.setChecked(0)
            self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.setPlainText("")
        else:
            self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.setEnabled(True)
            self.tmp_baseAngle=self.tmp_line13[2]
            self.tmp_baseAngle=self.tmp_baseAngle.rstrip()            
            if (self.tmp_baseAngle=="0"):        
                self.var_Ui_DC_2Dcode.cbox_BaseAngle_DC_2Dcode.setChecked(0)
            else :
                self.var_Ui_DC_2Dcode.cbox_BaseAngle_DC_2Dcode.setChecked(1)  

                self.tmp_baseAngle_Data=self.tmp_line13[3:len(self.tmp_line13)]
                self.tmp_baseAngle_Data=self.tmp_baseAngle_Data.rstrip()
                self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.setPlainText(self.tmp_baseAngle_Data)

    ####### doc  angle range ###########

    def func_readAngleRange_DC_2Dcode(self): 
        self.tmp_line14=self.var_dataSetting[14]  
        self.tmp_line14=self.tmp_line14.rstrip()
        if len(self.tmp_line14)==1:
            self.var_Ui_DC_2Dcode.tedit_AngleRange_DC_2Dcode.setPlainText("180")
        else:
           # self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.setEnabled(True)
            self.tmp_AngleRange=self.tmp_line14[2:len(self.tmp_line14)]
            self.tmp_AngleRange=self.tmp_AngleRange.rstrip()
            self.var_Ui_DC_2Dcode.tedit_AngleRange_DC_2Dcode.setPlainText(self.tmp_AngleRange)
    ####### doc Scale Variation ###########
    def func_readScaleVariation_DC_2Dcode(self): 
        self.tmp_line15=self.var_dataSetting[15]  
        self.tmp_line15=self.tmp_line15.rstrip()
        if len(self.tmp_line15)!=1:

            self.tmp_ScaleVariation=self.tmp_line15[2:len(self.tmp_line15)]
            self.tmp_ScaleVariation=self.tmp_AngleRange.rstrip()
            self.var_Ui_DC_2Dcode.combox_ScaleVariation_DC_2Dcode.setCurrentText(self.tmp_ScaleVariation)

    ####### doc  Time out ###########

    def func_readTimeout_DC_2Dcode(self): 
        self.tmp_line16=self.var_dataSetting[16]  
        self.tmp_line16=self.tmp_line16.rstrip()
        if len(self.tmp_line16)==1:
            self.var_Ui_DC_2Dcode.tedit_Timeout_DC_2Dcode.setPlainText("3")
        else:
           # self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.setEnabled(True)
            self.tmp_Timeout=self.tmp_line16[2:len(self.tmp_line16)]
            self.tmp_Timeout=self.tmp_Timeout.rstrip()
            self.var_Ui_DC_2Dcode.tedit_Timeout_DC_2Dcode.setPlainText(self.tmp_Timeout)
                 
####################set up cac thong so tren main######

    def func_wirteData_DC_2Dcode(self):
        self.var_filedata = open(self.var_fileConfig, 'w')
        self.var_filedata.writelines(self.var_dataSetting)
        self.var_filedata.close()

    def func_typeCode_DC_2Dcode(self):
        self.var_typeCode_DC_2Dcode=self.var_Ui_DC_2Dcode.combox_CodeType_DC_2Dcode.currentText()
        self.var_dataSetting[5]="1 "+self.var_typeCode_DC_2Dcode+"\n"
        self.func_wirteData_DC_2Dcode()

        

        
    def func_clickAutoTurning_DC_2Dcode(self):
        self.var_dataSetting[6]="1 "+"1"+"\n"
        self.var_Ui_DC_2Dcode.btn_AutoTuring_DC_2Dcode.setStyleSheet("background-color: blue")
        self.func_wirteData_DC_2Dcode()
       
     ########### code resolution##############
    def func_clickCodeResolution_DC_2Dcode(self):
        if  self.var_Ui_DC_2Dcode.cbox_CodeResolution_DC_2Dcode.isChecked():  
            self.var_dataSetting[8]="1 "+"1"+"\n"
            self.var_Ui_DC_2Dcode.tedit_CodeResolution_DC_2Dcode.setEnabled(True)
            self.func_wirteData_DC_2Dcode()        
        else:
            self.var_dataSetting[8]="0"+"\n"
            self.var_Ui_DC_2Dcode.tedit_CodeResolution_DC_2Dcode.setEnabled(False)
            self.func_wirteData_DC_2Dcode() 
    def func_changeTextCodeResolution_DC_2Dcode(self):
        self.tmp_textCodeResolution=self.var_Ui_DC_2Dcode.tedit_CodeResolution_DC_2Dcode.toPlainText()
        if len( self.tmp_textCodeResolution)!=0:

            self.var_dataSetting[8]="1 "+"1"+" "+self.tmp_textCodeResolution+"\n"
            self.var_Ui_DC_2Dcode.tedit_CodeResolution_DC_2Dcode.setEnabled(True)
            self.func_wirteData_DC_2Dcode()        

    ############ Reference Contrast ############
    def func_clickReferenceContrast_DC_2Dcode(self):
        if  self.var_Ui_DC_2Dcode.cbox_ReferenceContrast_DC_2Dcode.isChecked():
        
            self.tmp_comBoxReferenceContrast_DC_2Dcode=self.var_Ui_DC_2Dcode.comBox_ReferenceContrast_DC_2Dcode.currentText()
            self.var_dataSetting[9]="1 "+"1"+" "+self.tmp_comBoxReferenceContrast_DC_2Dcode+"\n"
            self.var_Ui_DC_2Dcode.comBox_ReferenceContrast_DC_2Dcode.setEnabled(True)
            self.func_wirteData_DC_2Dcode()  
        else:
            self.var_dataSetting[9]="0"+"\n"
            self.var_Ui_DC_2Dcode.comBox_ReferenceContrast_DC_2Dcode.setEnabled(False)
            self.func_wirteData_DC_2Dcode() 

    def func_changeComBoxReferenceContrast_DC_2Dcode(self):
        self.tmp_comBoxReferenceContrast_DC_2Dcode=self.var_Ui_DC_2Dcode.comBox_ReferenceContrast_DC_2Dcode.currentText()
        self.var_dataSetting[9]="1 "+"1"+" "+self.tmp_comBoxReferenceContrast_DC_2Dcode+"\n"
        self.var_Ui_DC_2Dcode.comBox_ReferenceContrast_DC_2Dcode.setEnabled(True)
        self.func_wirteData_DC_2Dcode()               


    ############ Number Cell ############

    def func_clickNumberCell_DC_2Dcode(self):
        if  self.var_Ui_DC_2Dcode.cbox_NumberCells_DC_2Dcode.isChecked():  
            self.tmp_comboxNumberCell_DC_2Dcode=self.var_Ui_DC_2Dcode.combox_NumberCell_DC_2Dcode.currentText()
            self.var_dataSetting[10]="1 "+"1"+" "+self.tmp_comboxNumberCell_DC_2Dcode+"\n"
            self.var_Ui_DC_2Dcode.combox_NumberCell_DC_2Dcode.setEnabled(True)
            self.func_wirteData_DC_2Dcode() 
        else:
            self.var_dataSetting[10]="0"+"\n"
            self.var_Ui_DC_2Dcode.combox_NumberCell_DC_2Dcode.setEnabled(False)
            self.func_wirteData_DC_2Dcode() 
        
    def func_changeComboxNumberCell_DC_2Dcode(self):
        self.tmp_comboxNumberCell_DC_2Dcode=self.var_Ui_DC_2Dcode.combox_NumberCell_DC_2Dcode.currentText()
        self.var_dataSetting[10]="1 "+"1"+" "+self.tmp_comboxNumberCell_DC_2Dcode+"\n"
        self.var_Ui_DC_2Dcode.combox_NumberCell_DC_2Dcode.setEnabled(True)
        self.func_wirteData_DC_2Dcode() 


    ####### Code Color  ################

    def func_clickCodeColor_DC_2Dcode(self):
        if  self.var_Ui_DC_2Dcode.cbox_CodeColor_DC_2Dcode.isChecked():  
            self.tmp_comboxCodeColor_DC_2Dcode=self.var_Ui_DC_2Dcode.combox_CodeColor_DC_2Dcode.currentText()
            self.var_dataSetting[11]="1 "+"1"+" "+self.tmp_comboxCodeColor_DC_2Dcode+"\n"
            self.var_Ui_DC_2Dcode.combox_CodeColor_DC_2Dcode.setEnabled(True)
            self.func_wirteData_DC_2Dcode()
        
        else:
            self.var_dataSetting[11]="0"+"\n"
            self.var_Ui_DC_2Dcode.combox_CodeColor_DC_2Dcode.setEnabled(False)
            self.func_wirteData_DC_2Dcode() 
    def func_changeComboxCodeColor_DC_2Dcode(self):
        self.tmp_comboxCodeColor_DC_2Dcode=self.var_Ui_DC_2Dcode.combox_CodeColor_DC_2Dcode.currentText()
        self.var_dataSetting[11]="1 "+"1"+" "+self.tmp_comboxCodeColor_DC_2Dcode+"\n"
        self.var_Ui_DC_2Dcode.combox_CodeColor_DC_2Dcode.setEnabled(True)
        self.func_wirteData_DC_2Dcode()

   #########  Mirrored Reading ##########

    def func_clickMirroredReading_DC_2Dcode(self):
        if  self.var_Ui_DC_2Dcode.cbox_MirroredReading_DC_2Dcode.isChecked():  
            self.tmp_comboxMirroredReading_DC_2Dcode=self.var_Ui_DC_2Dcode.combox_MirroredReading_DC_2Dcode.currentText()
            self.var_dataSetting[12]="1 "+"1"+" "+self.tmp_comboxMirroredReading_DC_2Dcode+"\n"
            self.var_Ui_DC_2Dcode.combox_MirroredReading_DC_2Dcode.setEnabled(True)
            self.func_wirteData_DC_2Dcode()
        else:
            self.var_dataSetting[12]="0"+"\n"
            self.var_Ui_DC_2Dcode.combox_MirroredReading_DC_2Dcode.setEnabled(False)
            self.func_wirteData_DC_2Dcode()            

        
    def func_changeComboxMirroredReading_DC_2Dcode(self):
        self.tmp_comboxMirroredReading_DC_2Dcode=self.var_Ui_DC_2Dcode.combox_MirroredReading_DC_2Dcode.currentText()
        self.var_dataSetting[12]="1 "+"1"+" "+self.tmp_comboxMirroredReading_DC_2Dcode+"\n"
        self.var_Ui_DC_2Dcode.combox_MirroredReading_DC_2Dcode.setEnabled(True)
        self.func_wirteData_DC_2Dcode()


     ########### Base Angle ##############
    def func_clickBaseAngle_DC_2Dcode(self):
        if  self.var_Ui_DC_2Dcode.cbox_BaseAngle_DC_2Dcode.isChecked():    
            self.var_dataSetting[13]="1 "+"1"+"\n"
            self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.setEnabled(True)
            self.func_wirteData_DC_2Dcode()
        else:
            self.var_dataSetting[13]="0"+"\n"
            self.func_wirteData_DC_2Dcode()
            self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.setEnabled(False)
            

    def func_changeTextBaseAngle_DC_2Dcode(self):
        self.tmp_textBaseAngle=self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.toPlainText()
        if len(self.tmp_textBaseAngle)!=0:
            self.var_dataSetting[13]="1 "+"1"+" "+self.tmp_textBaseAngle+"\n"
            self.var_Ui_DC_2Dcode.tedit_BaseAngle_DC_2Dcode.setEnabled(True)
            self.func_wirteData_DC_2Dcode()

        
    ########## angle range ###########
    def func_changeAngleRange_DC_2Dcode(self):
        self.tmp_textAngleRange=self.var_Ui_DC_2Dcode.tedit_AngleRange_DC_2Dcode.toPlainText()
        self.var_dataSetting[14]="1 "+self.tmp_textAngleRange+"\n"
        self.func_wirteData_DC_2Dcode()

        
    ########## Scale Variation########
    def func_changeScaleVariation_DC_2Dcode(self):
        self.tmp_combox_ScaleVariation=self.var_Ui_DC_2Dcode.combox_ScaleVariation_DC_2Dcode.currentText()
        self.var_dataSetting[15]="1 "+self.tmp_combox_ScaleVariation+"\n"
        self.func_wirteData_DC_2Dcode()


    ########## angle range ###########
    def func_changeTimeOut_DC_2Dcode(self):
        self.tmp_textTimeOut=self.var_Ui_DC_2Dcode.tedit_Timeout_DC_2Dcode.toPlainText()
        self.var_dataSetting[16]="1 "+self.tmp_textTimeOut+"\n"
        self.func_wirteData_DC_2Dcode()


########### write data ##############################
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= Class_DlogDC_2Dcode(None)
    mainWindow.show()
    sys.exit(app.exec_())
