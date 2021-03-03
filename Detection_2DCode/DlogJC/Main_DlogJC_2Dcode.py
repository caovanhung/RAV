from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from Detection_2DCode.DlogJC.Ui_DlogJC.I_DlogJC_2Dcode import Ui_Class_DlogJC_2Dcode


class Class_DlogJC_2Dcode(QDialog):
    var_signal_JC_2Dcode = pyqtSignal()
    def __init__(self, parent, *args):
        super(Class_DlogJC_2Dcode, self).__init__(*args)
        self.var_Ui_JC_2Dcode=Ui_Class_DlogJC_2Dcode()
        self.var_Ui_JC_2Dcode.setupUi(self)

        self.var_Ui_JC_2Dcode.btn_OK_JC_2Dcode.clicked.connect(self.func_createSignal_JC_2Dcode)
        self.var_Ui_JC_2Dcode.btn_Cancel_JC_2Dcode.clicked.connect(self.func_createSignal_Cancel_JC_2Dcode)






        self.var_Ui_JC_2Dcode.cbox_Single_JC_2Dcode.stateChanged.connect(self.func_clickConditionSingle_JC_2Dcode)        
        self.var_Ui_JC_2Dcode.cbox_Multiple_JC_2Dcode.stateChanged.connect(self.func_clickConditionMultiple_JC_2Dcode)
        self.var_Ui_JC_2Dcode.btn_CopyReadData_JC_2Dcode.clicked.connect(self.func_clickCopyData_JC_2Dcode)
        self.var_Ui_JC_2Dcode.tedit_CopyReadData_JC_2Dcode.textChanged.connect(self.func_changeCopyData_JC_2Dcode)
     
     
        self.var_Ui_JC_2Dcode.tedit_UpperLimit_Length_JC_2Dcode.textChanged.connect(self.func_change_Upper_Lower)
        self.var_Ui_JC_2Dcode.tedit_LowerLimit_Length_JC_2Dcode.textChanged.connect(self.func_change_Upper_Lower)

        self.var_Ui_JC_2Dcode.tedit_LowerLimit_PosX_JC_2Dcode_2.textChanged.connect(self.func_change_Upper_Lower)
        self.var_Ui_JC_2Dcode.tedit_LowerLimit_PosY_JC_2Dcode.textChanged.connect(self.func_change_Upper_Lower)

        self.var_Ui_JC_2Dcode.tedit_UpperLimit_PosX_JC_2Dcode.textChanged.connect(self.func_change_Upper_Lower)
        self.var_Ui_JC_2Dcode.tedit_UpperLimit_PosY_JC_2Dcode.textChanged.connect(self.func_change_Upper_Lower)

        self.var_Ui_JC_2Dcode.tedit_LowerLimit_Angle_JC_2Dcode.textChanged.connect(self.func_change_Upper_Lower)
        self.var_Ui_JC_2Dcode.tedit_UpperLimit_Angle_JC_2Dcode.textChanged.connect(self.func_change_Upper_Lower)




    def func_getSignal_JC_2Dcode(self):
        return self.var_signal_JC_2Dcode
    def func_createSignal_JC_2Dcode(self):
        self.var_signal_JC_2Dcode.emit()
     #   self.func_change_Upper_Lower()
        



    def func_setConfigFile_JC_2Dcode(self,tmp_fileConfig):
        self.var_fileConfig=tmp_fileConfig

    def func_createSignal_Cancel_JC_2Dcode(self):
        self.var_filedata = open(self.var_fileConfig, 'w')
        self.var_filedata.writelines(self.var_dataSetting_or)
        self.var_filedata.close()
       # print("da chay")
        self.close()

