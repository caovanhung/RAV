from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from DlogER.Ui_DlogER.I_DlogER_2Dcode import Ui_Class_DlogER_2Dcode


class Class_DlogER_2Dcode(QDialog):
    var_signal_ER_2Dcode = pyqtSignal()
    var_signal_ER_Cancel_2Dcode = pyqtSignal()
    def __init__(self, parent, *args):
        super(Class_DlogER_2Dcode, self).__init__(*args)
        self.var_Ui_ER_2Dcode=Ui_Class_DlogER_2Dcode()
        self.var_Ui_ER_2Dcode.setupUi(self)
        self.var_Ui_ER_2Dcode.btn_OK_editRegion_2Dcode.clicked.connect(self.func_createSignal_ER_2Dcode)
        self.var_Ui_ER_2Dcode.btn_Cancel_editRegion_2Dcode.clicked.connect(self.func_createCancelSignal_ER_2Dcode)   



    def func_getSignal_ER_2Dcode(self):
        return self.var_signal_ER_2Dcode
    
    def func_createSignal_ER_2Dcode(self):
         self.var_signal_ER_2Dcode.emit()


    def func_createCancelSignal_ER_2Dcode(self):
         self.var_signal_ER_Cancel_2Dcode.emit()

    def func_getCancelSignal_ER_2Dcode(self):
        return self.var_signal_ER_Cancel_2Dcode

    def func_setConfigData_ER_2Dcode(self):
        self.var_Inspection_Region = self.var_Ui_ER_2Dcode.comBox_InspectionRegion_2Dcode.currentText()
        self.var_nameText = self.var_Ui_ER_2Dcode.btn_referencImage_2Dcode.text()
        return self.var_Inspection_Region,self.var_nameText


        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow= Class_DlogER_2Dcode(None)
    mainWindow.show()
    sys.exit(app.exec_())
