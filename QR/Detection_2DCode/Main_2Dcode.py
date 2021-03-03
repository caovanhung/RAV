from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets


from M_2Dcode.I_2Dcode import Ui_Class_2Dcode
from DlogDC.Main_DlogDC_2Dcode import Class_DlogDC_2Dcode  # DC viet tat Detection conditions
from DlogJC.Main_DlogJC_2Dcode import Class_DlogJC_2Dcode  # DC viet tat Judgment Conditions
from DlogRDS.Main_DlogRDS_2Dcode import Class_DlogRDS_2Dcode
from DlogV.Main_DlogV_2Dcode import Class_DlogV_2Dcode
from DlogER.Main_DlogER_2Dcode import Class_DlogER_2Dcode
from XLA.XLA_2Dcode import Class_XLA_2Dcode
import cv2

class Class_2Dcode(QDialog):

    ### Khoi tao cac bien signal cua Main va thu cac signal cac ui setting.
    var_signal_2Dcode = pyqtSignal()

    var_signalCancel_2Dcode=pyqtSignal()
    var_signal_DC_2Dcode =pyqtSignal()
    var_signal_RDS_2Dcode =pyqtSignal()
    var_signal_ER_2Dcode = pyqtSignal()

    var_signal_ER_Cancel_2Dcode = pyqtSignal()
    var_signal_AddTool =pyqtSignal()
    var_signalFrom_ER_Cancel_2Dcode=pyqtSignal()



########################## Ham khoi tao cho class.............................
    def __init__(self, parent, *args):
        super(Class_2Dcode, self).__init__(*args)
        #load UI cua 2D code
        self.var_Ui_2Dcode=Ui_Class_2Dcode()
        self.var_Ui_2Dcode.setupUi(self)
       
        self.var_screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0, self.var_screen.height()*0.2, self.var_screen.width(), self.var_screen.height()*0.8)
        self.var_fileGoc=os.getcwd()
        self.var_fileConfig=self.var_fileGoc.replace("/Detection_2DCode","")
        self.var_fileConfig_incon_zoom_in=self.var_fileConfig+"/resources/icons/zoom-in.png"
        self.var_fileConfig_incon_zoom_out=self.var_fileConfig+"/resources/icons/zoom-out.png"
        self.var_fileConfig_incon_zoom_fit=self.var_fileConfig+"/resources/icons/zoom.png"
        self.var_Ui_2Dcode.btn_Full_2Dcode.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_fit))
        self.var_Ui_2Dcode.btn_RoomOut_2Dcode.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_out))
        self.var_Ui_2Dcode.btn_RoomIn_2Dcode.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_in))
      #  self.func_Camera_setting_open_img()



        
    #    self.show()


        
        self.var_sizeGbox=self.var_Ui_2Dcode.groupBox.frameGeometry()
        self.var_sizeFrame=self.var_Ui_2Dcode.frame_3.frameGeometry()
        self.func_createFileConfig()

#################### khoi tao ui ER EditRegion #############################
        self.var_UiDlog_ER_2Dcode =Class_DlogER_2Dcode(self)
        self.var_UiDlog_ER_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.tmp_with_ER_2Dcode   =int(0.8*(self.var_sizeGbox.width()-10))
        self.tmp_hight_ER_2Dcode   =int(0.8*self.var_sizeFrame.height())

        self.var_UiDlog_ER_2Dcode.setGeometry(self.var_screen.width()-self.tmp_with_ER_2Dcode,self.var_screen.height()*0.2+self.var_sizeFrame.y()+int(0.1*self.var_sizeFrame.height()),self.tmp_with_ER_2Dcode,self.tmp_hight_ER_2Dcode )
    ################ sign ok ER########### 
     
        self.var_signal_ER_2Dcode=self.var_UiDlog_ER_2Dcode.func_getSignal_ER_2Dcode()
       # self.var_signal_ER_2Dcode.connect(self.func_close_ER_2Dcode)
        self.var_signal_ER_2Dcode.connect(self.func_Camera_setting_open_img)
    ############### signal cancel ER ##########
        self.var_signal_ER_Cancel_2Dcode = self.var_UiDlog_ER_2Dcode.func_getCancelSignal_ER_2Dcode()
        self.var_signal_ER_Cancel_2Dcode.connect(self.func_close_ER_2Dcode)
        self.var_signal_ER_Cancel_2Dcode.connect(self.func_close_2Dcode)
       
       
        

