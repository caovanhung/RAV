import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from pylibdmtx import pylibdmtx

class Class_XLA_2Dcode:
    thred=0 
    img_t=0
    img_s=0
    img_cut=0
    var_x0_2Dcode=0
    var_x1_2Dcode=0
    var_y0_2Dcode=0
    var_y1_2Dcode=0
   # img_thred=0
   # img_c=0
    def __init__(self,img_1,img_2,x0,y0,x1,y1,var_fileImgRow):
        #self.img_t=img_t
  
        self.var_x0_2Dcode=x0
        self.var_y0_2Dcode=y0
        self.var_x1_2Dcode=x1
        self.var_y1_2Dcode=y1
        self.var_img_cut=img_1[y0:y1,x0:x1]
        self.var_img=img_2
        cv2.imwrite(var_fileImgRow, self.var_img)
 #   def dection_QR_code_filter(self,filter_list,kernel):
 #       if kernel=="3X3":
   #         self.kernel=3
    #    if kernel=="5X5":
    #        self.kernel=5
    #    if kernel=="7X7":
    #        self.kernel=7
    #    if kernel=="9X9":
    #        self.kernel=9
    #    if kernel=="11X11":
    #        self.kernel=11
       # print(self.kernel)
     #   if filter_list=="Averaging":
     #       self.filter_img = cv2.blur(self.img_cut,(self.kernel,self.kernel))
     #   if filter_list=="Gaussian Filtering":
     #       self.filter_img = cv2.GaussianBlur(self.img_cut,(self.kernel,self.kernel),0)
     #   if filter_list=="Median Filtering":
     #       self.filter_img =cv2.medianBlur(self.img_cut,self.kernel)
    def func_Threshold_xuly(self,thred,check):
        if check==1:
        #cv.THRESH_BINARY_INV
            thresh, self.var_img_thred = cv2.threshold(self.var_img_cut,thred, maxval=255, type=cv2.THRESH_BINARY_INV)
          #  self.var_img[self.var_y0_2Dcode:self.var_y1_2Dcode,self.var_x0_2Dcode:self.var_x1_2Dcode]=self.var_img_thred
        if check==2:

            thresh, self.var_img_thred = cv2.threshold(self.var_img_cut,thred, maxval=255, type=cv2.THRESH_BINARY)
          #  self.var_img[self.var_y0_2Dcode:self.var_y1_2Dcode,self.var_x0_2Dcode:self.var_x1_2Dcode]=self.var_img_thred

  #      return self.img
    def func_detectData_matrix(self):
        tmp_font = cv2.FONT_HERSHEY_PLAIN
        var_decodedObjects = pylibdmtx.decode(self.var_img_thred)
        self.tmp_img=self.var_img[self.var_y0_2Dcode:self.var_y1_2Dcode,self.var_x0_2Dcode:self.var_x1_2Dcode]
        self.var_strDataMatrix=""
        for obj in var_decodedObjects:
            if len(str(obj.data))!=0:
                self.var_strDataMatrix=obj.data.decode('utf-8')
                
            x,y,w,h=obj.rect
            cv2.rectangle( self.tmp_img , (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText( self.tmp_img ,self.var_strDataMatrix, (10, 10), tmp_font, 1,(255, 0, 0),1)        

            self.var_img[self.var_y0_2Dcode:self.var_y1_2Dcode,self.var_x0_2Dcode:self.var_x1_2Dcode]=self.tmp_img
        print(self.var_strDataMatrix)
        if len(self.var_strDataMatrix)==0:
                self.var_strDataMatrix="Khong phat hien"
        return self.var_strDataMatrix,self.var_img
        
        
    
    def func_detectQR_Code(self):
        tmp_font = cv2.FONT_HERSHEY_PLAIN

        self.tmp_img=self.var_img[self.var_y0_2Dcode:self.var_y1_2Dcode,self.var_x0_2Dcode:self.var_x1_2Dcode]
        var_decodedObjects = pyzbar.decode( self.var_img_thred )
        self.var_strQR=""
        for obj in var_decodedObjects:        
            if len(str(obj.data))!=0:
           
                self.var_strQR=obj.data.decode('utf-8')                
                x, y, w, h = obj.rect
                cv2.rectangle( self.tmp_img , (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText( self.tmp_img ,self.var_strQR, (10, 10), tmp_font, 1,(255, 0, 0),1)
            self.var_img[self.var_y0_2Dcode:self.var_y1_2Dcode,self.var_x0_2Dcode:self.var_x1_2Dcode]=self.tmp_img
       # print( self.str_QR)
        if len(self.var_strQR)==0:
                self.var_strQR="Khong phat hien"
                
        return  self.var_strQR,self.var_img
    


    def func_saveImage(self,var_fileImgRowProcessed,var_fileImgProcessed):
        self.tmp_img=self.var_img[self.var_y0_2Dcode:self.var_y1_2Dcode,self.var_x0_2Dcode:self.var_x1_2Dcode]
        cv2.imwrite(var_fileImgRowProcessed, self.tmp_img)
        cv2.imwrite(var_fileImgProcessed, self.var_img)


