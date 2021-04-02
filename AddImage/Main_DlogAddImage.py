from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal, QTimer , QRect, QObject
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, \
    qApp, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from pypylon import pylon
import cv2
import sys
import os
import numpy as np 

from AddImage.Ui_addImage.I_DlogAddImage import Ui_Ui_Class_DlogAddImage
from Detection_1DCode.ActionFile import ActionFile

camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

var_dirFileOS = os.getcwd()
var_dirFileOS = var_dirFileOS.rstrip()
var_dirFileOS = var_dirFileOS.replace("/Detection_1DCode","")
var_dirFileImageLib = var_dirFileOS + "/" + "ImageLib"


class Class_DlogAddImage(QDialog):
    var_signalLoadFunction = pyqtSignal()
    var_signalDelete = pyqtSignal()
########################## Ham khoi tao cho class.............................
    def __init__(self, parent, *args):
        super(Class_DlogAddImage, self).__init__(*args)
        self.var_Ui_DlogAddImage = Ui_Ui_Class_DlogAddImage()
        self.var_Ui_DlogAddImage.setupUi(self)
       
        self.var_screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0, self.var_screen.height()*0.1, self.var_screen.width(), self.var_screen.height()*0.9)

        self.var_fileConfig_incon_zoom_in=var_dirFileOS+"/resources/icons/zoom-in.png"
        self.var_fileConfig_incon_zoom_out=var_dirFileOS+"/resources/icons/zoom-out.png"
        self.var_fileConfig_incon_zoom_fit=var_dirFileOS+"/resources/icons/zoom.png"
        self.var_Ui_DlogAddImage.btn_normalImage.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_fit))
        self.var_Ui_DlogAddImage.btn_zoomOut.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_out))
        self.var_Ui_DlogAddImage.btn_zoomIn.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_in)) 

        self.var_scaleFactor = 1.0  


        self.func_creatListImage()
        self.file = ActionFile(var_dirFileImageLib)
        self.timer = QTimer()
        self.timer.timeout.connect(self.func_viewImage)
        self.func_showImageList()
        self.var_Ui_DlogAddImage.btn_normalImage.clicked.connect(self.func_zoomFit)
        self.var_Ui_DlogAddImage.btn_zoomOut.clicked.connect(self.func_zoomOut)
        self.var_Ui_DlogAddImage.btn_zoomIn.clicked.connect(self.func_zoomIn) 

        self.var_Ui_DlogAddImage.btn_runing.clicked.connect(self.controlTimer)
        self.var_Ui_DlogAddImage.btn_run.clicked.connect(self.grapImage)
        self.var_Ui_DlogAddImage.btn_saveImage.clicked.connect(self.func_saveImage)
        self.var_Ui_DlogAddImage.btn_saveImage.clicked.connect(self.func_showImageList)
        #self.var_Ui_DlogAddImage.btn_deleteImage.clicked.connect(self.func_showImageList)
        # self.var_Ui_DlogAddImage.spinBox_X_Direction.valueChanged.connect(self.func_translationImage)
        # self.var_Ui_DlogAddImage.spinBox_Y_Direction.valueChanged.connect(self.func_translationImage)

        for i in range (1000):
            self.var_signalLoadFunction = self.var_Ui_DlogAddImage.btn_imageList[i].func_getSignal_btn()
            self.var_signalDelete = self.var_Ui_DlogAddImage.btn_imageList[i].func_getSignalMouse_btn()
            #self.var_signalLoadFunction.connect(self.)
            self.var_signalDelete.connect(self.func_deleteImage)

    def func_deleteImage(self):
        var_file_txt = var_dirFileOS + "/0000.txt" 
        var_fileData =open(var_file_txt,"r")
        var_dataSetting =var_fileData.readlines()
        tmp_line1 = var_dataSetting[0]
        tmp_line1 = tmp_line1.rstrip()
        var_fileData.close()
        os.remove(var_dirFileOS + "/0000.txt" )
        var_index = int(self.file.func_convert_1to4Digit(int(tmp_line1)))
        var_nameImage = self.var_Ui_DlogAddImage.lab_line1ListImage[var_index].text()

        var_openFileImage = open(var_dirFileImageLib + "/" + str(var_nameImage) + ".jpg" ,"r")
        os.remove(var_dirFileImageLib + "/" + str(var_nameImage) + ".jpg" )
        var_openFileImage.close()

        self.func_hidentImageList()
        self.func_showImageList()

    def func_showFuncAddImage(self):
        self.var_Ui_DlogAddImage.image()

    def func_closeFuncAddImage(self):
        self.var_Ui_DlogAddImage.close()

    def func_creatListImage(self):
        self.var_Ui_DlogAddImage.frame_14 = []
        self.var_Ui_DlogAddImage.btn_imageList = []
        self.var_Ui_DlogAddImage.lab_line1ListImage = []
        self.var_Ui_DlogAddImage.lab_line2ListImage = []
        self.var_Ui_DlogAddImage.lab_line3ListImage = []


        for i in range(1000):
            self.var_Ui_DlogAddImage.frame_14.append(i)
            self.var_Ui_DlogAddImage.btn_imageList.append(i)
            self.var_Ui_DlogAddImage.lab_line1ListImage.append(i)
            self.var_Ui_DlogAddImage.lab_line2ListImage.append(i)
            self.var_Ui_DlogAddImage.lab_line3ListImage.append(i)

            self.var_Ui_DlogAddImage.frame_14[i] = QtWidgets.QFrame(self.var_Ui_DlogAddImage.frame_13)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.var_Ui_DlogAddImage.frame_14[i].sizePolicy().hasHeightForWidth())
            self.var_Ui_DlogAddImage.frame_14[i].setSizePolicy(sizePolicy)
            self.var_Ui_DlogAddImage.frame_14[i].setMinimumSize(QtCore.QSize(400, 150))
            self.var_Ui_DlogAddImage.frame_14[i].setMaximumSize(QtCore.QSize(400, 150))
            self.var_Ui_DlogAddImage.frame_14[i].setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.var_Ui_DlogAddImage.frame_14[i].setFrameShadow(QtWidgets.QFrame.Raised)
            self.var_Ui_DlogAddImage.frame_14[i].setObjectName("var_Ui_DlogAddImage.frame_14[i]")
            self.var_Ui_DlogAddImage.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.var_Ui_DlogAddImage.frame_14[i])
            self.var_Ui_DlogAddImage.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
            self.var_Ui_DlogAddImage.horizontalLayout_15.setSpacing(0)
            self.var_Ui_DlogAddImage.horizontalLayout_15.setObjectName("var_Ui_DlogAddImage.horizontalLayout_15")
            self.var_Ui_DlogAddImage.horizontalLayout_14 = QtWidgets.QHBoxLayout()
            self.var_Ui_DlogAddImage.horizontalLayout_14.setObjectName("var_Ui_DlogAddImage.horizontalLayout_14")
            self.var_Ui_DlogAddImage.horizontalLayout_16 = QtWidgets.QHBoxLayout()
            self.var_Ui_DlogAddImage.horizontalLayout_16.setObjectName("var_Ui_DlogAddImage.horizontalLayout_16")
            self.var_Ui_DlogAddImage.btn_imageList[i] = mouse_envent(self.var_Ui_DlogAddImage.frame_14[i])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.var_Ui_DlogAddImage.btn_imageList[i].sizePolicy().hasHeightForWidth())
            self.var_Ui_DlogAddImage.btn_imageList[i].setSizePolicy(sizePolicy)
            self.var_Ui_DlogAddImage.btn_imageList[i].setMinimumSize(QtCore.QSize(140, 140))
            self.var_Ui_DlogAddImage.btn_imageList[i].setMaximumSize(QtCore.QSize(140, 140))
            self.var_Ui_DlogAddImage.btn_imageList[i].setObjectName("var_Ui_DlogAddImage.btn_imageList[i]")
            self.var_Ui_DlogAddImage.horizontalLayout_16.addWidget(self.var_Ui_DlogAddImage.btn_imageList[i])
            spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
            self.var_Ui_DlogAddImage.horizontalLayout_16.addItem(spacerItem5)
            self.var_Ui_DlogAddImage.verticalLayout_28 = QtWidgets.QVBoxLayout()
            self.var_Ui_DlogAddImage.verticalLayout_28.setObjectName("var_Ui_DlogAddImage.verticalLayout_28")
            self.var_Ui_DlogAddImage.lab_line1ListImage[i] = QtWidgets.QLabel(self.var_Ui_DlogAddImage.frame_14[i])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.var_Ui_DlogAddImage.lab_line1ListImage[i].sizePolicy().hasHeightForWidth())
            self.var_Ui_DlogAddImage.lab_line1ListImage[i].setSizePolicy(sizePolicy)
            self.var_Ui_DlogAddImage.lab_line1ListImage[i].setMinimumSize(QtCore.QSize(170, 44))
            self.var_Ui_DlogAddImage.lab_line1ListImage[i].setMaximumSize(QtCore.QSize(170, 44))
            self.var_Ui_DlogAddImage.lab_line1ListImage[i].setText("")
            self.var_Ui_DlogAddImage.lab_line1ListImage[i].setObjectName("var_Ui_DlogAddImage.lab_line1ListImage[i]")
            self.var_Ui_DlogAddImage.verticalLayout_28.addWidget(self.var_Ui_DlogAddImage.lab_line1ListImage[i])
            self.var_Ui_DlogAddImage.lab_line2ListImage[i] = QtWidgets.QLabel(self.var_Ui_DlogAddImage.frame_14[i])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.var_Ui_DlogAddImage.lab_line2ListImage[i].sizePolicy().hasHeightForWidth())
            self.var_Ui_DlogAddImage.lab_line2ListImage[i].setSizePolicy(sizePolicy)
            self.var_Ui_DlogAddImage.lab_line2ListImage[i].setMinimumSize(QtCore.QSize(170, 43))
            self.var_Ui_DlogAddImage.lab_line2ListImage[i].setMaximumSize(QtCore.QSize(170, 43))
            self.var_Ui_DlogAddImage.lab_line2ListImage[i].setText("")
            self.var_Ui_DlogAddImage.lab_line2ListImage[i].setObjectName("var_Ui_DlogAddImage.lab_line2ListImage[i]")
            self.var_Ui_DlogAddImage.verticalLayout_28.addWidget(self.var_Ui_DlogAddImage.lab_line2ListImage[i])
            self.var_Ui_DlogAddImage.lab_line3ListImage[i] = QtWidgets.QLabel(self.var_Ui_DlogAddImage.frame_14[i])
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.var_Ui_DlogAddImage.lab_line3ListImage[i].sizePolicy().hasHeightForWidth())
            self.var_Ui_DlogAddImage.lab_line3ListImage[i].setSizePolicy(sizePolicy)
            self.var_Ui_DlogAddImage.lab_line3ListImage[i].setMinimumSize(QtCore.QSize(170, 43))
            self.var_Ui_DlogAddImage.lab_line3ListImage[i].setMaximumSize(QtCore.QSize(170, 43))
            self.var_Ui_DlogAddImage.lab_line3ListImage[i].setText("")
            self.var_Ui_DlogAddImage.lab_line3ListImage[i].setObjectName("var_Ui_DlogAddImage.lab_line3ListImage[i]")
            self.var_Ui_DlogAddImage.verticalLayout_28.addWidget(self.var_Ui_DlogAddImage.lab_line3ListImage[i])
            self.var_Ui_DlogAddImage.horizontalLayout_16.addLayout(self.var_Ui_DlogAddImage.verticalLayout_28)
            self.var_Ui_DlogAddImage.horizontalLayout_14.addLayout(self.var_Ui_DlogAddImage.horizontalLayout_16)
            self.var_Ui_DlogAddImage.horizontalLayout_15.addLayout(self.var_Ui_DlogAddImage.horizontalLayout_14)
            self.var_Ui_DlogAddImage.verticalLayout_25.addWidget(self.var_Ui_DlogAddImage.frame_14[i])


            self.var_Ui_DlogAddImage.frame_14[i].setHidden(1)
            self.var_Ui_DlogAddImage.btn_imageList[i].setHidden(1)
            self.var_Ui_DlogAddImage.lab_line1ListImage[i].setHidden(1)
            self.var_Ui_DlogAddImage.lab_line2ListImage[i].setHidden(1)
            self.var_Ui_DlogAddImage.lab_line3ListImage[i].setHidden(1)

        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.var_Ui_DlogAddImage.verticalLayout_25.addItem(spacerItem6)

    def controlTimer(self):
        if not self.timer.isActive():
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            self.timer.start(20)
        else:
            self.timer.stop()
            camera.StopGrabbing()


    def func_viewImage(self):
            converter = pylon.ImageFormatConverter()
            converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
            grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grabResult.GrabSucceeded():
                self.image = converter.Convert(grabResult)
                self.image = self.image.GetArray()
                #self.image = cv2.resize(self.image,(1500,1051))
                self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB) #mau video duoc chuyen doi tro lai RGB de no la mau thuc 
                height, width,channel = self.image.shape
                self.image=cv2.resize(self.image,(int(self.var_scaleFactor*width),int(self.var_scaleFactor*height)), interpolation = cv2.INTER_CUBIC) 
                self.func_translationImage()
                self.func_rotationImage()
                height, width, channel =  self.image.shape
                step = channel * width
                self.showImage = QtGui.QImage(self.image.data,self.image.shape[1],self.image.shape[0],QtGui.QImage.Format_RGB888) 
                self.var_Ui_DlogAddImage.lab_ShowImage.setPixmap(QtGui.QPixmap.fromImage(self.showImage))  

    def grapImage(self):
            camera.StopGrabbing()
            camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            converter = pylon.ImageFormatConverter()
            converter.OutputPixelFormat = pylon.PixelType_BGR8packed
            converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
            grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grabResult.GrabSucceeded():
                self.image = converter.Convert(grabResult)
                self.image = self.image.GetArray()
                #self.image = cv2.resize(self.image,(1500,1051))
                self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2RGB) #mau video duoc chuyen doi tro lai RGB de no la mau thuc  
        
                height, width, channel = self.image.shape
                self.image=cv2.resize(self.image,(int(self.var_scaleFactor*width),int(self.var_scaleFactor*height)), interpolation = cv2.INTER_CUBIC) 
                height, width, channel =  self.image.shape
                step = channel * width

                self.showImage = QtGui.QImage(self.image.data,self.image.shape[1],self.image.shape[0],QtGui.QImage.Format_RGB888) #chuyen doi du lieu viudeo da doc thanh dinh dang QImage
                self.var_Ui_DlogAddImage.lab_ShowImage.setPixmap(QtGui.QPixmap.fromImage(self.showImage))  #Hien thi QImage trong Label hien thi video
            camera.StopGrabbing()


    def func_saveImage(self):
        self.saveImage(self.image)


    def saveImage(self, image):
        name = int(self.var_Ui_DlogAddImage.ledit_numImageSave.text())
        name = self.file.func_convert_1to4Digit(name)
        name = var_dirFileImageLib + "/" + str(name) + ".jpg"
        cv2.imwrite(name, image)

    def func_hidentImageList(self):
        for i in range(1000):
            self.var_Ui_DlogAddImage.frame_14[i].setHidden(1)
            self.var_Ui_DlogAddImage.btn_imageList[i].setHidden(1)
            self.var_Ui_DlogAddImage.lab_line1ListImage[i].setHidden(1)
            self.var_Ui_DlogAddImage.lab_line2ListImage[i].setHidden(1)
            self.var_Ui_DlogAddImage.lab_line3ListImage[i].setHidden(1)

    def func_showImageList(self):
        list_file = os.listdir(var_dirFileImageLib)
        list_file=sorted(list_file)
        var_length = len(os.listdir(var_dirFileImageLib))
        for i in range(var_length):

            self.var_Ui_DlogAddImage.btn_imageList[i].setObjectName(str(i))
            self.var_Ui_DlogAddImage.btn_imageList[i].setIcon(QtGui.QIcon(var_dirFileImageLib + "/"+ list_file[i]))  
            self.var_Ui_DlogAddImage.btn_imageList[i].setIconSize(QtCore.QSize(140,140))
            self.var_Ui_DlogAddImage.lab_line1ListImage[i].setText(list_file[i].replace(".jpg",""))

            self.var_Ui_DlogAddImage.frame_14[i].setHidden(0)
            self.var_Ui_DlogAddImage.btn_imageList[i].setHidden(0)
            self.var_Ui_DlogAddImage.lab_line1ListImage[i].setHidden(0)
            self.var_Ui_DlogAddImage.lab_line2ListImage[i].setHidden(0)
            self.var_Ui_DlogAddImage.lab_line3ListImage[i].setHidden(0)


    def func_zoomIn(self):
        self.func_scaleImage(0.01)
    def func_zoomOut(self):
        self.func_scaleImage(-0.01)
    def func_zoomFit(self):
            tmp_height, tmp_width,tmp_channel = self.image.shape
            tmp_step =  tmp_width*tmp_channel
            self.var_scaleFactor=1
            tmp_scale=int(self.var_scaleFactor*100)
            self.var_Ui_DlogAddImage.spinBox_slectScale.setValue(tmp_scale)
            self.image = QImage(self.image.data, tmp_width, tmp_height, tmp_step, QImage.Format_RGB888)
            tmp_pixmap = QPixmap.fromImage(self.image)
            self.var_Ui_DlogAddImage.lab_ShowImage.setPixmap(QPixmap.fromImage(self.image))
        
    def func_scaleImage(self, factor):
        self.var_scaleFactor += factor
        tmp_scale=int(self.var_scaleFactor*100)
        self.var_Ui_DlogAddImage.spinBox_slectScale.setValue(tmp_scale)
        # tmp_height, tmp_width,tmp_channel = self.image.shape
        # if self.var_scaleFactor<3 or self.var_scaleFactor>0.4 :
        #     self.tmp_imgScale=cv2.resize(self.image,(int(self.var_scaleFactor*tmp_width),int(self.var_scaleFactor*tmp_height)))
        #     tmp_height, tmp_width,tmp_channel = self.tmp_imgScale.shape
        #     tmp_step =  tmp_width*tmp_channel
        #     self.image = QImage(self.tmp_imgScale.data, tmp_width, tmp_height, tmp_step, QImage.Format_RGB888)
        #     pixmap = QPixmap.fromImage(self.image)
        #     self.var_Ui_DlogAddImage.lab_ShowImage.setPixmap(QPixmap.fromImage(self.image))


    def func_translationImage(self):
        self.var_Translation_X = int(self.var_Ui_DlogAddImage.spinBox_X_Direction.value())
        self.var_Translation_Y = int(self.var_Ui_DlogAddImage.spinBox_Y_Direction.value())
        rows,cols = self.image.shape[0:2]
        M = np.float32([[1,0,self.var_Translation_X],[0,1,self.var_Translation_Y]])
        self.image = cv2.warpAffine(self.image,M,(cols,rows))

    def func_rotationImage(self):
        self.var_Rotation_O = int(self.var_Ui_DlogAddImage.spinBox_O_Direction.value())
        rows,cols = self.image.shape[0:2]
        M = cv2.getRotationMatrix2D((cols/2,rows/2),self.var_Rotation_O,1)
        self.image = cv2.warpAffine(self.image,M,(cols,rows))

