from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from Detection_2DCode.DlogV.Ui_DlogV.I_DlogV_2Dcode import Ui_Class_DlogV_2Dcode


class Class_DlogV_2Dcode(QDialog):
    var_signal_V_2Dcode = pyqtSignal()
    def __init__(self, parent, *args):
        super(Class_DlogV_2Dcode, self).__init__(*args)
        self.var_Ui_V_2Dcode=Ui_Class_DlogV_2Dcode()
        self.var_Ui_V_2Dcode.setupUi(self)

        self.var_Ui_V_2Dcode.btn_OK_V_2Dcode.clicked.connect(self.func_createSignal_V_2Dcode)
   #     self.var_signal_V_2Dcode.connect(self.show_dia)
    def func_getSignal_V_2Dcode(self):
        return self.var_signal_V_2Dcode
    def func_createSignal_V_2Dcode(self):
        self.var_signal_V_2Dcode.emit()

    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= Class_DlogV_2Dcode(None)
    mainWindow.show()
    sys.exit(app.exec_())
