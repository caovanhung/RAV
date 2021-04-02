from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication
import cv2
import sys

from pyzbar.pyzbar import decode
#from PIL import Image

class MyLabel(QLabel):
    x_start = 0
    y_start = 0
    x_end = 0
    y_end = 0
    flag = False
    
    def mousePressEvent(self,event):
        self.flag = True
        self.x_start = event.x()
        self.y_start = event.y()

    def mouseReleaseEvent(self,event):
        self.flag = False

    def mouseMoveEvent(self,event):
        if self.flag:
            self.x_end = event.x()
            self.y_end = event.y()
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        rect =QRect(self.x_start, self.y_start, abs(self.x_end-self.x_start), abs(self.y_end-self.y_start))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red,2,Qt.SolidLine))
        painter.drawRect(rect)

class class_DeCode1D:
    def __init__(self, image, x_start, y_start, x_end, y_end):
        self.image = image
        self.roi_image = self.image[y_start:y_end, x_start: x_end]
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end


    def func_decode_1D(self, codeType):
        self.codeType = codeType
        if self.codeType == "CODE39" or self.codeType == "CODE128" or self.codeType == "Databar" or self.codeType == "CODE93":
            result = decode(self.roi_image)
            # print(result)
            self.str_QR=""
            for obj in result:       
                if len(str(obj.data))!=0:
                    for i in range(2,len(str(obj.data))-1):
                        self.str_QR=self.str_QR+str(obj.data)[i]
                    x, y, w, h = obj.rect
                    cv2.rectangle( self.roi_image , (x, y), (x + w, y + h), (0, 0, 255), 2) 
            self.image[self.y_start:self.y_end, self.x_start: self.x_end] = self.roi_image   
            if len(self.str_QR)==0:
                    self.str_QR="Khong phat hien"
            return  self.str_QR, self.image

    def SimpleThresholding(self):
        thresh, self.img_thred = cv2.threshold(self.roi_image, 100, maxval=255, type=cv2.THRESH_BINARY)
        self.image[self.y_start:self.y_end,self.x_start:self.x_end]=self.img_thred
        cv2.imwrite('image.jpg', self.image)
