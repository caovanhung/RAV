from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import configparser



config = configparser.ConfigParser()

class ActionFile:
    def __init__(self, dir_os_file):
        self.dir_os_file = dir_os_file

    def updateDataFile(self, file, sector, key, value):
        self.file = str(file)
        self.sector = str(sector)
        self.key = str(key)
        self.value = str(value)
        fp = open(str(self.dir_os_file) + "/"+ str(self.file))
        config.readfp(fp)

        #config.read(str(self.dir_os_file) + "/"+ str(self.file))

        config.set(str(self.sector), str(self.key) , str(self.value))
        config.write(open(str(self.dir_os_file) + "/"+ str(self.file), "w"))

        fp.close()

    def func_creadFileSettingStand(self,file):
        self.file = file

        fp = open(str(self.dir_os_file) + "/"+ str(self.file), "w+")
        config.readfp(fp)

        try:            
            config.add_section("Detection_1Dcode")
        except configparser.DuplicateSectionError:
            pass
        try:            
            config.add_section("DC")
        except configparser.DuplicateSectionError:
            pass
        try:            
            config.add_section("JC")
        except configparser.DuplicateSectionError:
            pass
        try:            
            config.add_section("RD")
        except configparser.DuplicateSectionError:
            pass
        try:            
            config.add_section("ER")
        except configparser.DuplicateSectionError:
            pass     
        try:            
            config.add_section("PARAMETER")
        except configparser.DuplicateSectionError:
            pass    


        config.set("Detection_1Dcode", "dir_config", "....")
        config.set("Detection_1Dcode", "dir_ImageProcessed", "....")
        config.set("Detection_1Dcode", "dir_ImageRaw", "....")
        config.set("Detection_1Dcode", "dir_ImageRowProcessed", "....")


        config.set("DC", "CodeType", "CODE128")
        config.set("DC", "ReferecContrast", "Highest")
        config.set("DC", "CodeColor", "Both")
        config.set("DC", "ScaleVariation", "Small")
        config.set("DC", "checkCodeResulation", "0")
        config.set("DC", "checkReferenContrast", "0")
        config.set("DC", "checkNumberReadDigit", "0")
        config.set("DC", "checkCodeColor", "0")
        config.set("DC", "checkBaseAngle","0" )
        config.set("DC", "checkEnableCheckDigit", "0")
        config.set("DC", "ValueCodeResulation", "10")
        config.set("DC", "ValueMinNumberReadDigit", "1")
        config.set("DC", "ValueMaxNumberReadDigit", "100")
        config.set("DC", "ValueBaseAngle", "0")
        config.set("DC", "ValueTimeOut", "30")

        config.set("JC", "SingleOfConditi", "False")
        config.set("JC", "MultiOfConditi", "True")
        #config.set("JC", "DataRange", self.var_combox_DataRange)
        #config.set("JC", "StartDigit", self.var_lab_StartDigit)
        #config.set("JC", "RangeDigit", str(self.var_lab_RangeDigit))
        config.set("JC", "CopyFromReadData", "OK")
        #config.set("JC", "CollationResult", str(self.var_lab_CollationResult))
        config.set("JC", "UpperLimitLengData", "---")
        config.set("JC", "LowerLimitLengData", "---")
        config.set("JC", "UpperLimitPositX", "---")
        config.set("JC", "UpperLimitPositY", "---")
        config.set("JC", "LowerLimitPositX", "---")
        config.set("JC", "LowerLimitPositY", "---")
        config.set("JC", "UpperLimitDetecAngle", "---")
        config.set("JC", "LowerLimitDetecAngle", "---")

        config.set("RD", "var_ValueStartDigit", "1")
        config.set("RD", "var_ValueLengReadData", "100")
        config.set("RD", "var_checkSplitData", "0")
        config.set("RD", "var_checkOutFixLeng", "0")
        config.set("RD", "var_checkCallTextError", "0" )
        config.set("RD", "var_checkOutSymbleIdentifier", "0")
        config.set("RD", "var_ValueFillingCharac", "100")
        config.set("RD", "var_ValueCallTextError", "error")

        config.set("ER", "InspectionRegion", "Rectangle")
        config.set("ER", "ReferencImage", "0001")


        config.set("PARAMETER", "x_start", "10")
        config.set("PARAMETER", "y_start", "10")
        config.set("PARAMETER", "x_end", "200")
        config.set("PARAMETER", "y_end", "200")

        config.write(open(str(self.dir_os_file) + "/"+ str(self.file), "w"))

        fp.close()


    def saveDataFile(self, file, sector, key, value):
        self.file = str(file)
        self.sector = str(sector)
        self.key = str(key)
        self.value = str(value)

        config.set(str(self.sector), str(self.key) , str(self.value))
        config.write(open(str(self.dir_os_file) + "/"+ str(self.file), "w"))

    def deleteFile(self, file): 
        os.remove(str(self.dir_os_file) + "/"+ str(file))

    def func_getNumToolConfig(self):
        return len(os.listdir(self.dir_os_file))

    def func_convert_1to4Digit(self, num):
        if num < 10 :
            num = "000" + str(num)
        elif num >= 10 and num < 100 :
            num = "00" + str(num)
        elif num >= 100 and num < 1000 :
            num = "0" + str(num)
        return num

