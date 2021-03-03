from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from Detection_2DCode.DlogRDS.Ui_DlogRDS.I_DlogRDS_2Dcode import Ui_Class_DlogRDS_2Dcode
#from Ui_DlogRDS.I_DlogRDS_2Dcode import Ui_Class_DlogRDS_2Dcode
from Detection_2DCode.DlogRDS.DlogDSS.Main_Dlog_DSS_2Dcode import Class_DlogDSS_2Dcode
class Class_DlogRDS_2Dcode(QDialog):
    var_signal_RDS_2Dcode = pyqtSignal()
    def __init__(self, parent, *args):
        super(Class_DlogRDS_2Dcode, self).__init__(*args)
        self.var_Ui_RDS_2Dcode=Ui_Class_DlogRDS_2Dcode()
        self.var_Ui_RDS_2Dcode.setupUi(self)

        self.var_Ui_RDS_2Dcode.btn_OK_RDS_2Dcode.clicked.connect(self.func_createSignal_RDS_2Dcode)
        self.var_Ui_RDS_2Dcode.btn_Cancel_RDS_2Dcode.clicked.connect(self.func_createSignalCancel_RDS_2Dcode)
        self.var_Ui_RDS_2Dcode.btn_SplitSetting_RDS_2Dcode.clicked.connect(self.func_show_DSS_2Dcode)

######### Data slipt Setting ######
        self.var_class_DSS_2Dcode=Class_DlogDSS_2Dcode(None)


    ##### Start Digit #############
        self.var_Ui_RDS_2Dcode.tedit_StartDigit_RDS_2Dcode.textChanged.connect(self.func_changeStartDigit_RDS_2Dcode)

    ##### Data Length #############
        self.var_Ui_RDS_2Dcode.tedit_ReadDataLength_RDS_2Dcode.textChanged.connect(self.func_changeDataLength_RDS_2Dcode)


    ######## slipt Data ###########
        
        self.var_Ui_RDS_2Dcode.cbox_SplitData_RDS_2Dcode.stateChanged.connect(self.func_clickSplitData_RDS_2Dcode)
        
    ######## Output Length ########
        self.var_Ui_RDS_2Dcode.cbox_OutputLength_RDS_2Dcode.stateChanged.connect(self.func_clickOutputLength_RDS_2Dcode)
        self.var_Ui_RDS_2Dcode.tedit_FillingCharacter_RDS_2Dcode.textChanged.connect(self.func_changeOutputLength_RDS_2Dcode)
    
    ######## Call text error ########
        self.var_Ui_RDS_2Dcode.cbox_CallTextError_RDS_2Dcode.stateChanged.connect(self.func_clickCallTextError_RDS_2Dcode)
        self.var_Ui_RDS_2Dcode.tedit_TextCalled_RDS_2Dcode.textChanged.connect(self.func_changeCallTextError_RDS_2Dcode)

        
    ######## Output Identifier ################
        self.var_Ui_RDS_2Dcode.cbox_OutputIdentifier_RDS_2Dcode.stateChanged.connect(self.func_clickOutputIdentifier_RDS_2Dcode)

    ######## Ignore ###########################

        self.var_Ui_RDS_2Dcode.cbox_Ignore_RDS_2Dcode.stateChanged.connect(self.func_clickIgnore_RDS_2Dcode)
    ######## Ouput ###############################
        
        self.var_Ui_RDS_2Dcode.cbox_Output_RDS_2Dcode.stateChanged.connect(self.func_clickOutput_RDS_2Dcode)
  
        
        
    def func_getSignal_RDS_2Dcode(self):
        return self.var_signal_RDS_2Dcode
    def func_createSignal_RDS_2Dcode(self):
        self.var_signal_RDS_2Dcode.emit()
        #print(self.var_dataSetting)

    def func_createSignalCancel_RDS_2Dcode(self):

        self.var_fileData = open(self.var_fileConfig, 'w')
        self.var_fileData.writelines(self.var_dataSetting_or)
        self.var_fileData.close()
        self.close()


