# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 08:45:51 2023

@author: CTTC
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\CTTC\Downloads\einstein.webp")  #reading image from folder location

#'BGR' to 'RGB' conversion usingcv2 convert function
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)                  #uses function 'cvtColor' attribute 'BGR2RGB'
plt.imshow(rgb_img)
plt.show()


box = cv2.rectangle(rgb_img,(300,450),(760,30),(255,0,0),thickness=2)
plt.imshow(rgb_img)
plt.show()

face_data = r"C:\Users\CTTC\Downloads\Datasets\haarcascades\haarcascade_frontalface_default.xml"

model = cv2.CascadeClassifier(face_data)

img = cv2.imread(r"C:\Users\CTTC\Downloads\icon00000000007.jpg")

rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)                  #uses function 'cvtColor' attribute 'BGR2RGB'

facepoints = model.detectMultiScale(img)                       #for detecting multiple images/scales

for x,y,w,h in facepoints:                                            #loop for multiple faces
    cv2.rectangle(rgb_img,(x,y),(x+w,y+h),(0,0,255),thickness=3)
    
plt.imshow(rgb_img)
plt.show()