from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel ,QSizePolicy, QScrollArea, QMessageBox, QMenu, QAction, QFileDialog, qApp
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QRect
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter, QPen, QGuiApplication
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

import sys
import os
import configparser


from Ui_mainForm.I_formMain import Ui_Class_formMain
from AddTool.Main_DlogAddTool import Class_DlogAddTool
from AddImage.Main_DlogAddImage import Class_DlogAddImage
from CameraSetting.Main_DlogSetCamera import Class_CameraSetting
from Detection_2DCode.Main_2Dcode import Class_2Dcode
from Detection_1DCode.Main_1Dcode import Class_1Dcode
from Detection_1DCode.ActionFile import ActionFile

#from  Camera import Camera_Basler

var_dirFileOS = os.getcwd()
var_dirFileOS = var_dirFileOS.rstrip()
var_dirFileOS = var_dirFileOS.replace("/Detection_1DCode","")
var_dirFileConfig = var_dirFileOS + "/" + "config"

class Class_formMain(QDialog):

    ### Khoi tao cac bien signal cua Main va thu cac signal cac ui setting.
    var_signal_formMain = pyqtSignal()
    var_signal_AddTool= pyqtSignal()
    var_signal_2Dcode = pyqtSignal()
    var_signal_From_ER_2Dcode = pyqtSignal()
    var_signalCancel_2Dcode = pyqtSignal()
    var_signalLoadFunction = pyqtSignal()
    var_signalDelete = pyqtSignal()
    var_fileTextFunction=""

        ###### 1D #####################
    var_signal_AddTool_1D = pyqtSignal()
    var_signal_OK_1Dcode = pyqtSignal()


########################## Ham khoi tao cho class.............................
    def __init__(self, parent, *args):
        super(Class_formMain, self).__init__(*args)
        #load UI cua 2D code
        self.var_Ui_formMain=Ui_Class_formMain()
        self.var_Ui_formMain.setupUi(self)
        ###################Hung#############################
        self.file = ActionFile(var_dirFileConfig)
        self.config = configparser.ConfigParser()
        #self.camera = Camera_Basler()
        ####################################################
        self.var_screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, self.var_screen.width(), self.var_screen.height())
        self.var_fileGoc=os.getcwd()
        self.var_fileConfig=self.var_fileGoc.replace("/Main","")
        self.var_fileConfig_incon_zoom_in=self.var_fileConfig+"/resources/icons/zoom-in.png"
        self.var_fileConfig_incon_zoom_out=self.var_fileConfig+"/resources/icons/zoom-out.png"
        self.var_fileConfig_incon_zoom_fit=self.var_fileConfig+"/resources/icons/zoom.png"
        self.var_Ui_formMain.btn_zoomNormal_ModGuiMain.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_fit))
        self.var_Ui_formMain.btn_zoomOut_ModGuiMain.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_out))
        self.var_Ui_formMain.btn_zoomIn_ModGuiMain.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_in))        
        self.func_creatListTool()
        self.func_loadFunctionSetting()
        for i in range (100):
            self.var_signalLoadFunction=self.var_Ui_formMain.btn_showTool[i].func_getSignal_btn()
            self.var_signalDelete=self.var_Ui_formMain.btn_showTool[i].func_getSignalMouse_btn()
            self.var_signalLoadFunction.connect(self.func_runFuntionToMainScreen)
            self.var_signalDelete.connect(self.func_deleteFunction)

        ################ Camera Setting ################################
        self.var_UiDlog_CameraSetting = Class_CameraSetting(None)
        self.var_UiDlog_CameraSetting.setWindowFlag(QtCore.Qt.FramelessWindowHint)  

        ################ Add Image ################################
        self.var_UiDlog_AddImage=Class_DlogAddImage(None)
        self.var_UiDlog_AddImage.setWindowFlag(QtCore.Qt.FramelessWindowHint)          
        ################ Add Tool ################################
                ##### 2D #######
        self.var_UiDlog_AddTool=Class_DlogAddTool(None)
        self.var_UiDlog_AddTool.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.var_signal_AddTool=self.var_UiDlog_AddTool.func_getSignal_AddTool()
        self.var_signal_AddTool.connect(self.func_openTool)
        ################# function 2D code #########
        self.numberEditCliced = 0  ######xem edit  duoc click lan thu may

        ############## Main  ##############################################################        
        #self.var_Ui_formMain.btn_RegisterImage_ModGuiMain.clicked.connect(self.func_close_FormMain)
        self.var_Ui_formMain.btn_addTool_ModGuiMain.clicked.connect(self.func_show_func_AddTool)
        self.var_Ui_formMain.btn_selectEditTool_Mod_2Dcode.clicked.connect(self.func_reloadFunc)
        self.var_Ui_formMain.btn_setCamera_ModGuiMain.clicked.connect(self.func_showCameraSetting)

        #self.var_Ui_formMain.btn_RegisterImage_ModGuiMain.clicked.connect(self.var_UiDlog_AddImage.func_showFuncAddImage)
        self.var_Ui_formMain.btn_RegisterImage_ModGuiMain.clicked.connect(self.func_show_func_AddImage)

        self.var_UiDlog_AddImage.var_Ui_DlogAddImage.btn_close.clicked.connect(self.func_close_func_AddImage)

        self.show()
        #############################Hung _ 1D ###############################################
        self.var_signal_AddTool_1D=self.var_UiDlog_AddTool.func_getSignal1D_AddTool()
        self.var_signal_AddTool_1D.connect(self.func_openTool1D)