class mouse_envent(QtWidgets.QPushButton):
    var_signal_formMain = pyqtSignal()
    var_signal_mouseRight = pyqtSignal()
   
    def __init__(self, parent, *args):
        super(mouse_envent, self).__init__(*args)
    def mousePressEvent(self,QMouseEvent):
            if QMouseEvent.buttons() == Qt.LeftButton:
                ten = self.objectName()
                var_dataSetting = [0]
                var_filetxt= var_dirFileOS +"/0000.txt"
                var_fileData = open(var_filetxt, 'w')
                var_dataSetting[0]=ten[0:4]+"\n"
                var_fileData.writelines(var_dataSetting)
                var_fileData.close()
                self.var_signal_formMain.emit()


            if QMouseEvent.buttons() == Qt.RightButton:
               msg = QtWidgets.QMessageBox()
               self.buttonReply = msg.question(self, 'Function Message', "Do you like delete function", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  
               if self.buttonReply == QMessageBox.Yes:
                    ten = self.objectName()
                    var_dataSetting = [0]
                    var_filetxt= var_dirFileOS +"/0000.txt"
                    var_fileData = open(var_filetxt, 'w')
                    var_dataSetting[0]=ten[0:4]+"\n"
                    var_fileData.writelines(var_dataSetting)
                    var_fileData.close()
                    self.var_signal_mouseRight.emit()
                    
    def func_getSignal_btn(self):
        return self.var_signal_formMain
    def func_getSignalMouse_btn(self):
        return self.var_signal_mouseRight


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= Class_DlogAddImage(None)
    mainWindow.image()
    sys.exit(app.exec_())

