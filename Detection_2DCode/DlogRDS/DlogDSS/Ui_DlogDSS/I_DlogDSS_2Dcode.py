# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I_DlogDSS.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlogDSS_2Dcocde(object):
    def setupUi(self, DlogDSS_2Dcocde):
        DlogDSS_2Dcocde.setObjectName("DlogDSS_2Dcocde")
        DlogDSS_2Dcocde.resize(936, 816)
        self.verticalLayout = QtWidgets.QVBoxLayout(DlogDSS_2Dcocde)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(DlogDSS_2Dcocde)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame1 = QtWidgets.QFrame(self.frame)
        self.frame1.setMinimumSize(QtCore.QSize(0, 50))
        self.frame1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame1.setStyleSheet("background-color: rgb(32, 74, 135);\n"
"color: rgb(255, 255, 255);")
        self.frame1.setObjectName("frame1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_2.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.frame1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(20, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalFrame_3 = QtWidgets.QFrame(self.frame)
        self.horizontalFrame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame_3.setObjectName("horizontalFrame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_3.setContentsMargins(50, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lab_ReadData__DSS_2Dcode = QtWidgets.QLabel(self.horizontalFrame_3)
        self.lab_ReadData__DSS_2Dcode.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lab_ReadData__DSS_2Dcode.setFrameShape(QtWidgets.QFrame.Box)
        self.lab_ReadData__DSS_2Dcode.setText("")
        self.lab_ReadData__DSS_2Dcode.setObjectName("lab_ReadData__DSS_2Dcode")
        self.horizontalLayout_3.addWidget(self.lab_ReadData__DSS_2Dcode)
        self.btn_readDetialData = QtWidgets.QPushButton(self.horizontalFrame_3)
        self.btn_readDetialData.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_readDetialData.setObjectName("btn_readDetialData")
        self.horizontalLayout_3.addWidget(self.btn_readDetialData)
        self.verticalLayout_3.addWidget(self.horizontalFrame_3)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.frame)
        self.horizontalFrame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout.setContentsMargins(20, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_selecRange_DSS_2Dcode = QtWidgets.QFrame(self.horizontalFrame_2)
        self.frame_selecRange_DSS_2Dcode.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_selecRange_DSS_2Dcode.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame_selecRange_DSS_2Dcode.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_selecRange_DSS_2Dcode.setMidLineWidth(3)
        self.frame_selecRange_DSS_2Dcode.setObjectName("frame_selecRange_DSS_2Dcode")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_selecRange_DSS_2Dcode)
        self.gridLayout.setObjectName("gridLayout")
        self.ledit_readData8_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_readData8_DSS_2Dcode.setObjectName("ledit_readData8_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_readData8_DSS_2Dcode, 16, 6, 1, 1)
        self.ledit_startDigt5_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_startDigt5_DSS_2Dcode.setObjectName("ledit_startDigt5_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_startDigt5_DSS_2Dcode, 10, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 1)
        self.ledit_readData4_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_readData4_DSS_2Dcode.setObjectName("ledit_readData4_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_readData4_DSS_2Dcode, 8, 6, 1, 1)
        self.ledit_dataLength1_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_dataLength1_DSS_2Dcode.setObjectName("ledit_dataLength1_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_dataLength1_DSS_2Dcode, 2, 4, 1, 1)
        self.ledit_startDigt4_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_startDigt4_DSS_2Dcode.setObjectName("ledit_startDigt4_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_startDigt4_DSS_2Dcode, 8, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 11, 0, 1, 1)
        self.ledit_startDigt8_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_startDigt8_DSS_2Dcode.setObjectName("ledit_startDigt8_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_startDigt8_DSS_2Dcode, 16, 2, 1, 1)
        self.ledit_startDigt7_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_startDigt7_DSS_2Dcode.setObjectName("ledit_startDigt7_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_startDigt7_DSS_2Dcode, 14, 2, 1, 1)
        self.ledit_dataLength3_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_dataLength3_DSS_2Dcode.setObjectName("ledit_dataLength3_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_dataLength3_DSS_2Dcode, 6, 4, 1, 1)
        self.cbox_SlipRange3_DSS_2Dcode = QtWidgets.QCheckBox(self.frame_selecRange_DSS_2Dcode)
        self.cbox_SlipRange3_DSS_2Dcode.setObjectName("cbox_SlipRange3_DSS_2Dcode")
        self.gridLayout.addWidget(self.cbox_SlipRange3_DSS_2Dcode, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_selecRange_DSS_2Dcode)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 6, 1, 1)
        self.ledit_dataLength5_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_dataLength5_DSS_2Dcode.setObjectName("ledit_dataLength5_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_dataLength5_DSS_2Dcode, 10, 4, 1, 1)
        self.ledit_dataLength2_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_dataLength2_DSS_2Dcode.setObjectName("ledit_dataLength2_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_dataLength2_DSS_2Dcode, 4, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.ledit_startDigt6_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_startDigt6_DSS_2Dcode.setObjectName("ledit_startDigt6_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_startDigt6_DSS_2Dcode, 12, 2, 1, 1)
        self.ledit_dataLength4_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_dataLength4_DSS_2Dcode.setObjectName("ledit_dataLength4_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_dataLength4_DSS_2Dcode, 8, 4, 1, 1)
        self.ledit_dataLength7_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_dataLength7_DSS_2Dcode.setObjectName("ledit_dataLength7_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_dataLength7_DSS_2Dcode, 14, 4, 1, 1)
        self.ledit_dataLength8_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_dataLength8_DSS_2Dcode.setObjectName("ledit_dataLength8_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_dataLength8_DSS_2Dcode, 16, 4, 1, 1)
        self.cbox_SlipRange1_DSS_2Dcode = QtWidgets.QCheckBox(self.frame_selecRange_DSS_2Dcode)
        self.cbox_SlipRange1_DSS_2Dcode.setObjectName("cbox_SlipRange1_DSS_2Dcode")
        self.gridLayout.addWidget(self.cbox_SlipRange1_DSS_2Dcode, 2, 0, 1, 1)
        self.ledit_readData6_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_readData6_DSS_2Dcode.setObjectName("ledit_readData6_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_readData6_DSS_2Dcode, 12, 6, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 15, 0, 1, 1)
        self.cbox_SlipRange8_DSS_2Dcode = QtWidgets.QCheckBox(self.frame_selecRange_DSS_2Dcode)
        self.cbox_SlipRange8_DSS_2Dcode.setObjectName("cbox_SlipRange8_DSS_2Dcode")
        self.gridLayout.addWidget(self.cbox_SlipRange8_DSS_2Dcode, 16, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 5, 0, 1, 1)
        self.ledit_startDigt3_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_startDigt3_DSS_2Dcode.setObjectName("ledit_startDigt3_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_startDigt3_DSS_2Dcode, 6, 2, 1, 1)
        self.ledit_readData2_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_readData2_DSS_2Dcode.setObjectName("ledit_readData2_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_readData2_DSS_2Dcode, 4, 6, 1, 1)
        self.cbox_SlipRange4_DSS_2Dcode = QtWidgets.QCheckBox(self.frame_selecRange_DSS_2Dcode)
        self.cbox_SlipRange4_DSS_2Dcode.setObjectName("cbox_SlipRange4_DSS_2Dcode")
        self.gridLayout.addWidget(self.cbox_SlipRange4_DSS_2Dcode, 8, 0, 1, 1)
        self.cbox_SlipRange6_DSS_2Dcode = QtWidgets.QCheckBox(self.frame_selecRange_DSS_2Dcode)
        self.cbox_SlipRange6_DSS_2Dcode.setObjectName("cbox_SlipRange6_DSS_2Dcode")
        self.gridLayout.addWidget(self.cbox_SlipRange6_DSS_2Dcode, 12, 0, 1, 1)
        self.cbox_SlipRange5_DSS_2Dcode = QtWidgets.QCheckBox(self.frame_selecRange_DSS_2Dcode)
        self.cbox_SlipRange5_DSS_2Dcode.setObjectName("cbox_SlipRange5_DSS_2Dcode")
        self.gridLayout.addWidget(self.cbox_SlipRange5_DSS_2Dcode, 10, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 5, 1, 1)
        self.ledit_readData7_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_readData7_DSS_2Dcode.setObjectName("ledit_readData7_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_readData7_DSS_2Dcode, 14, 6, 1, 1)
        self.ledit_dataLength6_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_dataLength6_DSS_2Dcode.setObjectName("ledit_dataLength6_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_dataLength6_DSS_2Dcode, 12, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 3, 1, 1)
        self.cbox_SlipRange2_DSS_2Dcode = QtWidgets.QCheckBox(self.frame_selecRange_DSS_2Dcode)
        self.cbox_SlipRange2_DSS_2Dcode.setObjectName("cbox_SlipRange2_DSS_2Dcode")
        self.gridLayout.addWidget(self.cbox_SlipRange2_DSS_2Dcode, 4, 0, 1, 1)
        self.ledit_startDigt1_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_startDigt1_DSS_2Dcode.setObjectName("ledit_startDigt1_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_startDigt1_DSS_2Dcode, 2, 2, 1, 1)
        self.ledit_startDigt2_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_startDigt2_DSS_2Dcode.setObjectName("ledit_startDigt2_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_startDigt2_DSS_2Dcode, 4, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 1, 0, 1, 1)
        self.ledit_readData1_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_readData1_DSS_2Dcode.setMinimumSize(QtCore.QSize(400, 0))
        self.ledit_readData1_DSS_2Dcode.setObjectName("ledit_readData1_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_readData1_DSS_2Dcode, 2, 6, 1, 1)
        self.ledit_readData5_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_readData5_DSS_2Dcode.setObjectName("ledit_readData5_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_readData5_DSS_2Dcode, 10, 6, 1, 1)
        self.ledit_readData3_DSS_2Dcode = QtWidgets.QLineEdit(self.frame_selecRange_DSS_2Dcode)
        self.ledit_readData3_DSS_2Dcode.setObjectName("ledit_readData3_DSS_2Dcode")
        self.gridLayout.addWidget(self.ledit_readData3_DSS_2Dcode, 6, 6, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 3, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 7, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 13, 0, 1, 1)
        self.cbox_SlipRange7_DSS_2Dcode = QtWidgets.QCheckBox(self.frame_selecRange_DSS_2Dcode)
        self.cbox_SlipRange7_DSS_2Dcode.setObjectName("cbox_SlipRange7_DSS_2Dcode")
        self.gridLayout.addWidget(self.cbox_SlipRange7_DSS_2Dcode, 14, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_selecRange_DSS_2Dcode)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_selecRange_DSS_2Dcode)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_selecRange_DSS_2Dcode)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.btn_selectRange1_DSS_2Dcode = QtWidgets.QPushButton(self.frame_selecRange_DSS_2Dcode)
        self.btn_selectRange1_DSS_2Dcode.setObjectName("btn_selectRange1_DSS_2Dcode")
        self.gridLayout.addWidget(self.btn_selectRange1_DSS_2Dcode, 2, 7, 1, 1)
        self.btn_selectRange2_DSS_2Dcode = QtWidgets.QPushButton(self.frame_selecRange_DSS_2Dcode)
        self.btn_selectRange2_DSS_2Dcode.setObjectName("btn_selectRange2_DSS_2Dcode")
        self.gridLayout.addWidget(self.btn_selectRange2_DSS_2Dcode, 4, 7, 1, 1)
        self.btn_selectRange3_DSS_2Dcode = QtWidgets.QPushButton(self.frame_selecRange_DSS_2Dcode)
        self.btn_selectRange3_DSS_2Dcode.setObjectName("btn_selectRange3_DSS_2Dcode")
        self.gridLayout.addWidget(self.btn_selectRange3_DSS_2Dcode, 6, 7, 1, 1)
        self.btn_selectRange4_DSS_2Dcode = QtWidgets.QPushButton(self.frame_selecRange_DSS_2Dcode)
        self.btn_selectRange4_DSS_2Dcode.setObjectName("btn_selectRange4_DSS_2Dcode")
        self.gridLayout.addWidget(self.btn_selectRange4_DSS_2Dcode, 8, 7, 1, 1)
        self.btn_selectRange5_DSS_2Dcode = QtWidgets.QPushButton(self.frame_selecRange_DSS_2Dcode)
        self.btn_selectRange5_DSS_2Dcode.setObjectName("btn_selectRange5_DSS_2Dcode")
        self.gridLayout.addWidget(self.btn_selectRange5_DSS_2Dcode, 10, 7, 1, 1)
        self.btn_selectRange6_DSS_2Dcode = QtWidgets.QPushButton(self.frame_selecRange_DSS_2Dcode)
        self.btn_selectRange6_DSS_2Dcode.setObjectName("btn_selectRange6_DSS_2Dcode")
        self.gridLayout.addWidget(self.btn_selectRange6_DSS_2Dcode, 12, 7, 1, 1)
        self.btn_selectRange7_DSS_2Dcode = QtWidgets.QPushButton(self.frame_selecRange_DSS_2Dcode)
        self.btn_selectRange7_DSS_2Dcode.setObjectName("btn_selectRange7_DSS_2Dcode")
        self.gridLayout.addWidget(self.btn_selectRange7_DSS_2Dcode, 14, 7, 1, 1)
        self.btn_selectRange8_DSS_2Dcode = QtWidgets.QPushButton(self.frame_selecRange_DSS_2Dcode)
        self.btn_selectRange8_DSS_2Dcode.setObjectName("btn_selectRange8_DSS_2Dcode")
        self.gridLayout.addWidget(self.btn_selectRange8_DSS_2Dcode, 16, 7, 1, 1)
        self.horizontalLayout.addWidget(self.frame_selecRange_DSS_2Dcode)
        self.verticalLayout_3.addWidget(self.horizontalFrame_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, 10, -1)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.btn_OK_DSS_2Dcode = QtWidgets.QPushButton(self.frame)
        self.btn_OK_DSS_2Dcode.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(255, 255, 255);")
        self.btn_OK_DSS_2Dcode.setObjectName("btn_OK_DSS_2Dcode")
        self.horizontalLayout_2.addWidget(self.btn_OK_DSS_2Dcode)
        self.btn_Cancel_DSS_2Dcode = QtWidgets.QPushButton(self.frame)
        self.btn_Cancel_DSS_2Dcode.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"color: rgb(255, 255, 255);")
        self.btn_Cancel_DSS_2Dcode.setObjectName("btn_Cancel_DSS_2Dcode")
        self.horizontalLayout_2.addWidget(self.btn_Cancel_DSS_2Dcode)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(DlogDSS_2Dcocde)
        QtCore.QMetaObject.connectSlotsByName(DlogDSS_2Dcocde)

    def retranslateUi(self, DlogDSS_2Dcocde):
        _translate = QtCore.QCoreApplication.translate
        DlogDSS_2Dcocde.setWindowTitle(_translate("DlogDSS_2Dcocde", "Dialog"))
        self.label.setText(_translate("DlogDSS_2Dcocde", "<html><head/><body><p><span style=\" font-size:18pt;\">Data Split Setting</span></p></body></html>"))
        self.label_2.setText(_translate("DlogDSS_2Dcocde", "Read Data "))
        self.btn_readDetialData.setText(_translate("DlogDSS_2Dcocde", ">>>"))
        self.cbox_SlipRange3_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Slipt Range3"))
        self.label_7.setText(_translate("DlogDSS_2Dcocde", "Read Data"))
        self.cbox_SlipRange1_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Slipt Range1"))
        self.cbox_SlipRange8_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Slipt Range8"))
        self.cbox_SlipRange4_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Slipt Range4"))
        self.cbox_SlipRange6_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Slipt Range6"))
        self.cbox_SlipRange5_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Slipt Range5"))
        self.cbox_SlipRange2_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Slipt Range2"))
        self.cbox_SlipRange7_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Slipt Range7"))
        self.label_6.setText(_translate("DlogDSS_2Dcocde", "Start Digit"))
        self.label_4.setText(_translate("DlogDSS_2Dcocde", "Enabled"))
        self.label_5.setText(_translate("DlogDSS_2Dcocde", "Data length"))
        self.btn_selectRange1_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Select Range"))
        self.btn_selectRange2_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Select Range"))
        self.btn_selectRange3_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Select Range"))
        self.btn_selectRange4_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Select Range"))
        self.btn_selectRange5_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Select Range"))
        self.btn_selectRange6_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Select Range"))
        self.btn_selectRange7_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Select Range"))
        self.btn_selectRange8_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Select Range"))
        self.btn_OK_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "OK"))
        self.btn_Cancel_DSS_2Dcode.setText(_translate("DlogDSS_2Dcocde", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DlogDSS_2Dcocde = QtWidgets.QDialog()
    ui = Ui_DlogDSS_2Dcocde()
    ui.setupUi(DlogDSS_2Dcocde)
    DlogDSS_2Dcocde.show()
    sys.exit(app.exec_())