# ###############################################################################################

    def func_showCameraSetting(self):
         self.var_UiDlog_CameraSetting.show()
    def func_closeCameraSetting(self):
         self.var_UiDlog_CameraSetting.close()
# ###############################################################################################
    def func_show_func_AddImage(self):
        self.var_UiDlog_AddImage.show()

    def func_close_func_AddImage(self):
        self.var_UiDlog_AddImage.close()
#################################################################################################
    def func_runFuntionToMainScreen(self):
            file_goc =os.getcwd() #lay file goc
            
            self.var_filetxt1=file_goc +"/0000.txt"      
            self.var_fileData1 =open(self.var_filetxt1,"r")
            self.var_data1=self.var_fileData1.readlines()
            self.var_datafileConfig=self.var_data1[0]
            self.var_datafileConfig=self.var_datafileConfig.rstrip()
            self.var_fileData1.close()
            self.var_fileData=open(self.var_datafileConfig,"r")
            self.var_dataSetting=self.var_dataSetting=self.var_fileData.readlines()
            self.tmp_line1=self.var_dataSetting[0]
            self.tmp_line1=self.tmp_line1.rstrip()
            self.var_fileData.close()
            
            if self.tmp_line1=="Detection_2Dcode":
                self.func_reloadFunc_2Dcode()
            elif self.tmp_line1=="[Detection_1Dcode]":
                #self.func_reloadFunc_1Dcode()
                print("CLICK 1D")

    def func_deleteFunction(self):
            file_goc =os.getcwd() #lay file goc
            
            self.var_filetxt1=file_goc +"/0000.txt"      
            self.var_fileData1 =open(self.var_filetxt1,"r")
            self.var_data1=self.var_fileData1.readlines()
            self.var_datafileConfig=self.var_data1[0]
            self.var_datafileConfig=self.var_datafileConfig.rstrip()
            self.var_ten=self.var_data1[1]
            self.var_ten=self.var_ten.rstrip()

            self.var_fileData1.close()
            self.var_fileData=open(self.var_datafileConfig,"r")
            self.var_dataSetting=self.var_dataSetting=self.var_fileData.readlines()

            self.tmp_line=self.var_dataSetting[0]
            self.tmp_line=self.tmp_line.rstrip()
            self.tmp_line1=self.var_dataSetting[1]
            self.tmp_line1=self.tmp_line1.rstrip()
            self.tmp_line2=self.var_dataSetting[2]
            self.tmp_line2=self.tmp_line2.rstrip()
            self.tmp_line3=self.var_dataSetting[3]
            self.tmp_line3=self.tmp_line3.rstrip()
            self.tmp_line4=self.var_dataSetting[4]
            self.tmp_line4=self.tmp_line4.rstrip()   

            # lay list file
            file_cofig=os.listdir(file_goc+'/config')#list file /config
            file_image_list=os.listdir(file_goc+'/ImageProcessed')
            file_image_cut_list=os.listdir(file_goc+'/ImageRaw')
            file_image_cut_listRow=os.listdir(file_goc+'/ImageRowProcessed')
            #sap xep list file
            file_cofig=sorted(file_cofig,reverse=True)
            file_image_list=sorted(file_image_list,reverse=True)
            file_image_cut_list=sorted(file_image_cut_list,reverse=True)
            file_image_cut_listRow=sorted(file_image_cut_listRow,reverse=True)
            
            leng_file=len(os.listdir(file_goc+'/config'))
            self.dodai= leng_file

            file_cofig = file_cofig[::-1]
            file_image_list = file_image_list[::-1]
            file_image_cut_list = file_image_cut_list[::-1]
            file_image_cut_listRow =file_image_cut_listRow[::-1]

            #Xoa file config, image
            if self.tmp_line == "Detection_2Dcode":
                print("remote Detection_2Dcode")
                print("self.tmp_line1: "+self.tmp_line1)
                print("self.tmp_line2: "+self.tmp_line2)
                print("self.tmp_line3: "+self.tmp_line3)
                print("self.tmp_line4: "+self.tmp_line4)

                os.remove(self.tmp_line1)
                os.remove(self.tmp_line2)
                os.remove(self.tmp_line3)
                os.remove(self.tmp_line4)

            elif self.tmp_line == "[Detection_1Dcode]":
                print("remote Detection_1Dcode")
                print("self.var_datafileConfig: " + self.var_datafileConfig)

                self.config.read(self.var_datafileConfig)
                os.remove(self.config.get("Detection_1Dcode", "dir_ImageProcessed"))
                os.remove(self.config.get("Detection_1Dcode", "dir_ImageRaw"))
                os.remove(self.config.get("Detection_1Dcode", "dir_ImageRowProcessed"))
                os.remove(self.config.get("Detection_1Dcode", "dir_config"))

            self.var_fileData.close()
            print("da chay",self.var_ten)
            ten=int(self.var_ten)
            print("leng_file: " + str(leng_file))
            for i in range (leng_file):
                self.var_Ui_formMain.btn_showTool[i].setHidden(1)
                self.var_Ui_formMain.lab_showTool[i].setHidden(1)
                self.var_Ui_formMain.frame_2[i].setHidden(1)    

            for i in range(ten,leng_file):
                            print("ten : " + str(i))
                        #xep ca file trong config
                            file_1=file_goc+'/config'+'/'+file_cofig[i]
                            file_2=file_goc+'/config'+'/'+file_cofig[i-1]
                            os.rename( file_1,file_2 )
                        #xep cac file trong file_img_list
                            file_img_1=file_goc+'/ImageProcessed'+'/'+file_image_list[i]
                            file_img_2=file_goc+'/ImageProcessed'+'/'+file_image_list[i-1]
                            os.rename( file_img_1,file_img_2 )
                        #xep cac file trong file_img_cat
                            file_img_cut_1=file_goc+'/ImageRaw'+'/'+file_image_cut_list[i]
                            file_img_cut_2=file_goc+'/ImageRaw'+'/'+file_image_cut_list[i-1]
                            os.rename( file_img_cut_1,file_img_cut_2 )
            
                        #xep cac file trong file_img_cat
                            file_img_cut_1_Row=file_goc+'/ImageRowProcessed'+'/'+file_image_cut_listRow[i]
                            file_img_cut_2_Row=file_goc+'/ImageRowProcessed'+'/'+file_image_cut_listRow[i-1]
                            os.rename( file_img_cut_1_Row,file_img_cut_2_Row ) 

                            list_ten=os.listdir(file_goc+'/config')
                            list_ten=sorted(list_ten,reverse=True)
                            list_ten = list_ten[::-1] 
                            leng_file=len(os.listdir(file_goc+'/config'))
                  
                            for i in range(0,leng_file):
                                ten=int(i)
                                file_config=file_goc+'/config/'+list_ten[ten]
                                print(file_config)
                              #  studentList = []
                                File = open (file_config, "r")
     
                                studentList = File.readlines()
                                File.close()
                                print("studentList[0] = " + studentList[0])
                                temp_codetype = studentList[0]
                                temp_codetype = temp_codetype.rstrip()
                                if temp_codetype == "Detection_2Dcode":
                                    print("i = " + str(i))
                                    ten_1=studentList[1]
                                    ten_2=studentList[2]
                                    ten_3=studentList[3]
                                    ten_4=studentList[4]
                                    ten_1=ten_1.rstrip()
                                    ten_2=ten_2.rstrip()
                                    ten_3=ten_3.rstrip()
                                    ten_4=ten_4.rstrip()

                                    vitri_1=len(ten_1)
                                    vitri_2=len(ten_2)
                                    vitri_3=len(ten_3)
                                    vitri_4=len(ten_4)
                                    str_canthay=list_ten[i][0:4]

                                    str_ten_thay_1=ten_1[vitri_1-8:vitri_1-4]
                                    str_ten_thay_2=ten_2[vitri_2-8:vitri_2-4]
                                    str_ten_thay_3=ten_3[vitri_3-8:vitri_3-4]
                                    str_ten_thay_4=ten_4[vitri_4-8:vitri_4-4]

                                    studentList[1]=ten_1.replace(str_ten_thay_1,str_canthay)+"\n"
                                    studentList[2]=ten_2.replace(str_ten_thay_2,str_canthay)+"\n"
                                    studentList[3]=ten_3.replace(str_ten_thay_3,str_canthay)+"\n"
                                    studentList[4]=ten_4.replace(str_ten_thay_4,str_canthay)+"\n"

                                    File_1 = open (file_config, "w")
                                    File_1.writelines(studentList)
                                    File_1.close()

                                elif temp_codetype == "[Detection_1Dcode]" :
                                    num = self.file.func_convert_1to4Digit(i+1)
                                    print("i = " + str(i))

                                    dir_config = var_dirFileOS + "/" + "config"+"/"+str(num)+".ini"
                                    dir_ImageProcessed = var_dirFileOS + "/" + "ImageProcessed"+"/"+str(num)+".jpg"
                                    dir_ImageRaw = var_dirFileOS + "/" + "ImageRaw"+"/"+str(num)+".jpg"
                                    dir_ImageRowProcessed = var_dirFileOS + "/" + "ImageRowProcessed"+"/"+str(num)+".jpg"

                                    self.file.updateDataFile(str(list_ten[i]),"Detection_1Dcode","dir_config",dir_config)
                                    self.file.updateDataFile(str(list_ten[i]),"Detection_1Dcode","dir_ImageProcessed",dir_ImageProcessed)
                                    self.file.updateDataFile(str(list_ten[i]),"Detection_1Dcode","dir_ImageRaw",dir_ImageRaw)
                                    self.file.updateDataFile(str(list_ten[i]),"Detection_1Dcode","dir_ImageRowProcessed",dir_ImageRowProcessed)


            self.func_loadFunctionSetting()

    def func_reloadFunc_2Dcode(self):
        self.numberEditCliced=1
        self.var_2Dcode=Class_2Dcode(None)
        self.var_signal_2Dcode =self.var_2Dcode.func_getSignal_2Dcode()
        self.var_2Dcode.func_setFileConfig_2Dcode(self.var_datafileConfig)
        self.var_2Dcode.func_loadData_Main_2Dcode()
        self.var_signal_From_ER_2Dcode = self.var_2Dcode.func_get_signalForm_ER_2Dcode()
        self.var_signalCancel_2Dcode=self.var_2Dcode.func_getSignalCancel_2Dcode()
        self.var_signal_2Dcode.connect(self.func_loadFuncToMain)
        self.var_signal_From_ER_2Dcode.connect(self.func_show_AddTool)  
        self.var_signalCancel_2Dcode.connect(self.func_show_AddTool) 
 
        self.var_2Dcode.func_show_2Dcode()
        