####### function slipt Data ##################
    def func_show_DSS_2Dcode(self):
        self.var_class_DSS_2Dcode.show()
        self.var_class_DSS_2Dcode.func_setConfigFile_DSS_2Dcode(self.var_fileConfig)
        self.var_class_DSS_2Dcode.func_readData_DSS_2Dcode()
  #  def func_close_DSS_2Dcode(self):

######## get file config ##########################################

    def func_setConfigFile_RDS_2Dcode(self,tmp_fileConfig):
        self.var_fileConfig=tmp_fileConfig

######## read config data #########################################


    def func_readData_RDS_2Dcode(self):
        self.var_fileData_or=open(self.var_fileConfig,"r")
        self.var_dataSetting_or=self.var_fileData_or.readlines()
        self.var_fileData_or.close()



        self.var_fileData=open(self.var_fileConfig,"r")
        self.var_dataSetting=self.var_fileData.readlines()
      #  print(self.var_dataSetting)
        self.func_readStartDigit_RDS_2Dcode()
        self.func_readDataLength_RDS_2Dcode()
        self.func_readSplitData_RDS_2Dcode()
        self.func_readOutputLength_RDS_2Dcode()
        self.func_readCallTextError_RDS_2Dcode()
        self.func_readOutputIdentifier_RDS_2Dcode()
        self.func_readIgnore_RDS_2Dcode()
        self.func_readOutput_RDS_2Dcode()
        
        
        


    def func_readStartDigit_RDS_2Dcode(self):
        self.tmp_line17=self.var_dataSetting[17]  
        self.tmp_line17=self.tmp_line17.rstrip()
        if len(self.tmp_line17)!=1:
 
            self.tmp_startDigit=self.tmp_line17[2:len(self.tmp_line17)]
            self.tmp_startDigit=self.tmp_startDigit.rstrip()
            self.var_Ui_RDS_2Dcode.tedit_StartDigit_RDS_2Dcode.setPlainText(self.tmp_startDigit)
        else :
            self.var_Ui_RDS_2Dcode.tedit_StartDigit_RDS_2Dcode.setPlainText("0")
            
    def func_readDataLength_RDS_2Dcode(self):
        self.tmp_line18=self.var_dataSetting[18]  
        self.tmp_line18=self.tmp_line18.rstrip()
        if len(self.tmp_line18)!=1:
 
            self.tmp_DataLength=self.tmp_line18[2:len(self.tmp_line18)]
            self.tmp_DataLength=self.tmp_DataLength.rstrip()
            self.var_Ui_RDS_2Dcode.tedit_ReadDataLength_RDS_2Dcode.setPlainText(self.tmp_DataLength)
        else :
            self.var_Ui_RDS_2Dcode.tedit_ReadDataLength_RDS_2Dcode.setPlainText("100")
            
    def func_readSplitData_RDS_2Dcode(self):
        self.tmp_line19=self.var_dataSetting[19]  
        self.tmp_line19=self.tmp_line19.rstrip()
      
        if len(self.tmp_line19)==1:
            self.var_Ui_RDS_2Dcode.btn_SplitSetting_RDS_2Dcode.setEnabled(False)
            self.var_Ui_RDS_2Dcode.cbox_SplitData_RDS_2Dcode.setChecked(0)

        else:
            self.tmp_splitData=self.tmp_line19[2]
            self.tmp_splitData=self.tmp_splitData.rstrip()
            if (self.tmp_splitData=="0"):        
                self.var_Ui_RDS_2Dcode.cbox_SplitData_RDS_2Dcode.setChecked(0)
            else :
                              
                self.var_Ui_RDS_2Dcode.cbox_SplitData_RDS_2Dcode.setChecked(1)
                self.var_Ui_RDS_2Dcode.btn_SplitSetting_RDS_2Dcode.setEnabled(True)


                
    def func_readOutputLength_RDS_2Dcode(self):
        self.tmp_line30=self.var_dataSetting[30]  
        self.tmp_line30=self.tmp_line30.rstrip()

        if len(self.tmp_line30)==1:
            self.var_Ui_RDS_2Dcode.tedit_FillingCharacter_RDS_2Dcode.setEnabled(False)
            self.var_Ui_RDS_2Dcode.tedit_FillingCharacter_RDS_2Dcode.setPlainText("-")
            self.var_Ui_RDS_2Dcode.tedit_FillingCharacter_RDS_2Dcode.setStyleSheet("background-color: white")
            self.var_Ui_RDS_2Dcode.cbox_OutputLength_RDS_2Dcode.setChecked(0)
        else:
            self.tmp_OutputLength=self.tmp_line30[2]
            self.tmp_OutputLength=self.tmp_OutputLength.rstrip()
            if (self.tmp_OutputLength=="0"):        
                self.var_Ui_RDS_2Dcode.cbox_OutputLength_RDS_2Dcode.setChecked(0)
            else :

                self.var_Ui_RDS_2Dcode.cbox_OutputLength_RDS_2Dcode.setChecked(1)
                self.tmp_OutputLength_Data=self.tmp_line30[4:len(self.tmp_line30)]
                self.tmp_OutputLength_Data=self.tmp_OutputLength_Data.rstrip()
                self.var_Ui_RDS_2Dcode.tedit_FillingCharacter_RDS_2Dcode.setPlainText(self.tmp_OutputLength_Data)
                self.var_Ui_RDS_2Dcode.tedit_FillingCharacter_RDS_2Dcode.setEnabled(True)        
            


    def func_readCallTextError_RDS_2Dcode(self):
        
        self.tmp_line31=self.var_dataSetting[31]  
        self.tmp_line31=self.tmp_line31.rstrip()

        if len(self.tmp_line31)==1:
            self.var_Ui_RDS_2Dcode.tedit_TextCalled_RDS_2Dcode.setEnabled(False)
            self.var_Ui_RDS_2Dcode.tedit_TextCalled_RDS_2Dcode.setPlainText("error")
            self.var_Ui_RDS_2Dcode.tedit_TextCalled_RDS_2Dcode.setStyleSheet("background-color: white")
            self.var_Ui_RDS_2Dcode.cbox_CallTextError_RDS_2Dcode.setChecked(0)
        else:
            self.tmp_callTextError=self.tmp_line31[2]
            self.tmp_callTextError=self.tmp_callTextError.rstrip()
            if (self.tmp_callTextError=="0"):        
                self.var_Ui_RDS_2Dcode.cbox_CallTextError_RDS_2Dcode.setChecked(0)
            else :
                
                self.var_Ui_RDS_2Dcode.cbox_CallTextError_RDS_2Dcode.setChecked(1)
                self.tmp_callTextError_Data=self.tmp_line31[4:len(self.tmp_line31)]
                self.tmp_callTextError_Data=self.tmp_callTextError_Data.rstrip()

                
                self.var_Ui_RDS_2Dcode.tedit_TextCalled_RDS_2Dcode.setPlainText(self.tmp_callTextError_Data)
                self.var_Ui_RDS_2Dcode.tedit_TextCalled_RDS_2Dcode.setEnabled(True)         


    def func_readOutputIdentifier_RDS_2Dcode(self):
        
        self.tmp_line32=self.var_dataSetting[32]  
        self.tmp_line32=self.tmp_line32.rstrip()

        if len(self.tmp_line32)!=1:
            self.tmp_outputIdentifier=self.tmp_line32[2]
            self.tmp_outputIdentifier=self.tmp_outputIdentifier.rstrip()
           
            if(self.tmp_outputIdentifier=="0"):
                self.var_Ui_RDS_2Dcode.cbox_OutputIdentifier_RDS_2Dcode.setChecked(0) 
            else :
                self.var_Ui_RDS_2Dcode.cbox_OutputIdentifier_RDS_2Dcode.setChecked(1) 
        else:
            self.var_Ui_RDS_2Dcode.cbox_OutputIdentifier_RDS_2Dcode.setChecked(0)



    def func_readIgnore_RDS_2Dcode(self):     
        self.tmp_line33=self.var_dataSetting[33]  
        self.tmp_line33=self.tmp_line31.rstrip()

        if len(self.tmp_line33)!=1:
            self.tmp_ignorer=self.tmp_line33[2]
            self.tmp_ignorer=self.tmp_ignorer.rstrip()           
            if(self.tmp_line33=="0"):
                self.var_Ui_RDS_2Dcode.cbox_Ignore_RDS_2Dcode.setChecked(0) 
            else :
                self.var_Ui_RDS_2Dcode.cbox_Ignore_RDS_2Dcode.setChecked(1)                 
        else :
            self.var_Ui_RDS_2Dcode.cbox_Ignore_RDS_2Dcode.setChecked(0)
    def func_readOutput_RDS_2Dcode(self):     
        self.tmp_line34=self.var_dataSetting[34]  
        self.tmp_line34=self.tmp_line34.rstrip()

        if len(self.tmp_line34)!=1:
            self.tmp_Output=self.tmp_line34[2]
            self.tmp_Output=self.tmp_Output.rstrip()            
            if(self.tmp_line34=="0"):
                self.var_Ui_RDS_2Dcode.cbox_Output_RDS_2Dcode.setChecked(0) 
            else :
                self.var_Ui_RDS_2Dcode.cbox_Output_RDS_2Dcode.setChecked(1) 
        else:
            self.var_Ui_RDS_2Dcode.cbox_Output_RDS_2Dcode.setChecked(0)