######################## read data da luu #######


    def func_readData_JC_2Dcode(self):
        self.var_fileData_or=open(self.var_fileConfig,"r")
        self.var_dataSetting_or=self.var_fileData_or.readlines()
        self.var_fileData_or.close()



        self.var_fileData=open(self.var_fileConfig,"r")
        self.var_dataSetting=self.var_fileData.readlines()
        self.func_readConditionSingle_JC_2Dcode()
        self.func_readConditionMultiple_JC_2Dcode()
        self.func_readDataRange_JC_2Dcode()
        self.func_readStartDigit_JC_2Dcode()
        self.func_readRangeDigit_JC_2Dcode()
        self.func_readDataReaded_JC_2Dcode()
        self.func_readCopyData_JC_2Dcode()
        self.func_readConverData_JC_2Dcode()

        self.func_readCollationResult_JC_2Dcode()

        self.func_readLengthDataLower_JC_2Dcode()
        self.func_readLengthDataMeasure_JC_2Dcode()
        self.func_readLengthDataUpper_JC_2Dcode()


        self.func_readPosXDataLower_JC_2Dcode()
        self.func_readPosXDataMeasure_JC_2Dcode()
        self.func_readPosXDataUpper_JC_2Dcode()

        self.func_readPosYDataLower_JC_2Dcode()
        self.func_readPosYDataMeasure_JC_2Dcode()
        self.func_readPosYDataUpper_JC_2Dcode()

        self.func_readDataAngleLower_JC_2Dcode()
        self.func_readDataAngleMeasure_JC_2Dcode()
        self.func_readDataAngleUpper_JC_2Dcode()
       
        


    ###### condition single ############################
    def func_readConditionSingle_JC_2Dcode(self):            
        self.tmp_line54=self.var_dataSetting[54]
        self.tmp_line54=self.tmp_line54.rstrip()
        if (len(self.tmp_line54)==1):
            #self.var_Ui_JC_2Dcode.cbox_Single_JC_2Dcode.setEnabled(False)
            self.var_Ui_JC_2Dcode.cbox_Single_JC_2Dcode.setChecked(0)

        else :
          #  self.var_Ui_JC_2Dcode.cbox_Single_JC_2Dcode.setEnabled(True)
            self.tmp_condtitionSingle=self.tmp_line54[2]
            self.tmp_condtitionSingle=self.tmp_condtitionSingle.rstrip()
            if self.tmp_condtitionSingle =="0":
                self.var_Ui_JC_2Dcode.cbox_Single_JC_2Dcode.setChecked(0)
            else :
                self.var_Ui_JC_2Dcode.cbox_Single_JC_2Dcode.setChecked(1)
                self.var_Ui_JC_2Dcode.btn_ConditionsList_JC_2Dcode.setEnabled(False)

     ###### condition Multiple ############################
    def func_readConditionMultiple_JC_2Dcode(self):            
        self.tmp_line55=self.var_dataSetting[55]
        self.tmp_line55=self.tmp_line55.rstrip()
        if (len(self.tmp_line55)==1):
            #self.var_Ui_JC_2Dcode.cbox_Multiple_JC_2Dcode.setEnabled(False)
            self.var_Ui_JC_2Dcode.cbox_Multiple_JC_2Dcode.setChecked(0)
        else :
           # self.var_Ui_JC_2Dcode.cbox_Multiple_JC_2Dcode.setEnabled(True)
            self.tmp_condtitionMultiple=self.tmp_line55[2]
            self.tmp_condtitionMultiple=self.tmp_condtitionMultiple.rstrip()
            if self.tmp_condtitionMultiple =="0":
                self.var_Ui_JC_2Dcode.cbox_Multiple_JC_2Dcode.setChecked(0)
            else :
                self.var_Ui_JC_2Dcode.cbox_Multiple_JC_2Dcode.setChecked(1)
                self.var_Ui_JC_2Dcode.btn_ConditionsList_JC_2Dcode.setEnabled(True)               


     ###### Data Range ############################
    def func_readDataRange_JC_2Dcode(self):            
        self.tmp_line19=self.var_dataSetting[19]
        self.tmp_line19=self.tmp_line19.rstrip()
        #self.tmp_splitData=self.tmp_line19[2]
       # self.tmp_splitData=self.tmp_splitData.rstrip()
        if (len(self.tmp_line19)!=1):
            self.tmp_splitData=self.tmp_line19[2]
            self.tmp_splitData=self.tmp_splitData.rstrip()
            if self.tmp_splitData=="1":
                self.var_Ui_JC_2Dcode.combox_DataRange_JC_2Dcode.setEnabled(True)
                self.tmp_line56=self.var_dataSetting[56]
                self.tmp_DataRange=self.tmp_line56[2:len(self.tmp_line56)]
                self.tmp_DataRange=self.tmp_DataRange.rstrip()
                self.var_Ui_JC_2Dcode.combox_DataRange_JC_2Dcode.setCurrentText(self.tmp_DataRange) 
            
        else :
            self.var_Ui_JC_2Dcode.combox_DataRange_JC_2Dcode.setEnabled(False)

     ###### Start Digit ############################
    def func_readStartDigit_JC_2Dcode(self):            
        self.tmp_line17=self.var_dataSetting[17]
        self.tmp_line17=self.tmp_line17.rstrip()
        self.tmp_startDigit=self.tmp_line17[2:len(self.tmp_line17)]
     #   print(self.tmp_startDigit)
        self.var_Ui_JC_2Dcode.lab_StartDigit_JC_2Dcode.setText(self.tmp_startDigit)

    def func_readRangeDigit_JC_2Dcode(self):            
        self.tmp_line18=self.var_dataSetting[18]
        self.tmp_line18=self.tmp_line18.rstrip()
        self.tmp_rangeDigit=self.tmp_line18[2:len(self.tmp_line18)]
     #   print(self.tmp_rangeDigit)
        self.var_Ui_JC_2Dcode.lab_EndDigit_JC_2Dcode.setText(self.tmp_rangeDigit)
  
    ########## read data ##################
    def func_readDataReaded_JC_2Dcode(self):
        self.tmp_line57=self.var_dataSetting[57]
        self.tmp_line57=self.tmp_line57.rstrip()
        if len(self.tmp_line57) !=1:
            self.tmp_dataReaded=self.tmp_line57[2:len(self.tmp_line57)]
            self.tmp_dataReaded=self.tmp_dataReaded.rstrip()
            if (len(self.tmp_dataReaded)!=0):
                if self.tmp_dataReaded !="Khong phat hien":
                    self.var_Ui_JC_2Dcode.lab_ReadData_JC_2Dcode.setText(self.tmp_dataReaded)
                    self.var_Ui_JC_2Dcode.btn_CopyReadData_JC_2Dcode.setEnabled(1)
                    self.var_Ui_JC_2Dcode.btn_ConversionSetting_JC_2Dcode.setEnabled(1)
                    self.var_Ui_JC_2Dcode.tedit_CopyReadData_JC_2Dcode.setEnabled(1)
                else:
                    self.var_Ui_JC_2Dcode.btn_CopyReadData_JC_2Dcode.setEnabled(0)
                    self.var_Ui_JC_2Dcode.btn_ConversionSetting_JC_2Dcode.setEnabled(0)
                    self.var_Ui_JC_2Dcode.tedit_CopyReadData_JC_2Dcode.setEnabled(0)                   
        else :
            self.var_Ui_JC_2Dcode.lab_ReadData_JC_2Dcode.setText("")
            self.var_Ui_JC_2Dcode.btn_CopyReadData_JC_2Dcode.setEnabled(0)
            self.var_Ui_JC_2Dcode.btn_ConversionSetting_JC_2Dcode.setEnabled(0)
            self.var_Ui_JC_2Dcode.tedit_CopyReadData_JC_2Dcode.setEnabled(0)


    ######### copy data ##########
    def func_readCopyData_JC_2Dcode(self):
        self.tmp_line58=self.var_dataSetting[58]
        self.tmp_line58=self.tmp_line58.rstrip()
        
        if len(self.tmp_line58) !=1:
            self.tmp_copyData=self.tmp_line58[2:len(self.tmp_line58)]
            self.tmp_copyData=self.tmp_copyData.rstrip()
            if (len(self.tmp_copyData)!=0):
                 self.var_Ui_JC_2Dcode.tedit_CopyReadData_JC_2Dcode.setPlainText(self.tmp_copyData)
        else :
            self.var_Ui_JC_2Dcode.tedit_CopyReadData_JC_2Dcode.setPlainText("")
    ########  convert Data #####
    def func_readConverData_JC_2Dcode(self):
        self.tmp_line59=self.var_dataSetting[59]
        self.tmp_line59=self.tmp_line59.rstrip()
        if len(self.tmp_line59) !=1:
            self.tmp_convertData=self.tmp_line59[2:len(self.tmp_line59)]
            self.tmp_convertData=self.tmp_convertData.rstrip()
            if (len(self.tmp_convertData)!=0):
                 self.var_Ui_JC_2Dcode.lab_Coverted_JC_2Dcode.setText(self.tmp_convertData)        
        else:
            self.var_Ui_JC_2Dcode.lab_Coverted_JC_2Dcode.setText("")  


    ########  collation result #####
    def func_readCollationResult_JC_2Dcode(self):
        self.tmp_line60=self.var_dataSetting[60]
        self.tmp_line60=self.tmp_line60.rstrip()
        if len(self.tmp_line60) !=1:
            self.tmp_collationresult = self.tmp_line60[2:len(self.tmp_line60)]
            self.tmp_collationresult = self.tmp_collationresult.rstrip()
            if (len(self.tmp_collationresult)!=0):
                 self.var_Ui_JC_2Dcode.lab_CollationResult_JC_2Dcode.setText(self.tmp_collationresult)  
        else :
             self.var_Ui_JC_2Dcode.lab_CollationResult_JC_2Dcode.setText("") 

    #### length datta  upper ########
    def func_readLengthDataUpper_JC_2Dcode(self):
        self.tmp_line61=self.var_dataSetting[61]
        self.tmp_line61=self.tmp_line61.rstrip()
        if len(self.tmp_line61) !=1:
            self.tmp_lengthDataUpper = self.tmp_line61[2:len(self.tmp_line61)]
            self.tmp_lengthDataUpper = self.tmp_lengthDataUpper.rstrip()
            if (len(self.tmp_lengthDataUpper)!=0):
                 self.var_Ui_JC_2Dcode.tedit_UpperLimit_Length_JC_2Dcode.setPlainText(self.tmp_lengthDataUpper)    
  #      else:
  #          self.var_Ui_JC_2Dcode.tedit_UpperLimit_Length_JC_2Dcode.setPlainText("")
    ###### length data measure #####
    def func_readLengthDataMeasure_JC_2Dcode(self):
        self.tmp_line62=self.var_dataSetting[62]
        self.tmp_line62=self.tmp_line62.rstrip()
        if len(self.tmp_line62) !=1:
            self.tmp_lengthDataMeasure = self.tmp_line62[2:len(self.tmp_line62)]
            self.tmp_lengthDataMeasure = self.tmp_lengthDataMeasure.rstrip()
            if (len(self.tmp_lengthDataMeasure)!=0):
                 self.var_Ui_JC_2Dcode.tedit_Measured_Length_JC_2Dcode.setPlainText(self.tmp_lengthDataMeasure)  
    ###### length data lower #####
    def func_readLengthDataLower_JC_2Dcode(self):
        self.tmp_line63=self.var_dataSetting[63]
        self.tmp_line63=self.tmp_line63.rstrip()
        if len(self.tmp_line63) !=1:
            self.tmp_lengthDataLower = self.tmp_line63[2:len(self.tmp_line63)]
            self.tmp_lengthDataLower = self.tmp_lengthDataLower.rstrip()
            if (len(self.tmp_lengthDataLower)!=0):
                 self.var_Ui_JC_2Dcode.tedit_LowerLimit_Length_JC_2Dcode.setPlainText(self.tmp_lengthDataLower)    
   #     else:
   #         self.var_Ui_JC_2Dcode.tedit_LowerLimit_Length_JC_2Dcode.setPlainText("")   
    ###### position X data upper #####
    def func_readPosXDataUpper_JC_2Dcode(self):
        self.tmp_line64=self.var_dataSetting[64]
        self.tmp_line64=self.tmp_line64.rstrip()
        if len(self.tmp_line64) !=1:
            self.tmp_PosXDataLower = self.tmp_line64[2:len(self.tmp_line64)]
            self.tmp_PosXDataLower = self.tmp_PosXDataLower.rstrip()
            if (len(self.tmp_PosXDataLower)!=0):
                 self.var_Ui_JC_2Dcode.tedit_UpperLimit_PosX_JC_2Dcode.setPlainText(self.tmp_PosXDataLower)   
  #      else:
   #         self.var_Ui_JC_2Dcode.tedit_UpperLimit_PosX_JC_2Dcode.setPlainText("") 

    ###### position Y data upper #####
    def func_readPosYDataUpper_JC_2Dcode(self):
        self.tmp_line65=self.var_dataSetting[65]
        self.tmp_line65=self.tmp_line65.rstrip()
        if len(self.tmp_line65) !=1:
            self.tmp_PosYDataLower = self.tmp_line65[2:len(self.tmp_line65)]
            self.tmp_PosYDataLower = self.tmp_PosYDataLower.rstrip()
            if (len(self.tmp_PosYDataLower)!=0):
                 self.var_Ui_JC_2Dcode.tedit_UpperLimit_PosY_JC_2Dcode.setPlainText(self.tmp_PosYDataLower)  

  #      else:
   #         self.var_Ui_JC_2Dcode.tedit_UpperLimit_PosY_JC_2Dcode.setPlainText("")

    ###### position X data measure #####
    def func_readPosXDataMeasure_JC_2Dcode(self):
        self.tmp_line66=self.var_dataSetting[66]
        self.tmp_line66=self.tmp_line66.rstrip()
        if len(self.tmp_line66) !=1:
            self.tmp_PosXDataMeasure = self.tmp_line66[2:len(self.tmp_line66)]
            self.tmp_PosXDataMeasure = self.tmp_PosXDataMeasure.rstrip()
            if (len(self.tmp_PosXDataMeasure)!=0):
                 self.var_Ui_JC_2Dcode.tedit_Measured_PosX_JC_2Dcode.setPlainText(self.tmp_PosXDataMeasure) 

    ###### position Y data measure #####
    def func_readPosYDataMeasure_JC_2Dcode(self):
        self.tmp_line67=self.var_dataSetting[67]
        self.tmp_line67=self.tmp_line67.rstrip()
        if len(self.tmp_line67) !=1:
            self.tmp_PosYDataMeasure = self.tmp_line67[2:len(self.tmp_line67)]
            self.tmp_PosYDataMeasure = self.tmp_PosYDataMeasure.rstrip()
            if (len(self.tmp_PosXDataMeasure)!=0):
                 self.var_Ui_JC_2Dcode.tedit_Measured_PosY_JC_2Dcode.setPlainText(self.tmp_PosYDataMeasure) 


    ###### position X data lower #####
    def func_readPosXDataLower_JC_2Dcode(self):
        self.tmp_line68=self.var_dataSetting[68]
        self.tmp_line68=self.tmp_line68.rstrip()
        if len(self.tmp_line68) !=1:
            self.tmp_PosXDataLower = self.tmp_line68[2:len(self.tmp_line68)]
            self.tmp_PosXDataLower = self.tmp_PosXDataLower.rstrip()
            if (len(self.tmp_PosXDataLower)!=0):
                 self.var_Ui_JC_2Dcode.tedit_LowerLimit_PosX_JC_2Dcode_2.setPlainText(self.tmp_PosXDataLower) 
   #     else:
    #        self.var_Ui_JC_2Dcode.tedit_LowerLimit_PosX_JC_2Dcode_2.setPlainText("") 
    ###### position Y data lower #####
    def func_readPosYDataLower_JC_2Dcode(self):
        self.tmp_line69=self.var_dataSetting[69]
        self.tmp_line69=self.tmp_line69.rstrip()
        if len(self.tmp_line69) !=1:
            self.tmp_PosYDataLower = self.tmp_line69[2:len(self.tmp_line69)]
            self.tmp_PosYDataLower = self.tmp_PosYDataLower.rstrip()
            if (len(self.tmp_PosYDataLower)!=0):
                 self.var_Ui_JC_2Dcode.tedit_LowerLimit_PosY_JC_2Dcode.setPlainText(self.tmp_PosYDataLower) 

  #      else:
  #          self.var_Ui_JC_2Dcode.tedit_LowerLimit_PosY_JC_2Dcode.setPlainText("") 

    ######   data angle upper #####
    def func_readDataAngleUpper_JC_2Dcode(self):
        self.tmp_line70=self.var_dataSetting[70]
        self.tmp_line70=self.tmp_line70.rstrip()
        if len(self.tmp_line70) !=1:
            self.tmp_DataAngleUpper = self.tmp_line70[2:len(self.tmp_line70)]
            self.tmp_DataAngleUpper = self.tmp_DataAngleUpper.rstrip()
            if (len(self.tmp_DataAngleUpper)!=0):
                 self.var_Ui_JC_2Dcode.tedit_UpperLimit_Angle_JC_2Dcode.setPlainText(self.tmp_DataAngleUpper)

   #     else:
     #       self.var_Ui_JC_2Dcode.tedit_UpperLimit_Angle_JC_2Dcode.setPlainText("")
    ######   data angle Measure #####
    def func_readDataAngleMeasure_JC_2Dcode(self):
        self.tmp_line71=self.var_dataSetting[71]
        self.tmp_line71=self.tmp_line71.rstrip()
        if len(self.tmp_line71) !=1:
            self.tmp_DataAngleMeasure = self.tmp_line71[2:len(self.tmp_line71)]
            self.tmp_DataAngleMeasure = self.tmp_DataAngleMeasure.rstrip()
            if (len(self.tmp_DataAngleMeasure)!=0):
                 self.var_Ui_JC_2Dcode.tedit_Measured_Angle_JC_2Dcode.setPlainText(self.tmp_DataAngleMeasure)



    ######   data angle lower #####
    def func_readDataAngleLower_JC_2Dcode(self):
        self.tmp_line72=self.var_dataSetting[72]
        self.tmp_line72=self.tmp_line72.rstrip()
        if len(self.tmp_line72) !=1:
            self.tmp_DataAngleLower = self.tmp_line72[2:len(self.tmp_line72)]
            self.tmp_DataAngleLower = self.tmp_DataAngleLower.rstrip()
            if (len(self.tmp_DataAngleLower)!=0):
                 self.var_Ui_JC_2Dcode.tedit_LowerLimit_Angle_JC_2Dcode.setPlainText(self.tmp_DataAngleLower)
   #     else:
    #        self.var_Ui_JC_2Dcode.tedit_LowerLimit_Angle_JC_2Dcode.setPlainText("")

