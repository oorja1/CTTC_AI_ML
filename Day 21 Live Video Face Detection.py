# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:52:18 2023

@author: Hp
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

face_data = cv2.CascadeClassifier(r"C:\Users\Hp\ML Practise\Datasets\haarcascades\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

ret,frame = cap.read()

while ret:
    ret,image = cap.read()
    
    if not ret:
        break
    
    face = face_data.detectMultiScale(image)
    
    for x,y,w,h in face:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv2.imshow('Image',image)
    if cv2.waitKey(8)==27:
        break

cv2.destroyAllWindows()
cap.release()