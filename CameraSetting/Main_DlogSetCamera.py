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


from CameraSetting.UI_CameraSetting.I_CameraSetting import Ui_Class_CameraSetting

var_dirFileOS = os.getcwd()
var_dirFileOS = var_dirFileOS.rstrip()

class Class_CameraSetting(QDialog):
    def __init__(self, parent, *args):
        super(Class_CameraSetting, self).__init__(*args)
        self.var_Ui_CameraSetting = Ui_Class_CameraSetting()
        self.var_Ui_CameraSetting.setupUi(self)
        self.var_screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(0, self.var_screen.height()*0.1, self.var_screen.width(), self.var_screen.height()*0.9)

        self.var_fileConfig_incon_zoom_in = var_dirFileOS +"/resources/icons/zoom-in.png"
        self.var_fileConfig_incon_zoom_out = var_dirFileOS +"/resources/icons/zoom-out.png"
        self.var_fileConfig_incon_zoom_fit = var_dirFileOS +"/resources/icons/zoom.png"
        self.var_Ui_CameraSetting.btn_ZoomNormal.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_fit))
        self.var_Ui_CameraSetting.btn_ZoomOut.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_out))
        self.var_Ui_CameraSetting.btn_ZoomIn.setIcon(QtGui.QIcon(self.var_fileConfig_incon_zoom_in)) 