####################Khoi tao  cac ui DC ( Detection Condition)
        # bat dau vung viet DC........................................................................
        self.var_UiDlog_DC_2Dcode=Class_DlogDC_2Dcode(self)
        self.var_UiDlog_DC_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.var_UiDlog_DC_2Dcode.setGeometry(self.var_screen.width()-self.var_sizeGbox.width()+10,self.var_screen.height()*0.2+self.var_sizeFrame.y(),self.var_sizeGbox.width()-10,self.var_sizeFrame.height())
        self.var_signal_DC_2Dcode=self.var_UiDlog_DC_2Dcode.func_getSignal_DC_2Dcode()
        self.var_signal_DC_2Dcode.connect(self.func_close_DC_2Dcode)


###################Khoi tao  cac ui JC ( Judgment Conditions)
        # bat dau vung viet JC........................................................................
        self.var_UiDlog_JC_2Dcode=Class_DlogJC_2Dcode(self)
        self.var_UiDlog_JC_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.var_UiDlog_JC_2Dcode.setGeometry(self.var_screen.width()-self.var_sizeGbox.width()+10,self.var_screen.height()*0.2+self.var_sizeFrame.y(),self.var_sizeGbox.width()-10,self.var_sizeFrame.height())
        self.var_signal_JC_2Dcode=self.var_UiDlog_JC_2Dcode.func_getSignal_JC_2Dcode()
        self.var_signal_JC_2Dcode.connect(self.func_close_JC_2Dcode)

###################Khoi tao  cac ui RDS Judgment Conditions)
        # bat dau vung viet RDS ........................................................................
        self.var_UiDlog_RDS_2Dcode=Class_DlogRDS_2Dcode(self)
        self.var_UiDlog_RDS_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.var_UiDlog_RDS_2Dcode.setGeometry(self.var_screen.width()-self.var_sizeGbox.width()+10,self.var_screen.height()*0.2+self.var_sizeFrame.y(),self.var_sizeGbox.width()-10,self.var_sizeFrame.height())
        self.var_signal_RDS_2Dcode=self.var_UiDlog_RDS_2Dcode.func_getSignal_RDS_2Dcode()
        self.var_signal_RDS_2Dcode.connect(self.func_close_RDS_2Dcode)

#######################Khoi tao  cac ui V Judgment Conditions)
        # bat dau vung viet V ........................................................................
        self.var_UiDlog_V_2Dcode=Class_DlogV_2Dcode(self)
        self.var_UiDlog_V_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        self.var_UiDlog_V_2Dcode.setGeometry(self.var_screen.width()-self.var_sizeGbox.width()+10,self.var_screen.height()*0.2+self.var_sizeFrame.y(),self.var_sizeGbox.width()-10,self.var_sizeFrame.height())
        self.var_signal_V_2Dcode=self.var_UiDlog_V_2Dcode.func_getSignal_V_2Dcode()
        self.var_signal_V_2Dcode.connect(self.func_close_V_2Dcode)

        
######################################################################################################
###########################Code chinh############################################################        
        self.var_Ui_2Dcode.btn_OK_2Dcode.clicked.connect(self.func_createSign_2Dcode)
        
        self.var_Ui_2Dcode.btn_DetectionCondition_2Dcode.clicked.connect(self.func_show_DC_2Dcode)
        
        self.var_Ui_2Dcode.btn_JudgmentConditions_2Dcode.clicked.connect(self.func_show_JC_2Dcode)
        
        self.var_Ui_2Dcode.btn_ReadDataSetting_2Dcode.clicked.connect(self.func_show_RDS_2Dcode)

        self.var_Ui_2Dcode.btn_Verification_2Dcode.clicked.connect(self.func_show_V_2Dcode)

        self.var_Ui_2Dcode.btn_RoomIn_2Dcode.clicked.connect(self.func_zoomIn)
        self.var_Ui_2Dcode.btn_Full_2Dcode.clicked.connect(self.func_zoomFit)
        self.var_Ui_2Dcode.btn_RoomOut_2Dcode.clicked.connect(self.func_zoomOut)
        self.var_Ui_2Dcode.comBox_CodeType_2Dcode.currentIndexChanged.connect(self.func_typeCode)
        self.var_Ui_2Dcode.btn_AutoTurning_2Dcode.clicked.connect(self.func_clickAutoTurning)
        self.var_Ui_2Dcode.btn_OK_2Dcode.clicked.connect(self.func_close_2Dcode)
        self.var_Ui_2Dcode.btn_CopyReadData_2Dcode.clicked.connect(self.func_clickCopyData)
        self.var_Ui_2Dcode.tedit_CopyReadData_2Dcode.textChanged.connect(self.func_changeCopyData)
        self.var_Ui_2Dcode.btn_Cancel_2Dcode.clicked.connect(self.func_createSignCancel_2Dcode)
        
       # self.func_show_ER_2Dcode()
        
        #self.func_close_DC_2Dcode()




        