############open Tool 2D###########
    def func_openTool(self): 

    ################# function 2D code #########
        self.var_2Dcode = Class_2Dcode(None)
        self.var_2Dcode.func_createFileConfig()
        
        self.var_signal_2Dcode =self.var_2Dcode.func_getSignal_2Dcode()
  
        self.var_signal_From_ER_2Dcode = self.var_2Dcode.func_get_signalForm_ER_2Dcode()
        self.var_signalCancel_2Dcode=self.var_2Dcode.func_getSignalCancel_2Dcode()
        self.var_signal_2Dcode.connect(self.func_loadFuncToMain)
        self.var_signal_From_ER_2Dcode.connect(self.func_show_AddTool)  
        self.var_signalCancel_2Dcode.connect(self.func_show_AddTool) 
 
        self.var_2Dcode.func_show_2Dcode()
        self.var_2Dcode.func_show_ER_2Dcode()
   

############open Tool 1D########### HUNG##########################
    #khi nhat nut add tool
    def func_openTool1D(self): 
        self.var_1Dcode = Class_1Dcode(None) 
        self.var_1Dcode.func_show_1Dcode()
        self.var_signal_OK_1Dcode=self.var_1Dcode.getSignal_OK()
        self.var_signal_OK_1Dcode.connect(self.func_loadFuncToMain_1D)

    def func_reloadFunc_1Dcode(self):
        self.var_1Dcode = Class_1Dcode(None) 
        self.var_1Dcode.func_show_1Dcode()
        self.var_signal_OK_1Dcode=self.var_1Dcode.getSignal_OK()
        self.var_signal_OK_1Dcode.connect(self.func_loadFunctionSetting)

    def func_loadFuncToMain_1D(self):
        self.var_Ui_formMain.frame_setupToolDetail_ModGuiMain_1.setHidden(True)
        self.var_Ui_formMain.frame_setupToolDetail_ModGuiMain.setHidden(True)
        self.var_Ui_formMain.frame_setupToolDetail_2Dcode.setHidden(False)
        print("load 1D")
        self.func_loadFunctionSetting()




