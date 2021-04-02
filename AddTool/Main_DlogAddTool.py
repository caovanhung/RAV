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


from AddTool.Ui_addTool.I_DlogAddTool import Ui_Class_DlogAddTool
#from Detection_2DCode.Main_2Dcode import Class_2Dcode


class Class_DlogAddTool(QDialog):

    ### Khoi tao cac bien signal cua Main va thu cac signal cac ui setting.
    var_signal_AddTool = pyqtSignal()
    var_signal1D_AddTool = pyqtSignal()
    



########################## Ham khoi tao cho class.............................
    def __init__(self, parent, *args):
        super(Class_DlogAddTool, self).__init__(*args)
        #load UI cua 2D code
        self.var_Ui_DlogAddTool=Ui_Class_DlogAddTool()
        self.var_Ui_DlogAddTool.setupUi(self)
       
        self.var_screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0, self.var_screen.height()*0.1, self.var_screen.width(), self.var_screen.height()*0.9)
        self.var_Ui_DlogAddTool.btn_Cancel_AddTool.clicked.connect(self.func_close_AddTool)
        self.var_Ui_DlogAddTool.btn_2Dcode_AddTool.clicked.connect(self.func_createSignal_AddTool)
        
     #   self.var_2Dcode=Class_2Dcode(None)

     ########################################Hung##################################################
        self.var_Ui_DlogAddTool.btn_1Dcode_AddTool.clicked.connect(self.func_createSignal1D_AddTool)

    def func_show1Dcode_AddTool(self):
        self.close()

    def func_createSignal1D_AddTool(self):
        self.var_signal1D_AddTool.emit()
        self.var_nameTool="1Dcode"
        self.close()
        
    def func_getSignal1D_AddTool(self):
        return self.var_signal1D_AddTool


     ################################################################################################



########## close dlog ADDtool ###########
    def func_close_AddTool(self):
        self.close()
############## 2D code #################
    def func_show2Dcode_AddTool(self):
     #   self.var_2Dcode.func_show_2Dcode()
        self.close()

    def func_createSignal_AddTool(self):
        self.var_signal_AddTool.emit()
        self.var_nameTool="2Dcode"
        self.close()
        
    def func_getSignal_AddTool(self):
        return self.var_signal_AddTool
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= Class_DlogAddTool(None)
    mainWindow.show()
    sys.exit(app.exec_())