######################Vung viet ham 2Dcode################################################################# 
    def func_getSignal_2Dcode(self):
        return self.var_signal_2Dcode
    
    def func_createSign_2Dcode(self):
        self.var_signal_2Dcode.emit()


    def func_getSignalCancel_2Dcode(self):
        return self.var_signalCancel_2Dcode

    def func_createSignCancel_2Dcode(self):
        self.var_signalCancel_2Dcode.emit()
        os.remove(self.var_filetxt)
        os.remove(self.var_fileImgRow)
        os.remove(self.var_fileImgProcessed)
        os.remove(self.var_fileImgRowProcessed)
    

    def func_zoomIn(self):
        self.func_scaleImage(0.01)
    def func_zoomOut(self):
        self.func_scaleImage(-0.01)
    def func_zoomFit(self):
            tmp_height, tmp_width,tmp_channel = self.tmp_img.shape
            tmp_step =  tmp_width*tmp_channel
            self.var_scaleFactor=1
            tmp_scale=int(self.var_scaleFactor*100)
            self.var_Ui_2Dcode.spinBox_Percent_2Dcode.setValue(tmp_scale)
            tmp_qImg = QImage(self.tmp_img.data, tmp_width, tmp_height, tmp_step, QImage.Format_RGB888)
            tmp_pixmap = QPixmap.fromImage(tmp_qImg)
            self.var_Ui_2Dcode.lab_ShowImgae.setPixmap(QPixmap.fromImage(tmp_qImg))
        
    def func_scaleImage(self, factor):
        self.var_scaleFactor += factor
        tmp_scale=int(self.var_scaleFactor*100)
        self.var_Ui_2Dcode.spinBox_Percent_2Dcode.setValue(tmp_scale)
        tmp_height, tmp_width,tmp_channel = self.tmp_img.shape
        if self.var_scaleFactor<3 or self.var_scaleFactor>0.4 :

            self.tmp_imgScale=cv2.resize(self.tmp_img,(int(self.var_scaleFactor*tmp_height),int(self.var_scaleFactor*tmp_width)))
            tmp_height, tmp_width,tmp_channel = self.tmp_imgScale.shape
            tmp_step =  tmp_width*tmp_channel
            tmp_qImg = QImage(self.tmp_imgScale.data, tmp_width, tmp_height, tmp_step, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(tmp_qImg)
            self.var_Ui_2Dcode.lab_ShowImgae.setPixmap(QPixmap.fromImage(tmp_qImg))
    def func_Camera_setting_open_img(self):
        self.func_close_ER_2Dcode()


        tmp_fileGoc=os.getcwd()
        tmp_fileConfig=tmp_fileGoc.replace("/Detection_2DCode","")
        tmp_fileImg=tmp_fileConfig+"/"+"0001.png"
        self.tmp_img_display=cv2.imread(tmp_fileImg,1)
        self.tmp_img=cv2.imread(tmp_fileImg,1)
        self.tmp_imgGray=cv2.imread(tmp_fileImg,0)
        self.var_scaleFactor = 1.0  





        tmp_height, tmp_width,tmp_channel = self.tmp_img_display.shape


        self.var_Ui_2Dcode.lab_ShowImgae.func_paintQrect(int(0.3*tmp_width),int(0.6*tmp_width),int(0.3*tmp_height),int(0.6*tmp_height))  
        x0= self.var_Ui_2Dcode.lab_ShowImgae.x0
        y0=self.var_Ui_2Dcode.lab_ShowImgae.y0
        x1=self.var_Ui_2Dcode.lab_ShowImgae.x1
        y1=self.var_Ui_2Dcode.lab_ShowImgae.y1

        tmp_step =  tmp_width*tmp_channel
        tmp_qImg = QImage(self.tmp_img_display.data, tmp_width, tmp_height, tmp_step, QImage.Format_RGB888)
        tmp_pixmap = QPixmap.fromImage(tmp_qImg)
        self.var_Ui_2Dcode.lab_ShowImgae.setPixmap(QPixmap.fromImage(tmp_qImg))
       # self.var_Ui_2Dcode.lab_ShowImgae.func_paintQrect(0,100,0,100)
        self.var_Ui_2Dcode.lab_ShowImgae.setfdk(1)

    def func_createsignalFrom_ER_Cancel_2Dcode(self):
        self.var_signalFrom_ER_Cancel_2Dcode.emit()
        
    def func_get_signalForm_ER_2Dcode(self):
        return self.var_signalFrom_ER_Cancel_2Dcode

    def func_show_2Dcode(self):
        self.show()
        


        
        self.var_screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.var_sizeGbox=self.var_Ui_2Dcode.groupBox.frameGeometry()
        self.var_sizeFrame=self.var_Ui_2Dcode.frame_3.frameGeometry()

    



    ################ khoi tao ui ER EditRegion #############################
        self.var_UiDlog_ER_2Dcode =Class_DlogER_2Dcode(self)
        self.var_UiDlog_ER_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.tmp_with_ER_2Dcode   =int(0.8*(self.var_sizeGbox.width()-10))
        self.tmp_hight_ER_2Dcode   =int(0.8*self.var_sizeFrame.height())

        self.var_UiDlog_ER_2Dcode.setGeometry(self.var_screen.width()-self.tmp_with_ER_2Dcode,self.var_screen.height()*0.2+self.var_sizeFrame.y()+int(0.1*self.var_sizeFrame.height()),self.tmp_with_ER_2Dcode,self.tmp_hight_ER_2Dcode )
       
    ################ sign ok ER########### 
     
        self.var_signal_ER_2Dcode=self.var_UiDlog_ER_2Dcode.func_getSignal_ER_2Dcode()
        self.var_signal_ER_2Dcode.connect(self.func_Camera_setting_open_img)
    ############### signal cancel ER ##########
        self.var_signal_ER_Cancel_2Dcode = self.var_UiDlog_ER_2Dcode.func_getCancelSignal_ER_2Dcode()
        self.var_signal_ER_Cancel_2Dcode.connect(self.func_close_ER_2Dcode)
        self.var_signal_ER_Cancel_2Dcode.connect(self.func_close_2Dcode)
        self.var_signal_ER_Cancel_2Dcode.connect(self.func_createsignalFrom_ER_Cancel_2Dcode)
       
    ####################Khoi tao  cac ui DC ( Detection Condition)
        # bat dau vung viet DC........................................................................
        self.var_UiDlog_DC_2Dcode=Class_DlogDC_2Dcode(self)
        self.var_UiDlog_DC_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.var_UiDlog_DC_2Dcode.setGeometry(self.var_screen.width()-self.var_sizeGbox.width()+10,self.var_screen.height()*0.2+self.var_sizeFrame.y(),self.var_sizeGbox.width()-10,self.var_sizeFrame.height())
        self.var_signal_DC_2Dcode=self.var_UiDlog_DC_2Dcode.func_getSignal_DC_2Dcode()
        self.var_signal_DC_2Dcode.connect(self.func_close_DC_2Dcode)


    ###################Khoi tao  cac ui JC ( Judgment Conditions)
        # bat dau vung viet JC........................................................................
        self.var_UiDlog_JC_2Dcode=Class_DlogJC_2Dcode(self)
        self.var_UiDlog_JC_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.var_UiDlog_JC_2Dcode.setGeometry(self.var_screen.width()-self.var_sizeGbox.width()+10,self.var_screen.height()*0.2+self.var_sizeFrame.y(),self.var_sizeGbox.width()-10,self.var_sizeFrame.height())
        self.var_signal_JC_2Dcode=self.var_UiDlog_JC_2Dcode.func_getSignal_JC_2Dcode()
        self.var_signal_JC_2Dcode.connect(self.func_close_JC_2Dcode)

###################Khoi tao  cac ui RDS Judgment Conditions)
        # bat dau vung viet RDS ........................................................................
        self.var_UiDlog_RDS_2Dcode=Class_DlogRDS_2Dcode(self)
        self.var_UiDlog_RDS_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.var_UiDlog_RDS_2Dcode.setGeometry(self.var_screen.width()-self.var_sizeGbox.width()+10,self.var_screen.height()*0.2+self.var_sizeFrame.y(),self.var_sizeGbox.width()-10,self.var_sizeFrame.height())
        self.var_signal_RDS_2Dcode=self.var_UiDlog_RDS_2Dcode.func_getSignal_RDS_2Dcode()
        self.var_signal_RDS_2Dcode.connect(self.func_close_RDS_2Dcode)

#######################Khoi tao  cac ui V Judgment Conditions)
        # bat dau vung viet V ........................................................................
        self.var_UiDlog_V_2Dcode=Class_DlogV_2Dcode(self)
        self.var_UiDlog_V_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        self.var_UiDlog_V_2Dcode.setGeometry(self.var_screen.width()-self.var_sizeGbox.width()+10,self.var_screen.height()*0.2+self.var_sizeFrame.y(),self.var_sizeGbox.width()-10,self.var_sizeFrame.height())
        self.var_signal_V_2Dcode=self.var_UiDlog_V_2Dcode.func_getSignal_V_2Dcode()
        self.var_signal_V_2Dcode.connect(self.func_close_V_2Dcode)       

    def func_typeCode(self):
        self.var_typeCode=self.var_Ui_2Dcode.comBox_CodeType_2Dcode.currentText()
        self.var_dataSetting[5]="1 "+self.var_typeCode+"\n"
        self.func_wirteData()
        self.func_read2Dcode_2Dcode()

        


    def func_wirteData(self):
        self.var_fileData = open(self.var_filetxt, 'w')
        self.var_fileData.writelines(self.var_dataSetting)
        self.var_fileData.close()
        
    def func_clickAutoTurning(self):
      #  self.var_typeCode=self.var_Ui_2Dcode.comBox_CodeType_2Dcode.currentText()
        self.var_dataSetting[6]="1 "+"1"+"\n"
        self.var_Ui_2Dcode.btn_AutoTurning_2Dcode.setStyleSheet("background-color: blue")
        self.func_wirteData()
        self.func_codeRevolution()


        
        self.func_read2Dcode_2Dcode()
    #    self.func_readLength_2Dcode()
    #    self.func_readPositon_2Dcode()
      #  self.func_readAngle_2Dcode()

    def func_codeRevolution(self):
        ######## chuong trinh xu ly anh doc revolution######
        self.var_codeRevolution="11"
        self.var_dataSetting[7]="0 "+ self.var_codeRevolution+"\n"
        self.var_Ui_2Dcode.lab_CodeResolution_2Dcode.setText(self.var_codeRevolution)
        self.var_Ui_2Dcode.lab_CodeResolution_2Dcode.setEnabled(False)
        self.func_wirteData()
        
        
    def func_clickCopyData(self):

        self.var_line57=self.var_dataSetting[57]
        if len(self.var_line57)!=1:
           
            self.var_loadData =self.var_line57[2:len(self.var_line57)]
            self.var_loadData=self.var_loadData.rstrip()
          
            self.var_Ui_2Dcode.tedit_CopyReadData_2Dcode.setPlainText(self.var_loadData)
            self.var_Ui_2Dcode.ledit_CovertedData_2Dcode.setText(self.var_loadData)
            self.var_dataSetting[60]="1 "+"OK"+"\n"
            self.func_wirteData()


    def func_changeCopyData(self):
        self.var_changeCopyData=self.var_Ui_2Dcode.tedit_CopyReadData_2Dcode.toPlainText()
        self.var_changeCopyData= self.var_changeCopyData.rstrip()
        self.var_dataSetting[58]="1 "+ self.var_changeCopyData+"\n"
        self.var_dataSetting[59]="1 "+ self.var_changeCopyData+"\n"
        self.var_line57=self.var_dataSetting[57] 
     

        if len(self.var_line57)!=1:
           
            self.var_loadData =self.var_line57[2:len(self.var_line57)]
            self.var_loadData=self.var_loadData.rstrip()
            if self.var_loadData!=self.var_changeCopyData:
                self.var_dataSetting[60]="1 "+"NG"+"\n"
                #print(self.var_loadData)
            else:
                self.var_dataSetting[60]="1 "+"OK"+"\n"

        self.func_wirteData()
        self.var_Ui_2Dcode.ledit_CovertedData_2Dcode.setText(self.var_changeCopyData)
        self.var_Ui_2Dcode.ledit_CovertedData_2Dcode.setStyleSheet("color: black")






########## tao file setup #############        
    def func_createFileConfig(self):

        var_fileGoc=os.getcwd()
        if var_fileGoc.find("Detection_2DCode",20)==-1:
             #self.fileImgProcessed=file_goc+"/Image Processed"
             self.var_fileRow=os.getcwd()+"/ImageRaw"
             self.var_fileProcessed=os.getcwd()+"/ImageProcessed"
             self.var_fileRowProcessed=os.getcwd()+"/ImageRowProcessed"
             self.var_fileConfig=os.getcwd()+"/config"
        else:
          #   self.fileImgProcessed=file_goc.replace("Detection_2DCode","Image Processed")
             self.var_fileRow=var_fileGoc.replace("Detection_2DCode","ImageRaw")
             self.var_fileProcessed=var_fileGoc.replace("Detection_2DCode","ImageProcessed")
             self.var_fileRowProcessed=var_fileGoc.replace("Detection_2DCode","ImageRowProcessed")
             self.var_fileConfig=var_fileGoc.replace("Detection_2DCode","config")
            
        
        self.var_fileConfig=self.var_fileConfig.rstrip()
        tmp_Count_img=len(os.listdir(self.var_fileConfig))
        tmp_Count_img=tmp_Count_img+1
        tmp_length=len (str(tmp_Count_img))
  
        
        if tmp_length==1:
           self.var_nameFile="000"+str(tmp_Count_img)
        if tmp_length==2:
           self.var_nameFile="00"+str(tmp_Count_img)
        if tmp_length==3:
           self.var_nameFile="0"+str(tmp_Count_img)

        self.var_filetxt=self.var_fileConfig+"/"+self.var_nameFile+".ini"
        self.var_fileImgRow=self.var_fileRow+"/"+self.var_nameFile+".jpg"
        self.var_fileImgProcessed=self.var_fileProcessed+"/"+self.var_nameFile+".jpg"
        self.var_fileImgRowProcessed=self.var_fileRowProcessed+"/"+self.var_nameFile+".jpg"


        
        self.var_fileData = open(self.var_filetxt, 'w')
        self.var_fileData.writelines("Detection_2Dcode\n")
        self.var_fileData.writelines( self.var_fileConfig+"\n")
        self.var_fileData.writelines( self.var_fileImgRow+"\n")
        self.var_fileData.writelines(self.var_fileImgProcessed+"\n")
        self.var_fileData.writelines(self.var_fileImgRowProcessed+"\n")
        self.var_fileData.close()
        self.var_fileData = open(self.var_filetxt, 'r')
        self.var_dataSetting=self.var_fileData.readlines()
        self.var_fileData.close()
        for i in range(75):
            self.var_dataSetting.append("0\n")
            if i==17:
                self.var_dataSetting[17]="1 "+"0"+"\n"
            if i==18:
                self.var_dataSetting[18]="1 "+"100"+"\n"                
            if i==54 :
                self.var_dataSetting[54]="1 "+"1"+"\n"
            if i==56 :
                self.var_dataSetting[56]="1 "+"All Data"+"\n"                
        self.var_fileData = open(self.var_filetxt, 'w')
        self.var_fileData.writelines(self.var_dataSetting)
        self.var_Ui_2Dcode.btn_CopyReadData_2Dcode.setEnabled(0)
        self.var_Ui_2Dcode.tedit_CopyReadData_2Dcode.setEnabled(0)
        self.var_Ui_2Dcode.ledit_CovertedData_2Dcode.setEnabled(0)
        self.var_fileData.close()



################# chuong trinh xu ly anh ########################################       
    ######### read 2D code ################  
    def func_read2Dcode_2Dcode(self):


        self.tmp_x0=self.var_Ui_2Dcode.lab_ShowImgae.x0
        self.tmp_x1=self.var_Ui_2Dcode.lab_ShowImgae.x1

        self.tmp_y0=self.var_Ui_2Dcode.lab_ShowImgae.y0
        self.tmp_y1=self.var_Ui_2Dcode.lab_ShowImgae.y1



        self.tmp_tyData=self.var_Ui_2Dcode.comBox_CodeType_2Dcode.currentText()
        self.var_XLA_2Dcode=Class_XLA_2Dcode(self.tmp_imgGray,self.tmp_img, self.tmp_x0, self.tmp_y0, self.tmp_x1, self.tmp_y1,self.var_fileImgRow)
        self.var_XLA_2Dcode.func_Threshold_xuly(30,2) 
        self.var_data2Dcode="Khong phat hien"
        if (self.tmp_tyData=="QR"):
            self.var_data2Dcode,self.tmp_image_xuly=self.var_XLA_2Dcode.func_detectQR_Code()
            self.func_showImage_2Dcode(self.tmp_image_xuly)
            self.var_XLA_2Dcode.func_saveImage(self.var_fileImgRowProcessed,self.var_fileImgProcessed)

        if (self.tmp_tyData=="DataMatrix"):
         #   print("DataMatrix")
            self.var_data2Dcode,self.tmp_image_xuly=self.var_XLA_2Dcode.func_detectData_matrix()
            self.func_showImage_2Dcode(self.tmp_image_xuly) 
            self.var_XLA_2Dcode.func_saveImage(self.var_fileImgRowProcessed,self.var_fileImgProcessed)


        if  self.var_data2Dcode!="Khong phat hien":
            self.var_Ui_2Dcode.btn_CopyReadData_2Dcode.setEnabled(1)
            self.var_Ui_2Dcode.tedit_CopyReadData_2Dcode.setEnabled(1)
            self.var_Ui_2Dcode.ledit_CovertedData_2Dcode.setEnabled(1)
            self.var_dataSetting[62]="1 "+str(len(self.var_data2Dcode))+"\n"
        else :
            self.var_Ui_2Dcode.btn_CopyReadData_2Dcode.setEnabled(0)
            self.var_Ui_2Dcode.tedit_CopyReadData_2Dcode.setEnabled(0)
            self.var_Ui_2Dcode.ledit_CovertedData_2Dcode.setEnabled(0)

        self.var_Ui_2Dcode.lab_ReadData_2Dcode.setText(self.var_data2Dcode)  

        self.tmp_line17=self.var_dataSetting[17]
        self.tmp_line18=self.var_dataSetting[18]
       
        self.tmp_startDigt=self.tmp_line17[2:len(self.tmp_line17)]
        self.tmp_lengthData=self.tmp_line18[2:len(self.tmp_line18)]
        self.tmp_startDigt=self.tmp_startDigt.rstrip()
        self.tmp_lengthData=self.tmp_lengthData.rstrip()

        self.var_dataSetting[73]="1 "+self.var_data2Dcode+"\n" 
        if (self.tmp_startDigt!=""and self.tmp_lengthData!=""):  
            self.var_dataSetting[57]="1 "+self.var_data2Dcode[int(self.tmp_startDigt):int(self.tmp_lengthData)]+"\n"         
            print("dac chay if") 
        print(self.var_dataSetting)
        self.func_wirteData()

 

    def func_readPositon_2Dcode(self):
        self.var_posXMeasure="50"
        self.var_posYMeasure="50"
        self.var_dataSetting[66]="1 "+self.var_posXMeasure+"\n"   
        self.var_dataSetting[67]="1 "+self.var_posYMeasure+"\n" 
        self.func_wirteData()       

    def func_readLength_2Dcode(self):
        self.var_lengthMeasure="100"  
        self.var_dataSetting[62]="1 "+self.var_lengthMeasure+"\n" 
        self.func_wirteData()       

    def func_readAngle_2Dcode(self):
        self.var_angleMeasure="10"  
        self.var_dataSetting[71]="1 "+self.var_angleMeasure+"\n" 
        self.func_wirteData() 

    def func_showImage_2Dcode(self,tmp_img):
        tmp_height, tmp_width,tmp_channel = self.tmp_img.shape
        tmp_step =  tmp_width*tmp_channel
        tmp_qImg = QImage(self.tmp_img.data, tmp_width, tmp_height, tmp_step, QImage.Format_RGB888)
        tmp_pixmap = QPixmap.fromImage(tmp_qImg)
        self.var_Ui_2Dcode.lab_ShowImgae.setPixmap(QPixmap.fromImage(tmp_qImg))       

########## close 2Dcode######
    def func_close_2Dcode(self):
        self.close()





########  load data to main #####################
    def func_loadData_Main_2Dcode(self):
        self.var_fileData = open(self.var_filetxt, 'r')
        self.var_dataSetting=self.var_fileData.readlines()
        self.func_loadData_DC_2Dcode()
        self.func_loadData_RDS_2Dcode()
        self.func_loadData_JC_2Dcode()
      
        


        self.var_fileData.close()
    def func_loadData_DC_2Dcode(self):     
    ####doc loai code##########
        self.tmp_line5=self.var_dataSetting[5]
     
        self.tmp_typeData=self.tmp_line5[2:len(self.tmp_line5)]
        self.tmp_typeData=self.tmp_typeData.rstrip()
        self.var_Ui_2Dcode.comBox_CodeType_2Dcode.setCurrentText(self.tmp_typeData)

        
    ### doc auto turning########## 
        self.tmp_line6=self.var_dataSetting[6]  
        self.tmp_autoTuring=self.tmp_line6[2:len(self.tmp_line6)]
        self.tmp_autoTuring=self.tmp_autoTuring.rstrip()
        if (self.tmp_autoTuring=="1"):
            self.var_Ui_2Dcode.btn_AutoTurning_2Dcode.setStyleSheet("background-color: blue")



    ####### load Data RDS code ####
    def func_loadData_RDS_2Dcode(self):
        self.tmp_line57=self.var_dataSetting[57]
       
        self.tmp_dataReaded=self.tmp_line57[2:len(self.tmp_line57)]
        self.tmp_dataReaded=self.tmp_dataReaded.rstrip()
        if (len(self.tmp_dataReaded)!=0):
            self.var_Ui_2Dcode.lab_ReadData_2Dcode.setText(self.tmp_dataReaded)

    
    ########  load Data  JC code ####
    def func_loadData_JC_2Dcode(self):
        self.tmp_line58=self.var_dataSetting[58]
        self.tmp_line59=self.var_dataSetting[59]
       
        self.tmp_copyData=self.tmp_line58[2:len(self.tmp_line58)]
        self.tmp_copyData=self.tmp_copyData.rstrip()

        self.tmp_convertData=self.tmp_line59[2:len(self.tmp_line59)]
        self.tmp_convertData=self.tmp_convertData.rstrip()
       # print(tmp_convertData)
        if (len(self.tmp_convertData)!=0):
            self.var_Ui_2Dcode.tedit_CopyReadData_2Dcode.setPlainText(self.tmp_copyData)
            self.var_Ui_2Dcode.ledit_CovertedData_2Dcode.setText(self.tmp_convertData)
        
####################### vung viet ham  ER(Edit Region) ############################################

    def func_show_ER_2Dcode(self):
        self.var_UiDlog_ER_2Dcode.show()



    def func_close_ER_2Dcode(self):
        self.var_UiDlog_ER_2Dcode.close()
        self.var_Inspection_Region,self.var_nameText = self.var_UiDlog_ER_2Dcode.func_setConfigData_ER_2Dcode()

     

            
        
####################### vung viet ham  DC(detection Condtion) ############################################

    def func_show_DC_2Dcode(self):
        self.var_UiDlog_DC_2Dcode.show()
        self.var_UiDlog_DC_2Dcode.func_setConfigFile_DC_2Dcode(self.var_filetxt)
        self.var_UiDlog_DC_2Dcode.func_readData_DC_2Dcode()

    ##############Khoi tao  cac ui DC ( Detection Condition)
        # bat dau vung viet DC........................................................................
  #      self.var_UiDlog_DC_2Dcode=Class_DlogDC_2Dcode(self)
  #      self.var_UiDlog_DC_2Dcode.setWindowFlag(QtCore.Qt.FramelessWindowHint)
  #      self.var_UiDlog_DC_2Dcode.setGeometry(self.var_screen.width()-self.var_sizeGbox.width()+10,self.var_screen.height()*0.2+self.var_sizeFrame.y(),self.var_sizeGbox.width()-10,self.var_sizeFrame.height())
  #      self.var_signal_DC_2Dcode=self.var_UiDlog_DC_2Dcode.func_getSignal_DC_2Dcode()
    #    self.var_signal_DC_2Dcode.connect(self.func_close_DC_2Dcode)

    def func_close_DC_2Dcode(self):
        self.var_UiDlog_DC_2Dcode.close()
        self.func_loadData_Main_2Dcode()
        
#############################################################################################


############################## vung viet ham  JC(detection Condtion) #########

    def func_show_JC_2Dcode(self):
        self.var_UiDlog_JC_2Dcode.show()

        self.var_UiDlog_JC_2Dcode.func_setConfigFile_JC_2Dcode(self.var_filetxt)
        self.var_UiDlog_JC_2Dcode.func_readData_JC_2Dcode()

        
    def func_close_JC_2Dcode(self):
        self.var_UiDlog_JC_2Dcode.close()
        self.func_loadData_Main_2Dcode()
        
#############################################################################################    

################################# vung viet ham  RDS(detection Condtion) ####################

    def func_show_RDS_2Dcode(self):
        self.var_UiDlog_RDS_2Dcode.show()
        self.var_UiDlog_RDS_2Dcode.func_setConfigFile_RDS_2Dcode(self.var_filetxt)
        self.var_UiDlog_RDS_2Dcode.func_readData_RDS_2Dcode()
        
    def func_close_RDS_2Dcode(self):
        self.var_UiDlog_RDS_2Dcode.close()
        self.func_loadData_Main_2Dcode()
        
#############################################################################################

#############################################################################################    

########################## vung viet ham  V(detection Condtion)##############################

    def func_show_V_2Dcode(self):
        self.var_UiDlog_V_2Dcode.show()
    def func_close_V_2Dcode(self):
        self.var_UiDlog_V_2Dcode.close()
        
#############################################################################################  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= Class_2Dcode(None)
    mainWindow.show()
    sys.exit(app.exec_())