########## Load function ######
    def func_loadFuncToMain(self):
        self.var_Ui_formMain.frame_setupToolDetail_ModGuiMain_1.setHidden(True)
        self.var_Ui_formMain.frame_setupToolDetail_ModGuiMain.setHidden(True)
        self.var_Ui_formMain.frame_setupToolDetail_2Dcode.setHidden(False)
        self.func_loadDataSetting_2Dcode()
        self.func_loadData_toFrom_2Dcode()
        self.func_loadFunctionSetting()
########## reload function#######
    def func_reloadFunc(self):
        self.numberEditCliced=1
        self.var_2Dcode.func_loadData_Main_2Dcode()
        self.var_2Dcode.func_show_2Dcode()
        self.var_2Dcode.func_set_NumberEditclicked_2Dode(self.numberEditCliced)
######### close main #############

    def func_close_FormMain(self):
        self.close()

######### func AddTools ####

    def func_show_func_AddTool(self):
        self.var_UiDlog_AddTool.show()

    def func_show_AddTool(self):
        #print( self.numberEditCliced)
        if  self.numberEditCliced==0:
            self.var_UiDlog_AddTool.show()
            self.var_2Dcode.close()
        else :
            self.func_loadFuncToMain()
            self.var_2Dcode.close()
 

        