#########  write Data config ####################################        

    ######## write Start Digit ########
    def func_wirteData_RDS_2Dcode(self):
        self.var_fileData = open(self.var_fileConfig, 'w')
        self.var_fileData.writelines(self.var_dataSetting)
        self.var_fileData.close()

    
    def func_changeStartDigit_RDS_2Dcode(self):
        self.tmp_textStartDigit=self.var_Ui_RDS_2Dcode.tedit_StartDigit_RDS_2Dcode.toPlainText()
        self.tmp_textDataLength=self.var_Ui_RDS_2Dcode.tedit_ReadDataLength_RDS_2Dcode.toPlainText()
        self.var_dataSetting[17]="1 "+self.tmp_textStartDigit+"\n"
        self.tmp_line73=self.var_dataSetting[73]
        self.tmp_line73=self.tmp_line73.rstrip()
        if (len(self.tmp_line73)!=1):
           self.var_dataReaded=self.tmp_line73[3:len(self.tmp_line73)]
           if (self.tmp_textStartDigit!="" and self.tmp_textDataLength!=""):
               self.var_dataCut=self.var_dataReaded[int(self.tmp_textStartDigit):int(self.tmp_textStartDigit)+int(self.tmp_textDataLength)]
               self.var_dataSetting[57]="1 "+self.var_dataCut+"\n"


        self.func_wirteData_RDS_2Dcode()  
        
    def func_changeDataLength_RDS_2Dcode(self):
        self.tmp_textStartDigit=self.var_Ui_RDS_2Dcode.tedit_StartDigit_RDS_2Dcode.toPlainText()
        self.tmp_textDataLength=self.var_Ui_RDS_2Dcode.tedit_ReadDataLength_RDS_2Dcode.toPlainText()
        self.var_dataSetting[18]="1 "+self.tmp_textDataLength+"\n"


        self.tmp_line73=self.var_dataSetting[73]
        self.tmp_line73=self.tmp_line73.rstrip()
        if (len(self.tmp_line73)!=1):
           self.var_dataReaded=self.tmp_line73[2:len(self.tmp_line73)]
           if (self.tmp_textStartDigit!="" and self.tmp_textDataLength!=""):
               self.var_dataCut=self.var_dataReaded[int(self.tmp_textStartDigit):int(self.tmp_textStartDigit)+int(self.tmp_textDataLength)]
               self.var_dataSetting[57]="1 "+self.var_dataCut+"\n"

        self.func_wirteData_RDS_2Dcode()  

    #### split data ######
    def func_clickSplitData_RDS_2Dcode(self):
        if  self.var_Ui_RDS_2Dcode.cbox_SplitData_RDS_2Dcode.isChecked():
            self.var_dataSetting[19]="1 "+"1"+"\n"
            self.var_Ui_RDS_2Dcode.btn_SplitSetting_RDS_2Dcode.setEnabled(True)
            self.func_wirteData_RDS_2Dcode()
        else :
            self.var_dataSetting[19]="0"+"\n"
            self.var_Ui_RDS_2Dcode.btn_SplitSetting_RDS_2Dcode.setEnabled(False)
            self.func_wirteData_RDS_2Dcode()            

    #### output length ######
    def func_clickOutputLength_RDS_2Dcode(self):
        if  self.var_Ui_RDS_2Dcode.cbox_OutputLength_RDS_2Dcode.isChecked():    
            self.tmp_textOutputLength=self.var_Ui_RDS_2Dcode.tedit_FillingCharacter_RDS_2Dcode.toPlainText()
            self.var_dataSetting[30]="1 "+"1"+" "+self.tmp_textOutputLength+"\n"
            self.var_Ui_RDS_2Dcode.tedit_FillingCharacter_RDS_2Dcode.setEnabled(True)

            self.tmp_line57=self.var_dataSetting[57] 
            self.tmp_line57=self.tmp_line57.rstrip()
            if len(self.tmp_line57) !=1:
                self.tmp_dataReaded=self.tmp_line57[2:len(self.tmp_line57)]
                self.tmp_dataReaded=self.tmp_dataReaded.rstrip()
                if (len(self.tmp_dataReaded)!=0):
                    if self.tmp_dataReaded !="Khong phat hien":
                        self.tmp_textDataLength=self.var_Ui_RDS_2Dcode.tedit_ReadDataLength_RDS_2Dcode.toPlainText()
                        self.tmp_textDataLength.rstrip()
                        self.tmp_textDataLength=int(self.tmp_textDataLength)
                        for i in range(len(self.tmp_dataReaded ),self.tmp_textDataLength):
                            self.tmp_dataReaded=self.tmp_dataReaded+ self.tmp_textOutputLength
                        self.var_dataSetting[57]="1 "+self.tmp_dataReaded+"\n"
                        
            self.func_wirteData_RDS_2Dcode()




            
        else :
            self.var_dataSetting[30]="0"+"\n"
            self.var_Ui_RDS_2Dcode.tedit_FillingCharacter_RDS_2Dcode.setEnabled(False)
            self.tmp_line57=self.var_dataSetting[57] 
            self.tmp_dataReaded=self.tmp_line57[2:len(self.tmp_line57)]
            self.tmp_dataReaded=self.tmp_dataReaded.rstrip()
            if self.tmp_dataReaded !="Khong phat hien":
                self.tmp_line62=self.var_dataSetting[62] 
                self.tmp_lengthData=self.tmp_line62[2:len(self.tmp_line62)]
                self.tmp_lengthData=self.tmp_lengthData.rstrip()
                self.tmp_dataReaded_Config=self.tmp_dataReaded[0:int(self.tmp_lengthData)]
                self.var_dataSetting[57]="1 "+self.tmp_dataReaded_Config+"\n"
            self.func_wirteData_RDS_2Dcode()
            
    def func_changeOutputLength_RDS_2Dcode(self):
        if  self.var_Ui_RDS_2Dcode.cbox_OutputLength_RDS_2Dcode.isChecked():   
            self.tmp_textOutputLength=self.var_Ui_RDS_2Dcode.tedit_FillingCharacter_RDS_2Dcode.toPlainText()
            self.tmp_textOutputLength=self.tmp_textOutputLength.rstrip()
            
            if (self.tmp_textOutputLength!="-"):
                self.var_dataSetting[30]="1 "+"1"+" "+self.tmp_textOutputLength+"\n"
                self.func_wirteData_RDS_2Dcode()




            self.tmp_line57=self.var_dataSetting[57] 
            self.tmp_line57=self.tmp_line57.rstrip()
            if len(self.tmp_line57) !=1:
                    self.tmp_dataReaded=self.tmp_line57[2:len(self.tmp_line57)]
                    self.tmp_dataReaded=self.tmp_dataReaded.rstrip()
                #  print(self.tmp_dataReaded)
                    if (len(self.tmp_dataReaded)!=0):
                        if self.tmp_dataReaded !="Khong phat hien":
                            self.tmp_textDataLength=self.var_Ui_RDS_2Dcode.tedit_ReadDataLength_RDS_2Dcode.toPlainText()
                            self.tmp_textDataLength.rstrip()
                            self.tmp_textDataLength=int(self.tmp_textDataLength)
                            self.tmp_line62=self.var_dataSetting[62] 
                            self.tmp_lengthData=self.tmp_line62[2:len(self.tmp_line62)]
                            self.tmp_lengthData=self.tmp_lengthData.rstrip()
                            self.tmp_dataReaded_Config=self.tmp_dataReaded[0:int(self.tmp_lengthData)]

                            for i in range(int(self.tmp_lengthData),self.tmp_textDataLength):
                                self.tmp_dataReaded_Config=self.tmp_dataReaded_Config+ self.tmp_textOutputLength
                            
                            self.var_dataSetting[57]="1 "+self.tmp_dataReaded_Config+"\n"
        
                            self.func_wirteData_RDS_2Dcode()


            else :
                self.var_dataSetting[30]="0"+"\n"
                self.func_wirteData_RDS_2Dcode()



    #### CallText Error ######

        
    def func_clickCallTextError_RDS_2Dcode(self):
        if  self.var_Ui_RDS_2Dcode.cbox_CallTextError_RDS_2Dcode.isChecked():     
            self.tmp_textCallTextError=self.var_Ui_RDS_2Dcode.tedit_TextCalled_RDS_2Dcode.toPlainText()
            self.var_dataSetting[31]="1 "+"1"+" "+self.tmp_textCallTextError+"\n"
            self.var_Ui_RDS_2Dcode.tedit_TextCalled_RDS_2Dcode.setEnabled(True)
            self.func_wirteData_RDS_2Dcode()
        else:
         
            self.var_dataSetting[31]="0"+"\n"
            self.var_Ui_RDS_2Dcode.tedit_TextCalled_RDS_2Dcode.setEnabled(False)
            self.func_wirteData_RDS_2Dcode()

        
    def func_changeCallTextError_RDS_2Dcode(self):
      #  if  self.var_Ui_RDS_2Dcode.cbox_CallTextError_RDS_2Dcode.isChecked():          
        self.tmp_textCallTextError=self.var_Ui_RDS_2Dcode.tedit_TextCalled_RDS_2Dcode.toPlainText()

        self.tmp_textCallTextError=self.tmp_textCallTextError.rstrip()
        
        if (self.tmp_textCallTextError!="error"):
            self.var_dataSetting[31]="1 "+"1"+" "+self.tmp_textCallTextError+"\n"
        else:
            self.var_dataSetting[31]="0"+"\n"
            
        self.func_wirteData_RDS_2Dcode()

    ######## Output Identifier #######
    def func_clickOutputIdentifier_RDS_2Dcode(self):
        if  self.var_Ui_RDS_2Dcode.cbox_OutputIdentifier_RDS_2Dcode.isChecked():
            self.var_dataSetting[32]="1 "+"1"+" "+"\n"
            self.func_wirteData_RDS_2Dcode()
        else :
            self.var_dataSetting[32]="0"+"\n"
            self.func_wirteData_RDS_2Dcode()            
    ######## Ignore #######
    def func_clickIgnore_RDS_2Dcode(self):
        if  self.var_Ui_RDS_2Dcode.cbox_Ignore_RDS_2Dcode.isChecked():        
            self.var_dataSetting[33]="1 "+"1"+" "+"\n"
            self.func_wirteData_RDS_2Dcode()
        else:
            self.var_dataSetting[33]="0"+"\n"
            self.func_wirteData_RDS_2Dcode()
    ######## Output #######
    def func_clickOutput_RDS_2Dcode(self):
        if  self.var_Ui_RDS_2Dcode.cbox_Output_RDS_2Dcode.isChecked():         
            self.var_dataSetting[34]="1 "+"1"+" "+"\n"
            self.func_wirteData_RDS_2Dcode()

        else :
            self.var_dataSetting[34]="0"+"\n"
            self.func_wirteData_RDS_2Dcode()           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= Class_DlogRDS_2Dcode(None)
    mainWindow.show()
    sys.exit(app.exec_())
