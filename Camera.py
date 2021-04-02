from PyQt5.QtCore import QTimer
from pypylon import pylon
import cv2
import sys
import os
import numpy as np 



class Camera_Basler:
    def __init__(self):
        self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        self.camera.MaxNumBuffer = 20
        self.timer = QTimer()

    def openCamera(self):
        self.camera.Open()

    def closeCamera(self):
        self.camera.Close()

    def func_viewImage(self):
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            image = converter.Convert(grabResult)
            image = image.GetArray()
            image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #mau video duoc chuyen doi tro lai RGB de no la mau thuc 
            return image

    def grapImage(self):
        self.camera.StopGrabbing()
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grabResult.GrabSucceeded():
            image = converter.Convert(grabResult)
            image = image.GetArray()
            image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            self.camera.StopGrabbing()
            return image
        self.camera.StopGrabbing()

    def controlTimer(self):
        if not self.timer.isActive():
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
            self.timer.start(20)
        else:
            self.timer.stop()
            self.camera.StopGrabbing()

    def timerStop(self):
        self.timer.stop()
