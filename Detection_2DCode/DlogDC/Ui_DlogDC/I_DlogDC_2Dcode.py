# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I_DlogDC_2Dcode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Class_DlogDC_2Dcode(object):
    def setupUi(self, Class_DlogDC_2Dcode):
        Class_DlogDC_2Dcode.setObjectName("Class_DlogDC_2Dcode")
        Class_DlogDC_2Dcode.resize(494, 717)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Class_DlogDC_2Dcode)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget_2 = QtWidgets.QWidget(Class_DlogDC_2Dcode)
        self.horizontalWidget_2.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalWidget_2.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label.setStyleSheet("color: rgb(238, 238, 236);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.horizontalWidget_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(Class_DlogDC_2Dcode)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -71, 474, 652))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(400, 650))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalFrame_7 = QtWidgets.QFrame(self.frame)
        self.verticalFrame_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.verticalFrame_7.setObjectName("verticalFrame_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalFrame_7)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalFrame_3 = QtWidgets.QFrame(self.verticalFrame_7)
        self.horizontalFrame_3.setMinimumSize(QtCore.QSize(0, 50))
        self.horizontalFrame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame_3.setStyleSheet("\n"
"background-color: rgb(136, 138, 133);\n"
"color: rgb(0, 0, 0);")
        self.horizontalFrame_3.setObjectName("horizontalFrame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_4.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.horizontalFrame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_10.addWidget(self.horizontalFrame_3)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.verticalFrame_7)
        self.horizontalFrame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.horizontalFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_3.setContentsMargins(30, 10, -1, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalFrame_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.combox_CodeType_DC_2Dcode = QtWidgets.QComboBox(self.horizontalFrame_2)
        self.combox_CodeType_DC_2Dcode.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.combox_CodeType_DC_2Dcode.setObjectName("combox_CodeType_DC_2Dcode")
        self.combox_CodeType_DC_2Dcode.addItem("")
        self.combox_CodeType_DC_2Dcode.addItem("")
        self.combox_CodeType_DC_2Dcode.addItem("")
        self.combox_CodeType_DC_2Dcode.addItem("")
        self.combox_CodeType_DC_2Dcode.addItem("")
        self.horizontalLayout_3.addWidget(self.combox_CodeType_DC_2Dcode)
        self.verticalLayout_10.addWidget(self.horizontalFrame_2)
        self.verticalLayout_6.addWidget(self.verticalFrame_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalFrame_8 = QtWidgets.QFrame(self.frame)
        self.verticalFrame_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalFrame_8.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.verticalFrame_8.setObjectName("verticalFrame_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalFrame_8)
        self.verticalLayout_11.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.verticalFrame_8)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.verticalLayout_9.addWidget(self.verticalFrame_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.btn_AutoTuring_DC_2Dcode = QtWidgets.QPushButton(self.frame_2)
        self.btn_AutoTuring_DC_2Dcode.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.btn_AutoTuring_DC_2Dcode.setObjectName("btn_AutoTuring_DC_2Dcode")
        self.horizontalLayout_15.addWidget(self.btn_AutoTuring_DC_2Dcode)
        self.verticalLayout_13.addLayout(self.horizontalLayout_15)
        self.horizontalFrame_8 = QtWidgets.QFrame(self.frame_2)
        self.horizontalFrame_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.horizontalFrame_8.setObjectName("horizontalFrame_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalFrame_8)
        self.horizontalLayout_14.setContentsMargins(20, 0, -1, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_5 = QtWidgets.QLabel(self.horizontalFrame_8)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_14.addWidget(self.label_5)
        self.verticalLayout_13.addWidget(self.horizontalFrame_8)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.cbox_CodeResolution_DC_2Dcode = QtWidgets.QCheckBox(self.frame_2)
        self.cbox_CodeResolution_DC_2Dcode.setObjectName("cbox_CodeResolution_DC_2Dcode")
        self.horizontalLayout_12.addWidget(self.cbox_CodeResolution_DC_2Dcode)
        self.verticalLayout_13.addLayout(self.horizontalLayout_12)
        self.horizontalFrame_6 = QtWidgets.QFrame(self.frame_2)
        self.horizontalFrame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalFrame_6.setObjectName("horizontalFrame_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_11.setContentsMargins(1, 0, 10, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.tedit_CodeResolution_DC_2Dcode = QtWidgets.QTextEdit(self.horizontalFrame_6)
        self.tedit_CodeResolution_DC_2Dcode.setMaximumSize(QtCore.QSize(80, 30))
        self.tedit_CodeResolution_DC_2Dcode.setObjectName("tedit_CodeResolution_DC_2Dcode")
        self.horizontalLayout_11.addWidget(self.tedit_CodeResolution_DC_2Dcode)
        self.verticalLayout_13.addWidget(self.horizontalFrame_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(20, -1, 10, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.cbox_ReferenceContrast_DC_2Dcode = QtWidgets.QCheckBox(self.frame_2)
        self.cbox_ReferenceContrast_DC_2Dcode.setObjectName("cbox_ReferenceContrast_DC_2Dcode")
        self.horizontalLayout_10.addWidget(self.cbox_ReferenceContrast_DC_2Dcode)
        self.comBox_ReferenceContrast_DC_2Dcode = QtWidgets.QComboBox(self.frame_2)
        self.comBox_ReferenceContrast_DC_2Dcode.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.comBox_ReferenceContrast_DC_2Dcode.setObjectName("comBox_ReferenceContrast_DC_2Dcode")
        self.comBox_ReferenceContrast_DC_2Dcode.addItem("")
        self.comBox_ReferenceContrast_DC_2Dcode.addItem("")
        self.comBox_ReferenceContrast_DC_2Dcode.addItem("")
        self.comBox_ReferenceContrast_DC_2Dcode.addItem("")
        self.comBox_ReferenceContrast_DC_2Dcode.addItem("")
        self.horizontalLayout_10.addWidget(self.comBox_ReferenceContrast_DC_2Dcode)
        self.verticalLayout_13.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(20, -1, 10, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cbox_NumberCells_DC_2Dcode = QtWidgets.QCheckBox(self.frame_2)
        self.cbox_NumberCells_DC_2Dcode.setObjectName("cbox_NumberCells_DC_2Dcode")
        self.horizontalLayout_9.addWidget(self.cbox_NumberCells_DC_2Dcode)
        self.combox_NumberCell_DC_2Dcode = QtWidgets.QComboBox(self.frame_2)
        self.combox_NumberCell_DC_2Dcode.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.combox_NumberCell_DC_2Dcode.setObjectName("combox_NumberCell_DC_2Dcode")
        self.combox_NumberCell_DC_2Dcode.addItem("")
        self.combox_NumberCell_DC_2Dcode.addItem("")
        self.combox_NumberCell_DC_2Dcode.addItem("")
        self.combox_NumberCell_DC_2Dcode.addItem("")
        self.combox_NumberCell_DC_2Dcode.addItem("")
        self.horizontalLayout_9.addWidget(self.combox_NumberCell_DC_2Dcode)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setContentsMargins(20, -1, 10, -1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.cbox_CodeColor_DC_2Dcode = QtWidgets.QCheckBox(self.frame_2)
        self.cbox_CodeColor_DC_2Dcode.setObjectName("cbox_CodeColor_DC_2Dcode")
        self.horizontalLayout_17.addWidget(self.cbox_CodeColor_DC_2Dcode)
        self.combox_CodeColor_DC_2Dcode = QtWidgets.QComboBox(self.frame_2)
        self.combox_CodeColor_DC_2Dcode.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.combox_CodeColor_DC_2Dcode.setObjectName("combox_CodeColor_DC_2Dcode")
        self.combox_CodeColor_DC_2Dcode.addItem("")
        self.combox_CodeColor_DC_2Dcode.addItem("")
        self.combox_CodeColor_DC_2Dcode.addItem("")
        self.horizontalLayout_17.addWidget(self.combox_CodeColor_DC_2Dcode)
        self.verticalLayout_13.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(20, -1, 10, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cbox_MirroredReading_DC_2Dcode = QtWidgets.QCheckBox(self.frame_2)
        self.cbox_MirroredReading_DC_2Dcode.setObjectName("cbox_MirroredReading_DC_2Dcode")
        self.horizontalLayout_8.addWidget(self.cbox_MirroredReading_DC_2Dcode)
        self.combox_MirroredReading_DC_2Dcode = QtWidgets.QComboBox(self.frame_2)
        self.combox_MirroredReading_DC_2Dcode.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.combox_MirroredReading_DC_2Dcode.setObjectName("combox_MirroredReading_DC_2Dcode")
        self.combox_MirroredReading_DC_2Dcode.addItem("")
        self.combox_MirroredReading_DC_2Dcode.addItem("")
        self.combox_MirroredReading_DC_2Dcode.addItem("")
        self.horizontalLayout_8.addWidget(self.combox_MirroredReading_DC_2Dcode)
        self.verticalLayout_13.addLayout(self.horizontalLayout_8)
        self.verticalFrame_81 = QtWidgets.QFrame(self.frame_2)
        self.verticalFrame_81.setMaximumSize(QtCore.QSize(16777215, 40))
        self.verticalFrame_81.setObjectName("verticalFrame_81")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.verticalFrame_81)
        self.horizontalLayout_16.setContentsMargins(20, 0, 10, 0)
        self.horizontalLayout_16.setSpacing(60)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.cbox_BaseAngle_DC_2Dcode = QtWidgets.QCheckBox(self.verticalFrame_81)
        self.cbox_BaseAngle_DC_2Dcode.setObjectName("cbox_BaseAngle_DC_2Dcode")
        self.horizontalLayout_16.addWidget(self.cbox_BaseAngle_DC_2Dcode)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.tedit_BaseAngle_DC_2Dcode = QtWidgets.QTextEdit(self.verticalFrame_81)
        self.tedit_BaseAngle_DC_2Dcode.setMaximumSize(QtCore.QSize(80, 30))
        self.tedit_BaseAngle_DC_2Dcode.setObjectName("tedit_BaseAngle_DC_2Dcode")
        self.horizontalLayout_16.addWidget(self.tedit_BaseAngle_DC_2Dcode)
        self.verticalLayout_13.addWidget(self.verticalFrame_81)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalFrame_82 = QtWidgets.QFrame(self.frame)
        self.verticalFrame_82.setMaximumSize(QtCore.QSize(16777215, 60))
        self.verticalFrame_82.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.verticalFrame_82.setObjectName("verticalFrame_82")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalFrame_82)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_8 = QtWidgets.QLabel(self.verticalFrame_82)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_14.addWidget(self.label_8)
        self.verticalLayout_8.addWidget(self.verticalFrame_82)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalFrame_11 = QtWidgets.QFrame(self.frame)
        self.verticalFrame_11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalFrame_11.setObjectName("verticalFrame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.verticalFrame_11)
        self.horizontalLayout_6.setContentsMargins(20, -1, 10, -1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.verticalFrame_11)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.verticalFrame_11)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.tedit_AngleRange_DC_2Dcode = QtWidgets.QTextEdit(self.verticalFrame_11)
        self.tedit_AngleRange_DC_2Dcode.setMaximumSize(QtCore.QSize(80, 16777215))
        self.tedit_AngleRange_DC_2Dcode.setObjectName("tedit_AngleRange_DC_2Dcode")
        self.horizontalLayout_6.addWidget(self.tedit_AngleRange_DC_2Dcode)
        self.verticalLayout_12.addWidget(self.verticalFrame_11)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(20, -1, 10, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.combox_ScaleVariation_DC_2Dcode = QtWidgets.QComboBox(self.frame)
        self.combox_ScaleVariation_DC_2Dcode.setObjectName("combox_ScaleVariation_DC_2Dcode")
        self.combox_ScaleVariation_DC_2Dcode.addItem("")
        self.combox_ScaleVariation_DC_2Dcode.addItem("")
        self.combox_ScaleVariation_DC_2Dcode.addItem("")
        self.combox_ScaleVariation_DC_2Dcode.addItem("")
        self.horizontalLayout_7.addWidget(self.combox_ScaleVariation_DC_2Dcode)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.verticalFrame_83 = QtWidgets.QFrame(self.frame)
        self.verticalFrame_83.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalFrame_83.setObjectName("verticalFrame_83")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.verticalFrame_83)
        self.horizontalLayout_18.setContentsMargins(20, -1, 10, -1)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_12 = QtWidgets.QLabel(self.verticalFrame_83)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_18.addWidget(self.label_12)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem4)
        self.tedit_Timeout_DC_2Dcode = QtWidgets.QTextEdit(self.verticalFrame_83)
        self.tedit_Timeout_DC_2Dcode.setMaximumSize(QtCore.QSize(80, 16777215))
        self.tedit_Timeout_DC_2Dcode.setObjectName("tedit_Timeout_DC_2Dcode")
        self.horizontalLayout_18.addWidget(self.tedit_Timeout_DC_2Dcode)
        self.verticalLayout_12.addWidget(self.verticalFrame_83)
        self.verticalLayout_8.addLayout(self.verticalLayout_12)
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addWidget(self.frame)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalFrame = QtWidgets.QFrame(Class_DlogDC_2Dcode)
        self.horizontalFrame.setMinimumSize(QtCore.QSize(0, 80))
        self.horizontalFrame.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(10, 0, 10, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.btn_OK_DC_2Dcode = QtWidgets.QPushButton(self.horizontalFrame)
        self.btn_OK_DC_2Dcode.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_OK_DC_2Dcode.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);")
        self.btn_OK_DC_2Dcode.setObjectName("btn_OK_DC_2Dcode")
        self.horizontalLayout.addWidget(self.btn_OK_DC_2Dcode)
        self.btn_Cancel_DC_2Dcode = QtWidgets.QPushButton(self.horizontalFrame)
        self.btn_Cancel_DC_2Dcode.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_Cancel_DC_2Dcode.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);")
        self.btn_Cancel_DC_2Dcode.setObjectName("btn_Cancel_DC_2Dcode")
        self.horizontalLayout.addWidget(self.btn_Cancel_DC_2Dcode)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Class_DlogDC_2Dcode)
        QtCore.QMetaObject.connectSlotsByName(Class_DlogDC_2Dcode)

    def retranslateUi(self, Class_DlogDC_2Dcode):
        _translate = QtCore.QCoreApplication.translate
        Class_DlogDC_2Dcode.setWindowTitle(_translate("Class_DlogDC_2Dcode", "Dialog"))
        self.label.setText(_translate("Class_DlogDC_2Dcode", "2D Code Reader   > Detection Conditions"))
        self.label_2.setText(_translate("Class_DlogDC_2Dcode", "Code Type"))
        self.label_3.setText(_translate("Class_DlogDC_2Dcode", "Code type"))
        self.combox_CodeType_DC_2Dcode.setItemText(0, _translate("Class_DlogDC_2Dcode", "Not Specified"))
        self.combox_CodeType_DC_2Dcode.setItemText(1, _translate("Class_DlogDC_2Dcode", "QR"))
        self.combox_CodeType_DC_2Dcode.setItemText(2, _translate("Class_DlogDC_2Dcode", "Micro QR"))
        self.combox_CodeType_DC_2Dcode.setItemText(3, _translate("Class_DlogDC_2Dcode", "DataMatrix"))
        self.combox_CodeType_DC_2Dcode.setItemText(4, _translate("Class_DlogDC_2Dcode", "Rectangular DataMatrix"))
        self.label_4.setText(_translate("Class_DlogDC_2Dcode", "Tuning Paramenters"))
        self.btn_AutoTuring_DC_2Dcode.setText(_translate("Class_DlogDC_2Dcode", "Auto-Turing"))
        self.label_5.setText(_translate("Class_DlogDC_2Dcode", "Manual  Setting"))
        self.cbox_CodeResolution_DC_2Dcode.setText(_translate("Class_DlogDC_2Dcode", "Code Resolution (pixel)"))
        self.cbox_ReferenceContrast_DC_2Dcode.setText(_translate("Class_DlogDC_2Dcode", "Reference Contrast"))
        self.comBox_ReferenceContrast_DC_2Dcode.setToolTip(_translate("Class_DlogDC_2Dcode", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.comBox_ReferenceContrast_DC_2Dcode.setItemText(0, _translate("Class_DlogDC_2Dcode", "Highest"))
        self.comBox_ReferenceContrast_DC_2Dcode.setItemText(1, _translate("Class_DlogDC_2Dcode", "High"))
        self.comBox_ReferenceContrast_DC_2Dcode.setItemText(2, _translate("Class_DlogDC_2Dcode", "Normal"))
        self.comBox_ReferenceContrast_DC_2Dcode.setItemText(3, _translate("Class_DlogDC_2Dcode", "Low"))
        self.comBox_ReferenceContrast_DC_2Dcode.setItemText(4, _translate("Class_DlogDC_2Dcode", "Lowest"))
        self.cbox_NumberCells_DC_2Dcode.setText(_translate("Class_DlogDC_2Dcode", "The Number of Cells"))
        self.combox_NumberCell_DC_2Dcode.setItemText(0, _translate("Class_DlogDC_2Dcode", "Any"))
        self.combox_NumberCell_DC_2Dcode.setItemText(1, _translate("Class_DlogDC_2Dcode", "11x11"))
        self.combox_NumberCell_DC_2Dcode.setItemText(2, _translate("Class_DlogDC_2Dcode", "13x13"))
        self.combox_NumberCell_DC_2Dcode.setItemText(3, _translate("Class_DlogDC_2Dcode", "15x15"))
        self.combox_NumberCell_DC_2Dcode.setItemText(4, _translate("Class_DlogDC_2Dcode", "17x17"))
        self.cbox_CodeColor_DC_2Dcode.setText(_translate("Class_DlogDC_2Dcode", "Code Color "))
        self.combox_CodeColor_DC_2Dcode.setItemText(0, _translate("Class_DlogDC_2Dcode", "Both"))
        self.combox_CodeColor_DC_2Dcode.setItemText(1, _translate("Class_DlogDC_2Dcode", "Black"))
        self.combox_CodeColor_DC_2Dcode.setItemText(2, _translate("Class_DlogDC_2Dcode", "White"))
        self.cbox_MirroredReading_DC_2Dcode.setText(_translate("Class_DlogDC_2Dcode", "Mirrored Reading"))
        self.combox_MirroredReading_DC_2Dcode.setItemText(0, _translate("Class_DlogDC_2Dcode", "Both"))
        self.combox_MirroredReading_DC_2Dcode.setItemText(1, _translate("Class_DlogDC_2Dcode", "Standard Only"))
        self.combox_MirroredReading_DC_2Dcode.setItemText(2, _translate("Class_DlogDC_2Dcode", "Mirrored Only"))
        self.cbox_BaseAngle_DC_2Dcode.setText(_translate("Class_DlogDC_2Dcode", "Base Angle"))
        self.label_8.setText(_translate("Class_DlogDC_2Dcode", "Options"))
        self.label_9.setText(_translate("Class_DlogDC_2Dcode", "Angle Range"))
        self.label_6.setText(_translate("Class_DlogDC_2Dcode", "+/-"))
        self.label_11.setText(_translate("Class_DlogDC_2Dcode", "Scale Variations"))
        self.combox_ScaleVariation_DC_2Dcode.setItemText(0, _translate("Class_DlogDC_2Dcode", "Small"))
        self.combox_ScaleVariation_DC_2Dcode.setItemText(1, _translate("Class_DlogDC_2Dcode", "Medium"))
        self.combox_ScaleVariation_DC_2Dcode.setItemText(2, _translate("Class_DlogDC_2Dcode", "Large"))
        self.combox_ScaleVariation_DC_2Dcode.setItemText(3, _translate("Class_DlogDC_2Dcode", "Unlimited"))
        self.label_12.setText(_translate("Class_DlogDC_2Dcode", "Time out (sec.)   "))
        self.btn_OK_DC_2Dcode.setText(_translate("Class_DlogDC_2Dcode", "OK"))
        self.btn_Cancel_DC_2Dcode.setText(_translate("Class_DlogDC_2Dcode", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Class_DlogDC_2Dcode = QtWidgets.QDialog()
    ui = Ui_Class_DlogDC_2Dcode()
    ui.setupUi(Class_DlogDC_2Dcode)
    Class_DlogDC_2Dcode.show()
    sys.exit(app.exec_())