########### ghi data  config ######################################
    def func_wirteData_JC_2Dcode(self):
        self.var_filedata = open(self.var_fileConfig, 'w')
        self.var_filedata.writelines(self.var_dataSetting)
        self.var_filedata.close()
    ###### condition single ############################
    def func_clickConditionSingle_JC_2Dcode(self):            
        self.var_dataSetting[54]="1 "+"1"+"\n"
        self.var_Ui_JC_2Dcode.cbox_Multiple_JC_2Dcode.setChecked(0)
        self.func_wirteData_JC_2Dcode()

    ###### condition Multiple ############################
    def func_clickConditionMultiple_JC_2Dcode(self):            
        self.var_dataSetting[55]="1 "+"1"+"\n"
        self.var_Ui_JC_2Dcode.cbox_Single_JC_2Dcode.setChecked(0)
        self.var_Ui_JC_2Dcode.btn_ConditionsList_JC_2Dcode(0)
        self.func_wirteData_JC_2Dcode()

    ###### Data range  ############################
    def func_changeDataRange_JC_2Dcode(self):
        self.var_dataRange=self.var_Ui_JC_2Dcode.combox_DataRange_JC_2Dcode.currentText()          
        self.var_dataSetting[56]="1 "+self.var_dataRange+"\n"
        self.func_wirteData_JC_2Dcode()


    ######### copy data ##################
    def func_clickCopyData_JC_2Dcode(self):

        self.var_line57=self.var_dataSetting[57]
        if len(self.var_line57)!=1:
            self.var_loadData =self.var_line57[2:len(self.var_line57)]
            self.var_loadData=self.var_loadData.rstrip()
          
            self.var_Ui_JC_2Dcode.tedit_CopyReadData_JC_2Dcode.setPlainText(self.var_loadData)
            self.var_dataSetting[58]="1 "+ self.var_loadData+"\n"
            self.var_Ui_JC_2Dcode.lab_Coverted_JC_2Dcode.setText(self.var_loadData)
            self.func_wirteData_JC_2Dcode()
            self.var_Ui_JC_2Dcode.lab_CollationResult_JC_2Dcode.setText("OK")
     
    def func_changeCopyData_JC_2Dcode(self):
        self.var_changeCopyData=self.var_Ui_JC_2Dcode.tedit_CopyReadData_JC_2Dcode.toPlainText()
        self.var_changeCopyData=self.var_changeCopyData.rstrip()
        self.var_dataSetting[58]="1 "+ self.var_changeCopyData+"\n"
        self.var_dataSetting[59]="1 "+ self.var_changeCopyData+"\n"
        self.var_line57=self.var_dataSetting[57]   
        if len(self.var_line57)!=1:
            self.var_loadData =self.var_line57[2:len(self.var_line57)]
            self.var_loadData=self.var_loadData.rstrip()

            if self.var_changeCopyData != self.var_loadData:
                self.var_dataSetting[60]="1 "+ "NG"+"\n"
                self.var_Ui_JC_2Dcode.lab_CollationResult_JC_2Dcode.setText("NG")
            else :
                self.var_Ui_JC_2Dcode.lab_CollationResult_JC_2Dcode.setText("OK")






        self.func_wirteData_JC_2Dcode()
        self.var_Ui_JC_2Dcode.lab_Coverted_JC_2Dcode.setText(self.var_changeCopyData)
        self.var_Ui_JC_2Dcode.lab_Coverted_JC_2Dcode.setStyleSheet("color: black")   

    def func_change_Upper_Lower(self):
        self.tmp_upperLength=self.var_Ui_JC_2Dcode.tedit_UpperLimit_Length_JC_2Dcode.toPlainText()
        self.tmp_lowerLength=self.var_Ui_JC_2Dcode.tedit_LowerLimit_Length_JC_2Dcode.toPlainText()   


        self.var_dataSetting[61]="1 "+ self.tmp_upperLength+"\n"
        self.var_dataSetting[63]="1 "+ self.tmp_lowerLength+"\n"


        self.tmp_upperPosX=self.var_Ui_JC_2Dcode.tedit_UpperLimit_PosX_JC_2Dcode.toPlainText()
        self.tmp_lowerPosX=self.var_Ui_JC_2Dcode.tedit_LowerLimit_PosX_JC_2Dcode_2.toPlainText() 

        self.var_dataSetting[64]="1 "+ self.tmp_upperPosX+"\n"
        self.var_dataSetting[68]="1 "+ self.tmp_lowerPosX+"\n"

        self.tmp_upperPosY=self.var_Ui_JC_2Dcode.tedit_UpperLimit_PosY_JC_2Dcode.toPlainText()
        self.tmp_lowerPosY=self.var_Ui_JC_2Dcode.tedit_LowerLimit_PosY_JC_2Dcode.toPlainText() 

        self.var_dataSetting[65]="1 "+ self.tmp_upperPosY+"\n"
        self.var_dataSetting[69]="1 "+ self.tmp_lowerPosY+"\n"

        self.tmp_upperAngle=self.var_Ui_JC_2Dcode.tedit_UpperLimit_Angle_JC_2Dcode.toPlainText()
        self.tmp_lowerAngle=self.var_Ui_JC_2Dcode.tedit_LowerLimit_Angle_JC_2Dcode.toPlainText() 
        

        self.var_dataSetting[70]="1 "+ self.tmp_upperAngle+"\n"
        self.var_dataSetting[72]="1 "+ self.tmp_lowerAngle+"\n"
        self.func_wirteData_JC_2Dcode()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= Class_DlogJC_2Dcode(None)
    mainWindow.show()
    sys.exit(app.exec_())
