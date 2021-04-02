from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import configparser

var_dirFileOS = os.getcwd()
var_dirFileOS = var_dirFileOS.rstrip()
var_dirFileOS = var_dirFileOS.replace("/Detection_1DCode","")
var_dirFileConfig = var_dirFileOS + "/" + "config"

config = configparser.ConfigParser()
config.read(var_dirFileConfig + "/"+ "0006.ini")
config.add_section("DC")
config.add_section("JC")
config.add_section("RD")
# config.add_section("ER")
# config.set("ER", "InspectionRegion", "self.var_CodeType")
# config.set("ER", "ReferencImage", "self.var_ReferecContrast")

config.set("DC", "CodeType", "self.var_CodeType")
config.set("DC", "ReferecContrast", "self.var_ReferecContrast")
config.set("DC", "CodeColor", "self.var_CodeColor")
config.set("DC", "ScaleVariation", "self.var_ScaleVariation")
config.set("DC", "checkCodeResulation", "str(self.var_checkCodeResulation)")
config.set("DC", "checkReferenContrast", "str(self.var_checkReferenContrast)")
config.set("DC", "checkNumberReadDigit", "str(self.var_checkNumberReadDigit)")
config.set("DC", "checkCodeColor", "str(self.var_checkCodeColor)")
config.set("DC", "checkBaseAngle", "str(self.var_checkBaseAngle)")
config.set("DC", "checkEnableCheckDigit", "str(self.var_checkEnableCheckDigit)")
config.set("DC", "ValueCodeResulation", "self.var_ValueCodeResulation")
config.set("DC", "ValueMinNumberReadDigit", "self.var_ValueMinNumberReadDigit")
config.set("DC", "ValueMaxNumberReadDigit", "self.var_ValueMaxNumberReadDigit")
config.set("DC", "ValueBaseAngle", "self.var_ValueBaseAngl")
config.set("DC", "ValueTimeOut", "self.var_ValueTimeOut")

config.set("JC", "SingleOfConditi", "str(self.var_rbtn_SingleOfConditi)")
config.set("JC", "MultiOfConditi", "str(self.var_rbtn_MultiOfConditi)")
#config.set("JC", "DataRange", self.var_combox_DataRange)
#config.set("JC", "StartDigit", self.var_lab_StartDigit)
#config.set("JC", "RangeDigit", str(self.var_lab_RangeDigit))
config.set("JC", "CopyFromReadData", "self.var_ledit_CopyFromReadData")
#config.set("JC", "CollationResult", "str(self.var_lab_CollationResult))
config.set("JC", "UpperLimitLengData"," self.var_ledit_UpperLimitLengData")
config.set("JC", "LowerLimitLengData", "self.var_ledit_LowerLimitLengData")
config.set("JC", "UpperLimitPositX", "self.var_ledit_UpperLimitPositX")
config.set("JC", "UpperLimitPositY", "self.var_ledit_UpperLimitPositY")
config.set("JC", "LowerLimitPositX", "self.var_ledit_LowerLimitPositX")
config.set("JC", "LowerLimitPositY", "self.var_ledit_LowerLimitPositY")
config.set("JC", "UpperLimitDetecAngle", "self.var_ledit_UpperLimitDetecAngle")
config.set("JC", "LowerLimitDetecAngle"," self.var_ledit_LowerLimitDetecAngle")

config.set("RD", "var_ValueStartDigit"," self.var_ValueStartDigit")
config.set("RD", "var_ValueLengReadData", "self.var_ValueLengReadData")
config.set("RD", "var_checkSplitData"," str(self.var_checkSplitData)")
config.set("RD", "var_checkOutFixLeng", "str(self.var_checkOutFixLeng)")
config.set("RD", "var_checkCallTextError", "str(self.var_checkCallTextError)")
config.set("RD", "var_checkOutSymbleIdentifier", "str(self.var_checkOutSymbleIdentifier)")
config.set("RD", "var_ValueFillingCharac", "self.var_ValueFillingCharac")
config.set("RD", "var_ValueCallTextError", "self.var_ValueCallTextError")

config.write(open(var_dirFileConfig + "/"+ "0006.ini", "w"))