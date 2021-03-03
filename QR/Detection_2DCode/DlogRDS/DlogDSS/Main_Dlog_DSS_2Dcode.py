from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from DlogRDS.DlogDSS.Ui_DlogDSS.I_DlogDSS_2Dcode import Ui_DlogDSS_2Dcocde


class Class_DlogDSS_2Dcode(QDialog):
    var_signal_DSS_2Dcode = pyqtSignal()
    var_signalCancel_DSS_2Dcode=pyqtSignal()
    def __init__(self, parent, *args):
        super(Class_DlogDSS_2Dcode, self).__init__(*args)
        self.var_Ui_DSS_2Dcode=Ui_DlogDSS_2Dcocde()
        self.var_Ui_DSS_2Dcode.setupUi(self)
        self.var_Ui_DSS_2Dcode.btn_OK_DSS_2Dcode.clicked.connect(self.func_createSignal_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.btn_Cancel_DSS_2Dcode.clicked.connect(self.func_createSignalCancel_DSS_2Dcode)
        
        self.var_screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0, int(0.5*self.var_screen.height()), self.var_screen.width(), int (0.5*self.var_screen.height()))


        self.var_Ui_DSS_2Dcode.cbox_SlipRange1_DSS_2Dcode.stateChanged.connect(self.func_clicked_sliptRange1_DSS_2Dcode)             
        self.var_Ui_DSS_2Dcode.ledit_dataLength1_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange1_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_startDigt1_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange1_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_dataLength1_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_startDigt1_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_readData1_DSS_2Dcode.setEnabled(False) 
   
        self.var_Ui_DSS_2Dcode.cbox_SlipRange2_DSS_2Dcode.stateChanged.connect(self.func_clicked_sliptRange2_DSS_2Dcode)    
        self.var_Ui_DSS_2Dcode.ledit_dataLength2_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange2_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_startDigt2_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange2_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_dataLength2_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_startDigt2_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_readData2_DSS_2Dcode.setEnabled(False) 


        self.var_Ui_DSS_2Dcode.cbox_SlipRange3_DSS_2Dcode.stateChanged.connect(self.func_clicked_sliptRange3_DSS_2Dcode)    
        self.var_Ui_DSS_2Dcode.ledit_dataLength3_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange3_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_startDigt3_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange3_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_dataLength3_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_startDigt3_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_readData3_DSS_2Dcode.setEnabled(False) 

        self.var_Ui_DSS_2Dcode.cbox_SlipRange4_DSS_2Dcode.stateChanged.connect(self.func_clicked_sliptRange4_DSS_2Dcode)    
        self.var_Ui_DSS_2Dcode.ledit_dataLength4_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange4_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_startDigt4_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange4_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_dataLength4_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_startDigt4_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_readData4_DSS_2Dcode.setEnabled(False) 



        self.var_Ui_DSS_2Dcode.cbox_SlipRange5_DSS_2Dcode.stateChanged.connect(self.func_clicked_sliptRange5_DSS_2Dcode)    
        self.var_Ui_DSS_2Dcode.ledit_dataLength5_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange5_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_startDigt5_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange5_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_dataLength5_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_startDigt5_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_readData5_DSS_2Dcode.setEnabled(False) 



        self.var_Ui_DSS_2Dcode.cbox_SlipRange6_DSS_2Dcode.stateChanged.connect(self.func_clicked_sliptRange6_DSS_2Dcode)    
        self.var_Ui_DSS_2Dcode.ledit_dataLength6_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange6_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_startDigt6_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange6_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_dataLength6_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_startDigt6_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_readData6_DSS_2Dcode.setEnabled(False) 



        self.var_Ui_DSS_2Dcode.cbox_SlipRange7_DSS_2Dcode.stateChanged.connect(self.func_clicked_sliptRange7_DSS_2Dcode)    
        self.var_Ui_DSS_2Dcode.ledit_dataLength7_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange7_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_startDigt7_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange7_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_dataLength7_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_startDigt7_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_readData7_DSS_2Dcode.setEnabled(False) 

        self.var_Ui_DSS_2Dcode.cbox_SlipRange8_DSS_2Dcode.stateChanged.connect(self.func_clicked_sliptRange8_DSS_2Dcode)    
        self.var_Ui_DSS_2Dcode.ledit_dataLength8_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange8_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_startDigt8_DSS_2Dcode.textChanged.connect(self.func_changeSliptRange8_DSS_2Dcode)
        self.var_Ui_DSS_2Dcode.ledit_dataLength8_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_startDigt8_DSS_2Dcode.setEnabled(False) 
        self.var_Ui_DSS_2Dcode.ledit_readData8_DSS_2Dcode.setEnabled(False) 


    def func_createSignal_DSS_2Dcode(self):
        self.var_signal_DSS_2Dcode.emit()
        self.close()
    def func_createSignalCancel_DSS_2Dcode(self):
        self.var_signalCancel_DSS_2Dcode.emit()
        self.var_fileData = open(self.var_fileConfig, 'w')
        self.var_fileData.writelines(self.var_dataSetting_or)
        self.var_fileData.close()


        self.close()
    
    def func_getSignal_DSS_2Dcode(self):
        return self.var_signal_DSS_2Dcode()
        
    def func_getSignal_DSS_2Dcode(self):
        return self.var_signalCancel_DSS_2Dcode


    def func_readData_DSS_2Dcode(self):
        self.var_fileData_or=open(self.var_fileConfig,"r")
        self.var_dataSetting_or=self.var_fileData_or.readlines()
        self.var_fileData_or.close()



        self.var_fileData=open(self.var_fileConfig,"r")
        self.var_dataSetting=self.var_fileData.readlines()  
        self.func_readDataReaded_DSS_2Dcode()
        self.func_readSplitData1_DSS_2Dcode()
        self.func_readSplitData2_DSS_2Dcode()
        self.func_readSplitData3_DSS_2Dcode()
        self.func_readSplitData4_DSS_2Dcode()
        self.func_readSplitData5_DSS_2Dcode()
        self.func_readSplitData6_DSS_2Dcode()
        self.func_readSplitData7_DSS_2Dcode()
        self.func_readSplitData8_DSS_2Dcode()

    def func_readDataReaded_DSS_2Dcode(self):
        self.line57=self.var_dataSetting[57]
        if (len(self.line57)!=1 ):
            self.var_datareaded=self.line57[2:len(self.line57)]
            self.var_datareaded=self.var_datareaded.rstrip()
            if (self.var_datareaded!="Khong phat hien"):
                self.var_Ui_DSS_2Dcode.lab_ReadData__DSS_2Dcode.setText(self.var_datareaded)

    def func_readSplitData1_DSS_2Dcode(self):
        self.line20=self.var_dataSetting[20]

        if (len(self.line20)!=2):
            self.var_Ui_DSS_2Dcode.cbox_SlipRange1_DSS_2Dcode.setChecked(1)
            tmp_startData1=""
            tmp_pos1=0
            

            for i in range (2,len(self.line20)):
                tmp_startData1=tmp_startData1+self.line20[i]
                if (self.line20[i]==" "):
                    tmp_pos1=i
                    break
            self.var_Ui_DSS_2Dcode.ledit_startDigt1_DSS_2Dcode.setText(tmp_startData1)
            tmp_startData1=int(tmp_startData1)
            tmp_lengthDataslip1=self.line20[tmp_pos1+1:len(self.line20)-1]
            tmp_lengthDataslip1=tmp_lengthDataslip1.rstrip()
            self.var_Ui_DSS_2Dcode.ledit_dataLength1_DSS_2Dcode.setText(tmp_lengthDataslip1)
            tmp_lengthDataslip1=int(tmp_lengthDataslip1)
            if (tmp_lengthDataslip1<len(self.var_datareaded)-tmp_startData1):
                tmp_dataReaded1=self.var_datareaded[tmp_startData1:tmp_startData1+tmp_lengthDataslip1]
            else :
                tmp_dataReaded1=self.var_datareaded[tmp_startData1:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData1_DSS_2Dcode.setText(tmp_dataReaded1)
        else :
            self.var_Ui_DSS_2Dcode.ledit_dataLength1_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt1_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData1_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.cbox_SlipRange1_DSS_2Dcode.setChecked(0)

    def func_readSplitData2_DSS_2Dcode(self):
        self.line21=self.var_dataSetting[21]
        if (len(self.line21)!=2):
            self.var_Ui_DSS_2Dcode.cbox_SlipRange2_DSS_2Dcode.setChecked(1)
            tmp_startData2=""
            tmp_pos2=0
            for i in range (2,len(self.line21)):
                tmp_startData2=tmp_startData2+self.line21[i]
                if (self.line21[i]==" "):
                    tmp_pos2=i
                    break
            self.var_Ui_DSS_2Dcode.ledit_startDigt2_DSS_2Dcode.setText(tmp_startData2)
            tmp_startData2=int(tmp_startData2)
            tmp_lengthDataslip2=self.line21[tmp_pos2+1:len(self.line21)-1]
            tmp_lengthDataslip2=tmp_lengthDataslip2.rstrip()
            self.var_Ui_DSS_2Dcode.ledit_dataLength2_DSS_2Dcode.setText(tmp_lengthDataslip2)
            tmp_lengthDataslip2=int(tmp_lengthDataslip2)
            if (tmp_lengthDataslip2<len(self.var_datareaded)-tmp_startData2):
                tmp_dataReaded2=self.var_datareaded[tmp_startData2:tmp_startData2+tmp_lengthDataslip2]
            else :
                tmp_dataReaded2=self.var_datareaded[tmp_startData2:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData2_DSS_2Dcode.setText(tmp_dataReaded2)
        else :
            self.var_Ui_DSS_2Dcode.ledit_dataLength2_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt2_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData2_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.cbox_SlipRange2_DSS_2Dcode.setChecked(0)


    def func_readSplitData3_DSS_2Dcode(self):
        self.line22=self.var_dataSetting[22]
        if (len(self.line22)!=2):
            self.var_Ui_DSS_2Dcode.cbox_SlipRange3_DSS_2Dcode.setChecked(1)
            tmp_startData3=""
            tmp_pos3=0
            for i in range (2,len(self.line22)):
                tmp_startData3=tmp_startData3+self.line22[i]
                if (self.line22[i]==" "):
                    tmp_pos3=i
                    break
            self.var_Ui_DSS_2Dcode.ledit_startDigt3_DSS_2Dcode.setText(tmp_startData3)
            tmp_startData3=int(tmp_startData3)
            tmp_lengthDataslip3=self.line22[tmp_pos3+1:len(self.line22)-1]
            tmp_lengthDataslip3=tmp_lengthDataslip3.rstrip()
            self.var_Ui_DSS_2Dcode.ledit_dataLength3_DSS_2Dcode.setText(tmp_lengthDataslip3)
            tmp_lengthDataslip3=int(tmp_lengthDataslip3)
            if (tmp_lengthDataslip3<len(self.var_datareaded)-tmp_startData3):
                tmp_dataReaded3=self.var_datareaded[tmp_startData3:tmp_startData3+tmp_lengthDataslip3]
            else :
                tmp_dataReaded3=self.var_datareaded[tmp_startData3:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData3_DSS_2Dcode.setText(tmp_dataReaded3)

        else :
            self.var_Ui_DSS_2Dcode.ledit_dataLength3_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt3_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData3_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.cbox_SlipRange3_DSS_2Dcode.setChecked(0)


    def func_readSplitData4_DSS_2Dcode(self):
        self.line23=self.var_dataSetting[23]
        if (len(self.line23)!=2):
            self.var_Ui_DSS_2Dcode.cbox_SlipRange4_DSS_2Dcode.setChecked(1)
            tmp_startData4=""
            tmp_pos4=0
            for i in range (2,len(self.line23)):
                tmp_startData4=tmp_startData4+self.line23[i]
                if (self.line23[i]==" "):
                    tmp_pos4=i
                    break
            self.var_Ui_DSS_2Dcode.ledit_startDigt4_DSS_2Dcode.setText(tmp_startData4)
            tmp_startData4=int(tmp_startData4)
            tmp_lengthDataslip4=self.line23[tmp_pos4+1:len(self.line23)-1]
            tmp_lengthDataslip4=tmp_lengthDataslip4.rstrip()
            self.var_Ui_DSS_2Dcode.ledit_dataLength4_DSS_2Dcode.setText(tmp_lengthDataslip4)
            tmp_lengthDataslip4=int(tmp_lengthDataslip4)
            if (tmp_lengthDataslip4<len(self.var_datareaded)-tmp_startData4):
                tmp_dataReaded4=self.var_datareaded[tmp_startData4:tmp_startData4+tmp_lengthDataslip4]
            else :
                tmp_dataReaded4=self.var_datareaded[tmp_startData4:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData4_DSS_2Dcode.setText(tmp_dataReaded4)

        else :
            self.var_Ui_DSS_2Dcode.ledit_dataLength4_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt4_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData4_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.cbox_SlipRange4_DSS_2Dcode.setChecked(0)


    def func_readSplitData5_DSS_2Dcode(self):
        self.line24=self.var_dataSetting[24]
        if (len(self.line24)!=2):
            self.var_Ui_DSS_2Dcode.cbox_SlipRange5_DSS_2Dcode.setChecked(1)
            tmp_startData5=""
            tmp_pos5=0
            for i in range (2,len(self.line24)):
                tmp_startData5=tmp_startData5+self.line24[i]
                if (self.line24[i]==" "):
                    tmp_pos5=i
                    break
            self.var_Ui_DSS_2Dcode.ledit_startDigt5_DSS_2Dcode.setText(tmp_startData5)
            tmp_startData5=int(tmp_startData5)
            tmp_lengthDataslip5=self.line23[tmp_pos5+1:len(self.line24)-1]
            tmp_lengthDataslip5=tmp_lengthDataslip5.rstrip()
            self.var_Ui_DSS_2Dcode.ledit_dataLength5_DSS_2Dcode.setText(tmp_lengthDataslip5)
            tmp_lengthDataslip5=int(tmp_lengthDataslip5)
            if (tmp_lengthDataslip5<len(self.var_datareaded)-tmp_startData5):
                tmp_dataReaded5=self.var_datareaded[tmp_startData5:tmp_startData5+tmp_lengthDataslip5]
            else :
                tmp_dataReaded5=self.var_datareaded[tmp_startData5:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData5_DSS_2Dcode.setText(tmp_dataReaded5)

        else :
            self.var_Ui_DSS_2Dcode.ledit_dataLength5_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt5_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData5_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.cbox_SlipRange5_DSS_2Dcode.setChecked(0)
    def func_readSplitData6_DSS_2Dcode(self):
        self.line25=self.var_dataSetting[25]
        if (len(self.line25)!=2):
            self.var_Ui_DSS_2Dcode.cbox_SlipRange6_DSS_2Dcode.setChecked(1)
            tmp_startData6=""
            tmp_pos6=0
            for i in range (2,len(self.line25)):
                tmp_startData6=tmp_startData6+self.line25[i]
                if (self.line25[i]==" "):
                    tmp_pos6=i
                    break
            self.var_Ui_DSS_2Dcode.ledit_startDigt6_DSS_2Dcode.setText(tmp_startData6)
            tmp_startData6=int(tmp_startData6)
            tmp_lengthDataslip6=self.line23[tmp_pos6+1:len(self.line25)-1]
            tmp_lengthDataslip6=tmp_lengthDataslip6.rstrip()
            self.var_Ui_DSS_2Dcode.ledit_dataLength6_DSS_2Dcode.setText(tmp_lengthDataslip6)
            tmp_lengthDataslip6=int(tmp_lengthDataslip6)
            if (tmp_lengthDataslip6<len(self.var_datareaded)-tmp_startData6):
                tmp_dataReaded6=self.var_datareaded[tmp_startData6:tmp_startData6+tmp_lengthDataslip6]
            else :
                tmp_dataReaded6=self.var_datareaded[tmp_startData6:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData6_DSS_2Dcode.setText(tmp_dataReaded6)
        else :
            self.var_Ui_DSS_2Dcode.ledit_dataLength6_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt6_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData6_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.cbox_SlipRange6_DSS_2Dcode.setChecked(0)
    def func_readSplitData7_DSS_2Dcode(self):
        self.line26=self.var_dataSetting[26]
        if (len(self.line26)!=2):
            self.var_Ui_DSS_2Dcode.cbox_SlipRange7_DSS_2Dcode.setChecked(1)
            tmp_startData7=""
            tmp_pos7=0
            for i in range (2,len(self.line26)):
                tmp_startData7=tmp_startData7+self.line26[i]
                if (self.line26[i]==" "):
                    tmp_pos7=i
                    break
            self.var_Ui_DSS_2Dcode.ledit_startDigt7_DSS_2Dcode.setText(tmp_startData7)
            tmp_startData7=int(tmp_startData7)
            tmp_lengthDataslip7=self.line23[tmp_pos7+1:len(self.line26)-1]
            tmp_lengthDataslip7=tmp_lengthDataslip7.rstrip()
            self.var_Ui_DSS_2Dcode.ledit_dataLength7_DSS_2Dcode.setText(tmp_lengthDataslip7)
            tmp_lengthDataslip7=int(tmp_lengthDataslip7)
            if (tmp_lengthDataslip7<len(self.var_datareaded)-tmp_startData7):
                tmp_dataReaded7=self.var_datareaded[tmp_startData7:tmp_startData7+tmp_lengthDataslip7]
            else :
                tmp_dataReaded7=self.var_datareaded[tmp_startData7:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData7_DSS_2Dcode.setText(tmp_dataReaded7)
        else :
            self.var_Ui_DSS_2Dcode.ledit_dataLength7_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt7_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData7_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.cbox_SlipRange7_DSS_2Dcode.setChecked(0)

    def func_readSplitData8_DSS_2Dcode(self):
        self.line27=self.var_dataSetting[27]
        if (len(self.line27)!=2):
            self.var_Ui_DSS_2Dcode.cbox_SlipRange8_DSS_2Dcode.setChecked(1)
            tmp_startData8=""
            tmp_pos8=0
            for i in range (2,len(self.line27)):
                tmp_startData8=tmp_startData8+self.line27[i]
                if (self.line27[i]==" "):
                    tmp_pos8=i
                    break
            self.var_Ui_DSS_2Dcode.ledit_startDigt8_DSS_2Dcode.setText(tmp_startData8)
            tmp_startData8=int(tmp_startData8)
            tmp_lengthDataslip8=self.line23[tmp_pos8+1:len(self.line27)-1]
            tmp_lengthDataslip8=tmp_lengthDataslip8.rstrip()
            self.var_Ui_DSS_2Dcode.ledit_dataLength8_DSS_2Dcode.setText(tmp_lengthDataslip8)
            tmp_lengthDataslip8=int(tmp_lengthDataslip8)
            if (tmp_lengthDataslip8<len(self.var_datareaded)-tmp_startData8):
                tmp_dataReaded8=self.var_datareaded[tmp_startData8:tmp_startData8+tmp_lengthDataslip8]
            else :
                tmp_dataReaded8=self.var_datareaded[tmp_startData8:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData8_DSS_2Dcode.setText(tmp_dataReaded8)
        else :
            self.var_Ui_DSS_2Dcode.ledit_dataLength8_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt8_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData8_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.cbox_SlipRange8_DSS_2Dcode.setChecked(0)
########## write data  to cofig #############################################
    def func_wirteData_DSS_2Dcode(self):
        self.var_fileData = open(self.var_fileConfig, 'w')
        self.var_fileData.writelines(self.var_dataSetting)
        self.var_fileData.close()
    ###############  slipt 1 #######################
    def func_clicked_sliptRange1_DSS_2Dcode(self):
        if  self.var_Ui_DSS_2Dcode.cbox_SlipRange1_DSS_2Dcode.isChecked():

            self.var_Ui_DSS_2Dcode.ledit_dataLength1_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt1_DSS_2Dcode.setEnabled(True)
            self.var_Ui_DSS_2Dcode.ledit_readData1_DSS_2Dcode.setEnabled(True)  


            self.tmp_line17=self.var_dataSetting[17]  
            self.tmp_line17=self.tmp_line17.rstrip()
            tmp_startData1=self.tmp_line17[2:len(self.tmp_line17)]
            self.tmp_line18=self.var_dataSetting[18]  
            self.tmp_line18=self.tmp_line18.rstrip()
            tmp_lengthDataslip1=self.tmp_line18[2:len(self.tmp_line18)]
            self.var_Ui_DSS_2Dcode.ledit_startDigt1_DSS_2Dcode.setText(tmp_startData1)
            self.var_Ui_DSS_2Dcode.ledit_dataLength1_DSS_2Dcode.setText(tmp_lengthDataslip1)
            tmp_startData1=self.var_Ui_DSS_2Dcode.ledit_startDigt1_DSS_2Dcode.text()
            tmp_lengthDataslip1=self.var_Ui_DSS_2Dcode.ledit_dataLength1_DSS_2Dcode.text()       
            self.var_dataSetting[20]="1 "+tmp_startData1+" "+tmp_lengthDataslip1+"\n"
           

            tmp_startData1=int(tmp_startData1)
            tmp_lengthDataslip1=int(tmp_lengthDataslip1)
    

            if (tmp_lengthDataslip1<len(self.var_datareaded)-tmp_startData1):
                    tmp_dataReaded1=self.var_datareaded[tmp_startData1:tmp_startData1+tmp_lengthDataslip1]
            else :
                    tmp_dataReaded1=self.var_datareaded[tmp_startData1:len(self.var_datareaded)]
            
            self.var_Ui_DSS_2Dcode.ledit_readData1_DSS_2Dcode.setText(tmp_dataReaded1)
        else:
            self.var_Ui_DSS_2Dcode.ledit_dataLength1_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt1_DSS_2Dcode.setEnabled(False)
            self.var_Ui_DSS_2Dcode.ledit_readData1_DSS_2Dcode.setEnabled(False) 
            self.var_dataSetting[20]="0"+"\n"
        self.func_wirteData_DSS_2Dcode()
    def func_changeSliptRange1_DSS_2Dcode(self):
        self.tmp_startData1=str(self.var_Ui_DSS_2Dcode.ledit_startDigt1_DSS_2Dcode.text())
        self.tmp_lengthDataslip1=str(self.var_Ui_DSS_2Dcode.ledit_dataLength1_DSS_2Dcode.text())
   
        self.tmp_startData1=self.tmp_startData1.rstrip()        
        self.tmp_lengthDataslip1=self.tmp_lengthDataslip1.rstrip()
        self.var_dataSetting[20]="1 "+self.tmp_startData1+" "+ self.tmp_lengthDataslip1+"\n"
    
        self.func_wirteData_DSS_2Dcode()
        if (self.tmp_startData1!="" and self.tmp_lengthDataslip1!=""):
            self.tmp_startData1=int(self.tmp_startData1)
            self.tmp_lengthDataslip10=int(self.tmp_lengthDataslip1)

            if (self.tmp_lengthDataslip10<len(self.var_datareaded)-self.tmp_startData1):
                    self.tmp_dataReaded1=self.var_datareaded[self.tmp_startData1:self.tmp_startData1+self.tmp_lengthDataslip10]
            else :
                    self.tmp_dataReaded1=self.var_datareaded[self.tmp_startData1:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData1_DSS_2Dcode.setText(self.tmp_dataReaded1)


    ########         slipt2     #################################################

    def func_clicked_sliptRange2_DSS_2Dcode(self):

        if  self.var_Ui_DSS_2Dcode.cbox_SlipRange2_DSS_2Dcode.isChecked():

            self.var_Ui_DSS_2Dcode.ledit_dataLength2_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt2_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_readData2_DSS_2Dcode.setEnabled(True) 


            self.tmp_line17=self.var_dataSetting[17]  
            self.tmp_line17=self.tmp_line17.rstrip()
            tmp_startData2=self.tmp_line17[2:len(self.tmp_line17)]
            self.tmp_line18=self.var_dataSetting[18]  
            self.tmp_line18=self.tmp_line18.rstrip()
            tmp_lengthDataslip2=self.tmp_line18[2:len(self.tmp_line18)]
            self.var_Ui_DSS_2Dcode.ledit_startDigt2_DSS_2Dcode.setText(tmp_startData2)
            self.var_Ui_DSS_2Dcode.ledit_dataLength2_DSS_2Dcode.setText(tmp_lengthDataslip2)
            tmp_startData2=self.var_Ui_DSS_2Dcode.ledit_startDigt2_DSS_2Dcode.text()
            tmp_lengthDataslip2=self.var_Ui_DSS_2Dcode.ledit_dataLength2_DSS_2Dcode.text()

            
            
            self.var_dataSetting[21]="1 "+tmp_startData2+" "+tmp_lengthDataslip2+"\n"
#            self.func_wirteData_DSS_2Dcode()
            tmp_startData2=int(tmp_startData2)
            tmp_lengthDataslip2=int(tmp_lengthDataslip2)

            if (tmp_lengthDataslip2<len(self.var_datareaded)-tmp_startData2):
                    tmp_dataReaded2=self.var_datareaded[tmp_startData2:tmp_startData2+tmp_lengthDataslip2]
            else :
                    tmp_dataReaded2=self.var_datareaded[tmp_startData2:len(self.var_datareaded)]
            self.var_Ui_DSS_2Dcode.ledit_readData2_DSS_2Dcode.setText(tmp_dataReaded2)
        else:
            self.var_Ui_DSS_2Dcode.ledit_dataLength2_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt2_DSS_2Dcode.setEnabled(False)  
            self.var_Ui_DSS_2Dcode.ledit_readData2_DSS_2Dcode.setEnabled(False) 
            self.var_dataSetting[21]="0"+"\n"
        self.func_wirteData_DSS_2Dcode()
    def func_changeSliptRange2_DSS_2Dcode(self):
        tmp_startData2=self.var_Ui_DSS_2Dcode.ledit_startDigt2_DSS_2Dcode.text()
        tmp_lengthDataslip2=self.var_Ui_DSS_2Dcode.ledit_dataLength2_DSS_2Dcode.text()

        tmp_startData2=tmp_startData2.rstrip()        
        tmp_lengthDataslip2=tmp_lengthDataslip2.rstrip()
        self.var_dataSetting[21]="1 "+tmp_startData2+" "+tmp_lengthDataslip2+"\n"
        self.func_wirteData_DSS_2Dcode()
        if (tmp_lengthDataslip2!="" and tmp_startData2!=""):
            tmp_startData2=int(tmp_startData2)
            tmp_lengthDataslip2=int(tmp_lengthDataslip2)
            if (tmp_lengthDataslip2<len(self.var_datareaded)-tmp_startData2):
                    tmp_dataReaded2=self.var_datareaded[tmp_startData2:tmp_startData2+tmp_lengthDataslip2]
            else :
                    tmp_dataReaded2=self.var_datareaded[tmp_startData2:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData2_DSS_2Dcode.setText(tmp_dataReaded2)


    ########         slipt 3     #################################################

    def func_clicked_sliptRange3_DSS_2Dcode(self):
        if  self.var_Ui_DSS_2Dcode.cbox_SlipRange3_DSS_2Dcode.isChecked():

            self.var_Ui_DSS_2Dcode.ledit_dataLength3_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt3_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_readData3_DSS_2Dcode.setEnabled(True) 

            self.tmp_line17=self.var_dataSetting[17]  
            self.tmp_line17=self.tmp_line17.rstrip()
            tmp_startData3=self.tmp_line17[2:len(self.tmp_line17)]
            self.tmp_line18=self.var_dataSetting[18]  
            self.tmp_line18=self.tmp_line18.rstrip()
            tmp_lengthDataslip3=self.tmp_line18[2:len(self.tmp_line18)]
            self.var_Ui_DSS_2Dcode.ledit_startDigt3_DSS_2Dcode.setText(tmp_startData3)
            self.var_Ui_DSS_2Dcode.ledit_dataLength3_DSS_2Dcode.setText(tmp_lengthDataslip3)
            tmp_startData3=self.var_Ui_DSS_2Dcode.ledit_startDigt3_DSS_2Dcode.text()
            tmp_lengthDataslip3=self.var_Ui_DSS_2Dcode.ledit_dataLength3_DSS_2Dcode.text()

            
            
            self.var_dataSetting[22]="1 "+tmp_startData3+" "+tmp_lengthDataslip3+"\n"
     #       self.func_wirteData_DSS_2Dcode()
            tmp_startData3=int(tmp_startData3)
            tmp_lengthDataslip3=int(tmp_lengthDataslip3)

            if (tmp_lengthDataslip3<len(self.var_datareaded)-tmp_startData3):
                    tmp_dataReaded3=self.var_datareaded[tmp_startData3:tmp_startData3+tmp_lengthDataslip3]
            else :
                    tmp_dataReaded3=self.var_datareaded[tmp_startData3:len(self.var_datareaded)]
                    
            self.var_Ui_DSS_2Dcode.ledit_readData3_DSS_2Dcode.setText(tmp_dataReaded3)
        else:
            self.var_Ui_DSS_2Dcode.ledit_dataLength3_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt3_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData3_DSS_2Dcode.setEnabled(False)  
            self.var_dataSetting[22]="0"+"\n"
        self.func_wirteData_DSS_2Dcode()

    def func_changeSliptRange3_DSS_2Dcode(self):



        tmp_startData3=self.var_Ui_DSS_2Dcode.ledit_startDigt3_DSS_2Dcode.text()
        tmp_lengthDataslip3=self.var_Ui_DSS_2Dcode.ledit_dataLength3_DSS_2Dcode.text()
        tmp_startData3=tmp_startData3.rstrip()        
        tmp_lengthDataslip3=tmp_lengthDataslip3.rstrip()
        self.var_dataSetting[22]="1 "+tmp_startData3+" "+tmp_lengthDataslip3+"\n"
        self.func_wirteData_DSS_2Dcode()
        if (tmp_lengthDataslip3!="" and tmp_startData3!=""):
            tmp_startData3=int(tmp_startData3)
            tmp_lengthDataslip3=int(tmp_lengthDataslip3)
            if (tmp_lengthDataslip3<len(self.var_datareaded)-tmp_startData3):
                    tmp_dataReaded3=self.var_datareaded[tmp_startData3:tmp_startData3+tmp_lengthDataslip3]
            else :
                    tmp_dataReaded3=self.var_datareaded[tmp_startData3:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData3_DSS_2Dcode.setText(tmp_dataReaded3)




    ########         slipt 4     #################################################

    def func_clicked_sliptRange4_DSS_2Dcode(self):

        if  self.var_Ui_DSS_2Dcode.cbox_SlipRange4_DSS_2Dcode.isChecked():

            self.var_Ui_DSS_2Dcode.ledit_dataLength4_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt4_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_readData4_DSS_2Dcode.setEnabled(True) 
            self.tmp_line17=self.var_dataSetting[17]  
            self.tmp_line17=self.tmp_line17.rstrip()
            tmp_startData4=self.tmp_line17[2:len(self.tmp_line17)]
            self.tmp_line18=self.var_dataSetting[18]  
            self.tmp_line18=self.tmp_line18.rstrip()
            tmp_lengthDataslip4=self.tmp_line18[2:len(self.tmp_line18)]
            self.var_Ui_DSS_2Dcode.ledit_startDigt4_DSS_2Dcode.setText(tmp_startData4)
            self.var_Ui_DSS_2Dcode.ledit_dataLength4_DSS_2Dcode.setText(tmp_lengthDataslip4)
            tmp_startData4=self.var_Ui_DSS_2Dcode.ledit_startDigt4_DSS_2Dcode.text()
            tmp_lengthDataslip4=self.var_Ui_DSS_2Dcode.ledit_dataLength4_DSS_2Dcode.text() 
            self.var_dataSetting[23]="1 "+tmp_startData4+" "+tmp_lengthDataslip4+"\n"
#            self.func_wirteData_DSS_2Dcode()
            tmp_startData4=int(tmp_startData4)
            tmp_lengthDataslip4=int(tmp_lengthDataslip4)

            if (tmp_lengthDataslip4<len(self.var_datareaded)-tmp_startData4):
                    tmp_dataReaded4=self.var_datareaded[tmp_startData4:tmp_startData4+tmp_lengthDataslip4]
            else :
                    tmp_dataReaded4=self.var_datareaded[tmp_startData4:len(self.var_datareaded)]
            self.var_Ui_DSS_2Dcode.ledit_readData4_DSS_2Dcode.setText(tmp_dataReaded4)

        else:
            self.var_Ui_DSS_2Dcode.ledit_dataLength4_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt4_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData4_DSS_2Dcode.setEnabled(False) 
            self.var_dataSetting[23]="0"+"\n" 

        self.func_wirteData_DSS_2Dcode()




    def func_changeSliptRange4_DSS_2Dcode(self):
        tmp_startData4=self.var_Ui_DSS_2Dcode.ledit_startDigt4_DSS_2Dcode.text()
        tmp_lengthDataslip4=self.var_Ui_DSS_2Dcode.ledit_dataLength4_DSS_2Dcode.text()
        tmp_startData4=tmp_startData4.rstrip()        
        tmp_lengthDataslip4=tmp_lengthDataslip4.rstrip()
        self.var_dataSetting[23]="1 "+tmp_startData4+" "+tmp_lengthDataslip4+"\n"
        self.func_wirteData_DSS_2Dcode()
        if (tmp_lengthDataslip4!="" and tmp_startData4!=""):
            tmp_startData4=int(tmp_startData4)
            tmp_lengthDataslip4=int(tmp_lengthDataslip4)
            if (tmp_lengthDataslip4<len(self.var_datareaded)-tmp_startData4):
                    tmp_dataReaded4=self.var_datareaded[tmp_startData4:tmp_startData4+tmp_lengthDataslip4]
            else :
                    tmp_dataReaded4=self.var_datareaded[tmp_startData4:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData4_DSS_2Dcode.setText(tmp_dataReaded4)



    ########         slipt 5     #################################################

    def func_clicked_sliptRange5_DSS_2Dcode(self):

        if  self.var_Ui_DSS_2Dcode.cbox_SlipRange5_DSS_2Dcode.isChecked():

            self.var_Ui_DSS_2Dcode.ledit_dataLength5_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt5_DSS_2Dcode.setEnabled(True)   
            self.var_Ui_DSS_2Dcode.ledit_readData5_DSS_2Dcode.setEnabled(True)           
            self.tmp_line17=self.var_dataSetting[17]  
            self.tmp_line17=self.tmp_line17.rstrip()
            tmp_startData5=self.tmp_line17[2:len(self.tmp_line17)]
            self.tmp_line18=self.var_dataSetting[18]  
            self.tmp_line18=self.tmp_line18.rstrip()
            tmp_lengthDataslip5=self.tmp_line18[2:len(self.tmp_line18)]
            self.var_Ui_DSS_2Dcode.ledit_startDigt5_DSS_2Dcode.setText(tmp_startData5)
            self.var_Ui_DSS_2Dcode.ledit_dataLength5_DSS_2Dcode.setText(tmp_lengthDataslip5)
            tmp_startData5=self.var_Ui_DSS_2Dcode.ledit_startDigt5_DSS_2Dcode.text()
            tmp_lengthDataslip5=self.var_Ui_DSS_2Dcode.ledit_dataLength5_DSS_2Dcode.text()

            
            
            self.var_dataSetting[24]="1 "+tmp_startData5+" "+tmp_lengthDataslip5+"\n"
#            self.func_wirteData_DSS_2Dcode()
            tmp_startData5=int(tmp_startData5)
            tmp_lengthDataslip5=int(tmp_lengthDataslip5)

            if (tmp_lengthDataslip5<len(self.var_datareaded)-tmp_startData5):
                    tmp_dataReaded5=self.var_datareaded[tmp_startData5:tmp_startData5+tmp_lengthDataslip5]
            else :
                    tmp_dataReaded5=self.var_datareaded[tmp_startData5:len(self.var_datareaded)]
            self.var_Ui_DSS_2Dcode.ledit_readData5_DSS_2Dcode.setText(tmp_dataReaded5)
        else:
            self.var_Ui_DSS_2Dcode.ledit_dataLength5_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt5_DSS_2Dcode.setEnabled(False)
            self.var_Ui_DSS_2Dcode.ledit_readData5_DSS_2Dcode.setEnabled(False) 
            self.var_dataSetting[24]="0"+"\n"  
        self.func_wirteData_DSS_2Dcode()
    def func_changeSliptRange5_DSS_2Dcode(self):
        tmp_startData5=self.var_Ui_DSS_2Dcode.ledit_startDigt5_DSS_2Dcode.text()
        tmp_lengthDataslip5=self.var_Ui_DSS_2Dcode.ledit_dataLength5_DSS_2Dcode.text()
        tmp_startData5=tmp_startData5.rstrip()        
        tmp_lengthDataslip5=tmp_lengthDataslip5.rstrip()
        self.var_dataSetting[24]="1 "+tmp_startData5+" "+tmp_lengthDataslip5+"\n"
        self.func_wirteData_DSS_2Dcode()
        if (tmp_lengthDataslip5!="" and tmp_startData5!=""):
            tmp_startData5=int(tmp_startData5)
            tmp_lengthDataslip5=int(tmp_lengthDataslip5)
            if (tmp_lengthDataslip5<len(self.var_datareaded)-tmp_startData5):
                    tmp_dataReaded5=self.var_datareaded[tmp_startData5:tmp_startData5+tmp_lengthDataslip5]
            else :
                    tmp_dataReaded5=self.var_datareaded[tmp_startData5:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData5_DSS_2Dcode.setText(tmp_dataReaded5)

    ########         slipt 6     #################################################

    def func_clicked_sliptRange6_DSS_2Dcode(self):

        if  self.var_Ui_DSS_2Dcode.cbox_SlipRange6_DSS_2Dcode.isChecked():

            self.var_Ui_DSS_2Dcode.ledit_dataLength6_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt6_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_readData6_DSS_2Dcode.setEnabled(True) 

            self.tmp_line17=self.var_dataSetting[17]  
            self.tmp_line17=self.tmp_line17.rstrip()
            tmp_startData6=self.tmp_line17[2:len(self.tmp_line17)]
            self.tmp_line18=self.var_dataSetting[18]  
            self.tmp_line18=self.tmp_line18.rstrip()
            tmp_lengthDataslip6=self.tmp_line18[2:len(self.tmp_line18)]
            self.var_Ui_DSS_2Dcode.ledit_startDigt6_DSS_2Dcode.setText(tmp_startData6)
            self.var_Ui_DSS_2Dcode.ledit_dataLength6_DSS_2Dcode.setText(tmp_lengthDataslip6)
            tmp_startData6=self.var_Ui_DSS_2Dcode.ledit_startDigt6_DSS_2Dcode.text()
            tmp_lengthDataslip6=self.var_Ui_DSS_2Dcode.ledit_dataLength6_DSS_2Dcode.text()

            
            
            self.var_dataSetting[25]="1 "+tmp_startData6+" "+tmp_lengthDataslip6+"\n"

            tmp_startData6=int(tmp_startData6)
            tmp_lengthDataslip6=int(tmp_lengthDataslip6)

            if (tmp_lengthDataslip6<len(self.var_datareaded)-tmp_startData6):
                    tmp_dataReaded6=self.var_datareaded[tmp_startData6:tmp_startData6+tmp_lengthDataslip6]
            else :
                    tmp_dataReaded6=self.var_datareaded[tmp_startData6:len(self.var_datareaded)]
            self.var_Ui_DSS_2Dcode.ledit_readData6_DSS_2Dcode.setText(tmp_dataReaded6)
        else:
            self.var_Ui_DSS_2Dcode.ledit_dataLength6_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt6_DSS_2Dcode.setEnabled(False)
            self.var_Ui_DSS_2Dcode.ledit_readData6_DSS_2Dcode.setEnabled(False) 
            self.var_dataSetting[25]="0"+"\n"  
        self.func_wirteData_DSS_2Dcode()
    def func_changeSliptRange6_DSS_2Dcode(self):
        tmp_startData6=self.var_Ui_DSS_2Dcode.ledit_startDigt6_DSS_2Dcode.text()
        tmp_lengthDataslip6=self.var_Ui_DSS_2Dcode.ledit_dataLength6_DSS_2Dcode.text()
        tmp_startData6=tmp_startData6.rstrip()        
        tmp_lengthDataslip6=tmp_lengthDataslip6.rstrip()
        self.var_dataSetting[25]="1 "+tmp_startData6+" "+tmp_lengthDataslip6+"\n"
        self.func_wirteData_DSS_2Dcode()
        if (tmp_lengthDataslip6!="" and tmp_startData6!=""):
            tmp_startData6=int(tmp_startData6)
            tmp_lengthDataslip6=int(tmp_lengthDataslip6)
            if (tmp_lengthDataslip6<len(self.var_datareaded)-tmp_startData6):
                    tmp_dataReaded6=self.var_datareaded[tmp_startData6:tmp_startData6+tmp_lengthDataslip6]
            else :
                    tmp_dataReaded6=self.var_datareaded[tmp_startData6:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData6_DSS_2Dcode.setText(tmp_dataReaded6)

    ########         slipt 7     #################################################

    def func_clicked_sliptRange7_DSS_2Dcode(self):

        if  self.var_Ui_DSS_2Dcode.cbox_SlipRange7_DSS_2Dcode.isChecked():

            self.var_Ui_DSS_2Dcode.ledit_dataLength7_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt7_DSS_2Dcode.setEnabled(True)
            self.var_Ui_DSS_2Dcode.ledit_readData7_DSS_2Dcode.setEnabled(True)  

            self.tmp_line17=self.var_dataSetting[17]  
            self.tmp_line17=self.tmp_line17.rstrip()
            tmp_startData7=self.tmp_line17[2:len(self.tmp_line17)]
            self.tmp_line18=self.var_dataSetting[18]  
            self.tmp_line18=self.tmp_line18.rstrip()
            tmp_lengthDataslip7=self.tmp_line18[2:len(self.tmp_line18)]
            self.var_Ui_DSS_2Dcode.ledit_startDigt7_DSS_2Dcode.setText(tmp_startData7)
            self.var_Ui_DSS_2Dcode.ledit_dataLength7_DSS_2Dcode.setText(tmp_lengthDataslip7)
            tmp_startData7=self.var_Ui_DSS_2Dcode.ledit_startDigt7_DSS_2Dcode.text()
            tmp_lengthDataslip7=self.var_Ui_DSS_2Dcode.ledit_dataLength7_DSS_2Dcode.text()

            
            
            self.var_dataSetting[26]="1 "+tmp_startData7+" "+tmp_lengthDataslip7+"\n"

            tmp_startData7=int(tmp_startData7)
            tmp_lengthDataslip7=int(tmp_lengthDataslip7)

            if (tmp_lengthDataslip7<len(self.var_datareaded)-tmp_startData7):
                    tmp_dataReaded7=self.var_datareaded[tmp_startData7:tmp_startData7+tmp_lengthDataslip7]
            else :
                    tmp_dataReaded7=self.var_datareaded[tmp_startData7:len(self.var_datareaded)]
            self.var_Ui_DSS_2Dcode.ledit_readData7_DSS_2Dcode.setText(tmp_dataReaded7)
        else:
            self.var_Ui_DSS_2Dcode.ledit_dataLength7_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt7_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_readData7_DSS_2Dcode.setEnabled(False) 
            self.var_dataSetting[26]="0"+"\n" 
        self.func_wirteData_DSS_2Dcode()

    def func_changeSliptRange7_DSS_2Dcode(self):
            tmp_startData7=self.var_Ui_DSS_2Dcode.ledit_startDigt7_DSS_2Dcode.text()
            tmp_lengthDataslip7=self.var_Ui_DSS_2Dcode.ledit_dataLength7_DSS_2Dcode.text()
            tmp_startData7=tmp_startData7.rstrip()        
            tmp_lengthDataslip7=tmp_lengthDataslip7.rstrip()
            self.var_dataSetting[26]="1 "+tmp_startData7+" "+tmp_lengthDataslip7+"\n"
            self.func_wirteData_DSS_2Dcode()
            if (tmp_lengthDataslip7!="" and tmp_startData7!=""):
                tmp_startData7=int(tmp_startData7)
                tmp_lengthDataslip7=int(tmp_lengthDataslip7)
                if (tmp_lengthDataslip7<len(self.var_datareaded)-tmp_startData7):
                        tmp_dataReaded7=self.var_datareaded[tmp_startData7:tmp_startData7+tmp_lengthDataslip7]
                else :
                        tmp_dataReaded7=self.var_datareaded[tmp_startData7:len(self.var_datareaded)]

                self.var_Ui_DSS_2Dcode.ledit_readData7_DSS_2Dcode.setText(tmp_dataReaded7)


    ########         slipt 8     #################################################

    def func_clicked_sliptRange8_DSS_2Dcode(self):


        if  self.var_Ui_DSS_2Dcode.cbox_SlipRange8_DSS_2Dcode.isChecked():

            self.var_Ui_DSS_2Dcode.ledit_dataLength8_DSS_2Dcode.setEnabled(True) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt8_DSS_2Dcode.setEnabled(True)  
            self.var_Ui_DSS_2Dcode.ledit_readData8_DSS_2Dcode.setEnabled(True)            
            self.tmp_line17=self.var_dataSetting[17]  
            self.tmp_line17=self.tmp_line17.rstrip()
            tmp_startData8=self.tmp_line17[2:len(self.tmp_line17)]
            self.tmp_line18=self.var_dataSetting[18]  
            self.tmp_line18=self.tmp_line18.rstrip()
            tmp_lengthDataslip8=self.tmp_line18[2:len(self.tmp_line18)]
            self.var_Ui_DSS_2Dcode.ledit_startDigt8_DSS_2Dcode.setText(tmp_startData8)
            self.var_Ui_DSS_2Dcode.ledit_dataLength8_DSS_2Dcode.setText(tmp_lengthDataslip8)
            tmp_startData8=self.var_Ui_DSS_2Dcode.ledit_startDigt8_DSS_2Dcode.text()
            tmp_lengthDataslip8=self.var_Ui_DSS_2Dcode.ledit_dataLength8_DSS_2Dcode.text()

            
            
            self.var_dataSetting[27]="1 "+tmp_startData8+" "+tmp_lengthDataslip8+"\n"

            tmp_startData8=int(tmp_startData8)
            tmp_lengthDataslip8=int(tmp_lengthDataslip8)

            if (tmp_lengthDataslip8<len(self.var_datareaded)-tmp_startData8):
                    tmp_dataReaded8=self.var_datareaded[tmp_startData8:tmp_startData8+tmp_lengthDataslip8]
            else :
                    tmp_dataReaded8=self.var_datareaded[tmp_startData8:len(self.var_datareaded)]
            self.var_Ui_DSS_2Dcode.ledit_readData8_DSS_2Dcode.setText(tmp_dataReaded8)
        else:
            self.var_Ui_DSS_2Dcode.ledit_dataLength8_DSS_2Dcode.setEnabled(False) 
            self.var_Ui_DSS_2Dcode.ledit_startDigt8_DSS_2Dcode.setEnabled(False)  
            self.var_Ui_DSS_2Dcode.ledit_readData8_DSS_2Dcode.setEnabled(False) 
            self.var_dataSetting[27]="0"+"\n"
        self.func_wirteData_DSS_2Dcode()
    def func_changeSliptRange8_DSS_2Dcode(self):
        tmp_startData8=self.var_Ui_DSS_2Dcode.ledit_startDigt8_DSS_2Dcode.text()
        tmp_lengthDataslip8=self.var_Ui_DSS_2Dcode.ledit_dataLength8_DSS_2Dcode.text()
        tmp_startData8=tmp_startData8.rstrip()        
        tmp_lengthDataslip8=tmp_lengthDataslip8.rstrip()
        self.var_dataSetting[27]="1 "+tmp_startData8+" "+tmp_lengthDataslip8+"\n"
        self.func_wirteData_DSS_2Dcode()
        if (tmp_lengthDataslip8!="" and tmp_startData8!=""):
            tmp_startData8=int(tmp_startData8)
            tmp_lengthDataslip8=int(tmp_lengthDataslip8)
            if (tmp_lengthDataslip8<len(self.var_datareaded)-tmp_startData8):
                    tmp_dataReaded8=self.var_datareaded[tmp_startData8:tmp_startData8+tmp_lengthDataslip8]
            else :
                    tmp_dataReaded8=self.var_datareaded[tmp_startData8:len(self.var_datareaded)]

            self.var_Ui_DSS_2Dcode.ledit_readData8_DSS_2Dcode.setText(tmp_dataReaded8)

    ######## get file config ##########################################


    def func_setConfigFile_DSS_2Dcode(self,tmp_fileConfig):
        self.var_fileConfig=tmp_fileConfig



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= var_Ui_DSS_2Dcode(None)
    mainWindow.show()
    sys.exit(app.exec_())