######### LOAD 2D CODE #################
    def func_loadDataSetting_2Dcode(self):
        self.var_fileText_2Dcode=self.var_2Dcode.func_getFileSetting_2Dcode()
        self.var_fileData_2Dcode =open(self.var_fileText_2Dcode,"r")
        self.var_dataSetting_2Dcode =self.var_fileData_2Dcode.readlines()
        self.tmp_line74 = self.var_dataSetting_2Dcode[74]
        self.tmp_line75 = self.var_dataSetting_2Dcode[75]
        self.tmp_line76 = self.var_dataSetting_2Dcode[76]
        self.tmp_line77 = self.var_dataSetting_2Dcode[77]
        self.tmp_x0_2Dcode =self.tmp_line74[2:len(self.tmp_line74)]
        self.tmp_x0_2Dcode = self.tmp_x0_2Dcode.rstrip()


        self.tmp_y0_2Dcode =self.tmp_line75[2:len(self.tmp_line75)]
        self.tmp_y0_2Dcode = self.tmp_y0_2Dcode.rstrip()    


        self.tmp_x1_2Dcode =self.tmp_line76[2:len(self.tmp_line76)]
        self.tmp_x1_2Dcode = self.tmp_x1_2Dcode.rstrip() 

        self.tmp_y1_2Dcode =self.tmp_line77[2:len(self.tmp_line77)]
        self.tmp_y1_2Dcode = self.tmp_y1_2Dcode.rstrip() 
        self.tmp_line5=self.var_dataSetting_2Dcode[5]
     
        self.tmp_typeData_2Dcode=self.tmp_line5[2:len(self.tmp_line5)]
        self.tmp_typeData_2Dcode=self.tmp_typeData_2Dcode.rstrip()

        self.tmp_line17=self.var_dataSetting_2Dcode[17]  
        self.tmp_line17=self.tmp_line17.rstrip()
        if len(self.tmp_line17)!=1:
            self.tmp_startDigit_2Dcode=self.tmp_line17[2:len(self.tmp_line17)]
            self.tmp_startDigit_2Dcode=self.tmp_startDigit_2Dcode.rstrip()
        
        self.tmp_line18=self.var_dataSetting_2Dcode[18]  
        self.tmp_line18=self.tmp_line18.rstrip()
        if len(self.tmp_line18)!=1:
 
            self.tmp_DataLength_2Dcode=self.tmp_line18[2:len(self.tmp_line18)]
            self.tmp_DataLength_2Dcode=self.tmp_DataLength_2Dcode.rstrip()
        self.tmp_line19=self.var_dataSetting_2Dcode[19]  
        self.tmp_line19=self.tmp_line19.rstrip()
        if len(self.tmp_line19)!=1:
            self.tmp_splitData_2Dcode =self.tmp_line19[2]
            self.tmp_splitData_2Dcode=self.tmp_splitData_2Dcode.rstrip()
        self.tmp_line30=self.var_dataSetting_2Dcode[30]  
        self.tmp_line30=self.tmp_line30.rstrip()

        if len(self.tmp_line30)!=1:
            self.tmp_OutputLength_2Dcode=self.tmp_line30[2]
            self.tmp_OutputLength_2Dcode=self.tmp_OutputLength_2Dcode.rstrip()

    def func_loadData_toFrom_2Dcode(self):

        self.tmp_line73=self.var_dataSetting_2Dcode[73]  
        self.tmp_line73=self.tmp_line73.rstrip()
        if len(self.tmp_line73)!=1:
            self.tmp_dataReadedFull=self.tmp_line73[2:len(self.tmp_line73)]
            self.tmp_dataReadedFull=self.tmp_dataReadedFull.rstrip()
            self.var_Ui_formMain.label_tab3_showReadDataFull_2Dcode.setText(self.tmp_dataReadedFull)

        self.tmp_line57=self.var_dataSetting_2Dcode[57]  
        self.tmp_line57=self.tmp_line57.rstrip()
        if len(self.tmp_line57)!=1:
            self.tmp_dataReaded=self.tmp_line57[2:len(self.tmp_line57)]
            self.tmp_dataReaded=self.tmp_dataReaded.rstrip()
            self.var_Ui_formMain.label_tab1_showDataReaded_2Dcode.setText(self.tmp_dataReaded)

        self.tmp_line62=self.var_dataSetting_2Dcode[62]  
        self.tmp_line62=self.tmp_line62.rstrip()
        if len(self.tmp_line62)!=1:
            self.tmp_lengthDataMeasure=self.tmp_line62[2:len(self.tmp_line62)]
            self.tmp_lengthDataMeasure=self.tmp_lengthDataMeasure.rstrip()
            self.var_Ui_formMain.label_tab4_showLengDataCode_2Dcode.setText(self.tmp_lengthDataMeasure)       

        self.tmp_line58=self.var_dataSetting_2Dcode[58]  
        self.tmp_line58=self.tmp_line58.rstrip()
        if len(self.tmp_line58)!=1:
            self.tmp_dataCopy=self.tmp_line58[2:len(self.tmp_line58)]
            self.tmp_dataCopy=self.tmp_dataCopy.rstrip()
            self.var_Ui_formMain.label_tab1_showDataReferen_2Dcode.setText(self.tmp_dataCopy)     
        self.tmp_line60=self.var_dataSetting_2Dcode[60]  
        self.tmp_line60=self.tmp_line60.rstrip()
        if len(self.tmp_line60)!=1:
            self.tmp_collationResult=self.tmp_line60[2:len(self.tmp_line60)]
            self.tmp_collationResult=self.tmp_collationResult.rstrip()
            self.var_Ui_formMain.label_tab1_showResultCollation_2Dcode.setText(self.tmp_collationResult) 

        self.tmp_line63=self.var_dataSetting_2Dcode[63]  
        self.tmp_line63=self.tmp_line63.rstrip()
        if len(self.tmp_line63)!=1:
            self.tmp_lengthData_lower=self.tmp_line63[2:len(self.tmp_line63)]
            self.tmp_lengthData_lower=self.tmp_lengthData_lower.rstrip()
            self.var_Ui_formMain.label_tab2_showLowLengDataRead_2Dcode.setText(self.tmp_lengthData_lower) 
        else :
            self.var_Ui_formMain.label_tab2_showLowLengDataRead_2Dcode.setText("-----")     
        self.tmp_line61=self.var_dataSetting_2Dcode[61]  
        self.tmp_line61=self.tmp_line61.rstrip()
        if len(self.tmp_line61)!=1:
            self.tmp_lengthData_upper=self.tmp_line61[2:len(self.tmp_line61)]
            self.tmp_lengthData_upper=self.tmp_lengthData_upper.rstrip()
            self.var_Ui_formMain.label_tab2_showUpLengDataRead_2Dcode.setText(self.tmp_lengthData_upper)
        else:
            self.var_Ui_formMain.label_tab2_showUpLengDataRead_2Dcode.setText("------")


        self.tmp_line64=self.var_dataSetting_2Dcode[64]  
        self.tmp_line64=self.tmp_line64.rstrip()
        if len(self.tmp_line64)!=1:
            self.tmp_posXData_upper=self.tmp_line64[2:len(self.tmp_line64)]
            self.tmp_posXData_upper=self.tmp_posXData_upper.rstrip()
            self.var_Ui_formMain.label_tab2_showUpPosX_2Dcode.setText(self.tmp_posXData_upper) 
        else :
            self.var_Ui_formMain.label_tab2_showUpPosX_2Dcode.setText("-----") 
 
        self.tmp_line65=self.var_dataSetting_2Dcode[65]  
        self.tmp_line65=self.tmp_line65.rstrip()
        if len(self.tmp_line65)!=1:
            self.tmp_posYData_upper=self.tmp_line65[2:len(self.tmp_line65)]
            self.tmp_posYData_upper=self.tmp_posYData_upper.rstrip()
            self.var_Ui_formMain.label_tab2_showUpPosY_2Dcode.setText(self.tmp_posYData_upper) 
        else :
            self.var_Ui_formMain.label_tab2_showUpPosY_2Dcode.setText("-----") 

        self.tmp_line68=self.var_dataSetting_2Dcode[68]  
        self.tmp_line68=self.tmp_line68.rstrip()
        if len(self.tmp_line68)!=1:
            self.tmp_posXData_lower=self.tmp_line68[2:len(self.tmp_line68)]
            self.tmp_posXData_lower=self.tmp_posXData_lower.rstrip()
            self.var_Ui_formMain.label_tab2_showLowPosX_2Dcode.setText(self.tmp_posXData_lower)     
        else:    
            self.var_Ui_formMain.label_tab2_showLowPosX_2Dcode.setText("-----") 
        self.tmp_line69=self.var_dataSetting_2Dcode[69]  
        self.tmp_line69=self.tmp_line69.rstrip()
        if len(self.tmp_line69)!=1:
            self.tmp_posYData_lower=self.tmp_line69[2:len(self.tmp_line69)]
            self.tmp_posYData_lower=self.tmp_posYData_lower.rstrip()
            self.var_Ui_formMain.label_tab2_showLowPosY_2Dcode.setText(self.tmp_posYData_lower)   
        else:
            self.var_Ui_formMain.label_tab2_showLowPosY_2Dcode.setText("-----")              


        self.tmp_line70=self.var_dataSetting_2Dcode[70]  
        self.tmp_line70=self.tmp_line70.rstrip()
        if len(self.tmp_line70)!=1:
            self.tmp_angleData_upper=self.tmp_line70[2:len(self.tmp_line70)]
            self.tmp_angleData_upper=self.tmp_angleData_upper.rstrip()
            self.var_Ui_formMain.label_tab2_showUpDetectAngle_2Dcode.setText(self.tmp_angleData_upper) 
        else:
            self.var_Ui_formMain.label_tab2_showUpDetectAngle_2Dcode.setText("----")             

        self.tmp_line72=self.var_dataSetting_2Dcode[72]  
        self.tmp_line72=self.tmp_line72.rstrip()
        if len(self.tmp_line72)!=1:
            self.tmp_angleData_lower=self.tmp_line72[2:len(self.tmp_line72)]
            self.tmp_angleData_lower=self.tmp_angleData_lower.rstrip()
            self.var_Ui_formMain.label_tab2_showLowDetectAngle_2Dcode.setText(self.tmp_angleData_lower) 
        else:  
            self.var_Ui_formMain.label_tab2_showLowDetectAngle_2Dcode.setText("----") 
    
