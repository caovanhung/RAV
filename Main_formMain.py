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


from Ui_mainForm.I_formMain import Ui_Class_formMain
from AddTool.Main_DlogAddTool import Class_DlogAddTool
from Detection_2DCode.Main_2Dcode import Class_2Dcode


class Class_formMain(QDialog):

    ### Khoi tao cac bien signal cua Main va thu cac signal cac ui setting.
    var_signal_formMain = pyqtSignal()
    var_signal_AddTool= pyqtSignal()
    var_signal_2Dcode = pyqtSignal()
    var_signal_From_ER_2Dcode = pyqtSignal()
    var_signalCancel_2Dcode = pyqtSignal()




########################## Ham khoi tao cho class.............................
    def __init__(self, parent, *args):
        super(Class_formMain, self).__init__(*args)
        #load UI cua 2D code
        self.var_Ui_formMain=Ui_Class_formMain()
        self.var_Ui_formMain.setupUi(self)
       
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

################# Add Tool ################################

        self.var_UiDlog_AddTool=Class_DlogAddTool(None)
        self.var_UiDlog_AddTool.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.var_signal_AddTool=self.var_UiDlog_AddTool.func_getSignal_AddTool()
        

        self.var_signal_AddTool.connect(self.func_openTool)

################# function 2D code #########
    #    self.var_2Dcode=Class_2Dcode(None)
     #   self.var_signal_2Dcode =self.var_2Dcode.func_getSignal_2Dcode()
  
     #   self.var_signal_From_ER_2Dcode = self.var_2Dcode.func_get_signalForm_ER_2Dcode()
     #   self.var_signal_2Dcode.connect(self.func_loadFuncToMain)
      #  self.var_signal_From_ER_2Dcode.connect(self.func_show_AddTool)  




        
###################### Main  ##############################################################        
        self.var_Ui_formMain.btn_RegisterImage_ModGuiMain.clicked.connect(self.func_close_FormMain)
        self.var_Ui_formMain.btn_addTool_ModGuiMain.clicked.connect(self.func_show_AddTool)
        self.var_Ui_formMain.btn_selectEditTool_ModGuiMain.clicked.connect(self.func_reloadFunc)
        self.show() 


############open Tool ###########
    def func_openTool(self): 

    ################# function 2D code #########
        self.var_2Dcode=Class_2Dcode(None)
        self.var_signal_2Dcode =self.var_2Dcode.func_getSignal_2Dcode()
  
        self.var_signal_From_ER_2Dcode = self.var_2Dcode.func_get_signalForm_ER_2Dcode()
        self.var_signalCancel_2Dcode=self.var_2Dcode.func_getSignalCancel_2Dcode()
        self.var_signal_2Dcode.connect(self.func_loadFuncToMain)
        self.var_signal_From_ER_2Dcode.connect(self.func_show_AddTool)  
        self.var_signalCancel_2Dcode.connect(self.func_show_AddTool)    
        self.var_2Dcode.func_show_2Dcode()
        self.var_2Dcode.func_show_ER_2Dcode()
            
########## Load function ######
    def func_loadFuncToMain(self):
        self.var_Ui_formMain.frame_setupToolDetail_ModGuiMain_1.setHidden(True)
        self.var_Ui_formMain.frame_setupToolDetail_ModGuiMain.setHidden(False)
########## reload function#######
    def func_reloadFunc(self):
        self.var_2Dcode.func_show_2Dcode()
######### close main #############
    def func_close_FormMain(self):
        self.close()
######### func AddTools ####
    def func_show_AddTool(self):
        self.var_UiDlog_AddTool.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= Class_formMain(None)
   # mainWindow.show()
    sys.exit(app.exec_())