#########################################

    def func_creatListTool(self):
        self.var_Ui_formMain.btn_showTool = []
        self.var_Ui_formMain.lab_showTool = []
        self.var_Ui_formMain.frame_2 = []       



        for i in range(100):
            self.var_Ui_formMain.btn_showTool.append(i)
            self.var_Ui_formMain.lab_showTool.append(i)
            self.var_Ui_formMain.frame_2.append(i)

            self.var_Ui_formMain.frame_2[i] = QtWidgets.QFrame(self.var_Ui_formMain.frame_showTool)
            self.var_Ui_formMain.frame_2[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.var_Ui_formMain.frame_2[i].setFrameShadow(QtWidgets.QFrame.Raised)
            self.var_Ui_formMain.frame_2[i].setObjectName("frame_2")
            self.var_Ui_formMain.verticalLayout_8 = QtWidgets.QVBoxLayout(self.var_Ui_formMain.frame_2[i])
            self.var_Ui_formMain.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
            self.var_Ui_formMain.verticalLayout_8.setSpacing(0)
            self.var_Ui_formMain.verticalLayout_8.setObjectName("verticalLayout_8")
            self.var_Ui_formMain.verticalLayout_7 = QtWidgets.QVBoxLayout()
            self.var_Ui_formMain.verticalLayout_7.setObjectName("verticalLayout_7")

            self.var_Ui_formMain.btn_showTool[i] = mouse_envent(self.var_Ui_formMain.frame_2[i])

            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.var_Ui_formMain.btn_showTool[i].sizePolicy().hasHeightForWidth())
            self.var_Ui_formMain.btn_showTool[i].setSizePolicy(sizePolicy)

            #self.var_Ui_1Dcode.btn_showTool[i] = QtWidgets.QPushButton(self.var_Ui_1Dcode.frame_2)
            self.var_Ui_formMain.btn_showTool[i].setMinimumSize(QtCore.QSize(150, 100))
            self.var_Ui_formMain.btn_showTool[i].setMaximumSize(QtCore.QSize(150, 150))
            
            self.var_Ui_formMain.btn_showTool[i].setObjectName("btn "+str(i))
            self.var_signalLoadFunction=self.var_Ui_formMain.btn_showTool[i].func_getSignal_btn()

            self.var_Ui_formMain.verticalLayout_7.addWidget(self.var_Ui_formMain.btn_showTool[i])
            self.var_Ui_formMain.lab_showTool[i] = QtWidgets.QLabel(self.var_Ui_formMain.frame_2[i])
            self.var_Ui_formMain.lab_showTool[i].setMinimumSize(QtCore.QSize(100, 0))
            self.var_Ui_formMain.lab_showTool[i].setMaximumSize(QtCore.QSize(100, 30))
            self.var_Ui_formMain.lab_showTool[i].setSizeIncrement(QtCore.QSize(100, 0))
            self.var_Ui_formMain.lab_showTool[i].setObjectName("lab_showTool"+str(i))
           # self.var_Ui_formMain.lab_showTool[i].setText("lab "+str(i))
          #  self.var_Ui_formMain.frame_showTool.setStyleSheet("background-color:   Red")  
           # self.var_Ui_formMain.frame_2.setStyleSheet("background-color:   Green")      

            self.var_Ui_formMain.verticalLayout_7.addWidget(self.var_Ui_formMain.lab_showTool[i])
            self.var_Ui_formMain.verticalLayout_8.addLayout(self.var_Ui_formMain.verticalLayout_7)
            self.var_Ui_formMain.horizontalLayout_4.addWidget(self.var_Ui_formMain.frame_2[i])

            self.var_Ui_formMain.btn_showTool[i].setHidden(1)
            self.var_Ui_formMain.lab_showTool[i].setHidden(1)
            self.var_Ui_formMain.frame_2[i].setHidden(1)



        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.var_Ui_formMain.horizontalLayout_4.addItem(spacerItem2)
    
    def func_loadFunctionSetting(self):
        self.var_file_goc =os.getcwd() 
        self.file_config=self.var_file_goc+'/config'
        self.list_file=os.listdir(self.file_config)
        self.list_file=sorted(self.list_file)

        for i in range(len(self.list_file)):


            self.var_file_txt=self.file_config+'/'+self.list_file[i]
            self.var_fileData =open(self.var_file_txt,"r")
            self.var_dataSetting =self.var_fileData.readlines()


            #Doc line dau tien trong fileconfig de check la Detection_2Dcode hay Detection_1Dcode
            self.tmp_line1=self.var_dataSetting[0]
            self.tmp_line1=self.tmp_line1.rstrip()

            if self.tmp_line1 == "Detection_2Dcode":
                self.var_imgRowProcessd=self.var_dataSetting[4]
                self.var_imgRowProcessd=self.var_imgRowProcessd.rstrip()
                self.var_Ui_formMain.btn_showTool[i].setObjectName(self.list_file[i])
                self.var_Ui_formMain.btn_showTool[i].setIcon(QtGui.QIcon(self.var_imgRowProcessd))  
                self.var_Ui_formMain.btn_showTool[i].setIconSize(QtCore.QSize(100,100))
                self.var_Ui_formMain.lab_showTool[i].setMinimumSize(QtCore.QSize(100, 0))
                self.var_Ui_formMain.lab_showTool[i].setMaximumSize(QtCore.QSize(100, 30))
                self.var_Ui_formMain.lab_showTool[i].setSizeIncrement(QtCore.QSize(100, 0))
                self.var_Ui_formMain.btn_showTool[i].setHidden(0)
                self.var_Ui_formMain.lab_showTool[i].setHidden(0)
                self.var_Ui_formMain.frame_2[i].setHidden(0)    

            elif self.tmp_line1=="[Detection_1Dcode]":
                num = self.file.func_convert_1to4Digit(i + 1)
                self.config = configparser.ConfigParser()
                self.config.read(var_dirFileConfig + "/"+ str(num) + ".ini")
                self.var_Ui_formMain.btn_showTool[i].setObjectName(self.list_file[i])
                self.var_Ui_formMain.btn_showTool[i].setIcon(QtGui.QIcon(self.config.get("Detection_1Dcode", "dir_imagerowprocessed")))
                self.var_Ui_formMain.btn_showTool[i].setIconSize(QtCore.QSize(100,100))
                self.var_Ui_formMain.lab_showTool[i].setMinimumSize(QtCore.QSize(100, 0))
                self.var_Ui_formMain.lab_showTool[i].setMaximumSize(QtCore.QSize(100, 30))
                self.var_Ui_formMain.lab_showTool[i].setSizeIncrement(QtCore.QSize(100, 0))
                self.var_Ui_formMain.btn_showTool[i].setHidden(0)
                self.var_Ui_formMain.lab_showTool[i].setHidden(0)
                self.var_Ui_formMain.frame_2[i].setHidden(0) 

class mouse_envent(QtWidgets.QPushButton):
    var_signal_formMain = pyqtSignal()
    var_signal_mouseRight = pyqtSignal()
   
    def __init__(self, parent, *args):
        super(mouse_envent, self).__init__(*args)
    def mousePressEvent(self,QMouseEvent):
            if QMouseEvent.buttons() == Qt.LeftButton:
                ten=self.objectName()
                file_goc =os.getcwd() #lay file goc
                self.file_txt_can=file_goc+'/config/'+ten# ten file txt du lieu
                self.var_filetxt=file_goc +"/0000.txt"
                self.var_fileData = open(self.var_filetxt, 'w')
                self.var_dataSetting=self.file_txt_can
                self.var_fileData.writelines(self.var_dataSetting)
                self.var_fileData.close()
                self.var_signal_formMain.emit()


            if QMouseEvent.buttons() == Qt.RightButton:
               msg = QtWidgets.QMessageBox()
               self.buttonReply = msg.question(self, 'Function Message', "Do you like delete function", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  
               if self.buttonReply == QMessageBox.Yes:
                    ten=self.objectName()
                    self.var_dataSetting=[0]*2
                    file_goc =os.getcwd() #lay file goc
                    self.file_txt_can=file_goc+'/config/'+ten# ten file txt du lieu
                    self.var_filetxt=file_goc +"/0000.txt"
                    self.var_fileData = open(self.var_filetxt, 'w')
                    self.var_dataSetting[0]=self.file_txt_can+"\n"
                    self.var_dataSetting[1]=ten[0:4]+"\n"
                    self.var_fileData.writelines(self.var_dataSetting)
                    self.var_fileData.close()
                    self.var_signal_mouseRight.emit()
                    

    def func_getSignal_btn(self):
        return self.var_signal_formMain
    def func_getSignalMouse_btn(self):
        return self.var_signal_mouseRight
 



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= Class_formMain(None)
   # mainWindow.show()
    sys.exit(app.exec_())


