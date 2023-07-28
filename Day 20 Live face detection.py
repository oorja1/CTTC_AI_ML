# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 16:57:04 2023

@author: Hp
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)                        #opens up the live camera for capturing the frames            
if cap.isOpened():                               #checks if the camera is opened         
    ret,frame = cap.read()                       #if the camera is opened return true to 'ret' and stores the image in 'frame'
else:
    ret=False                                    #if the camera is not opened, return 'False' that no image is captured
    
img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)      #change the color of the image from 'BGR' to 'RGB'

face_data = r"C:\Users\Hp\ML Practise\Datasets\haarcascades\haarcascade_frontalface_default.xml"
#call the 'haarcascade', an Object Detection Algorithm used to identify faces in an image or a real time video. 

model = cv2.CascadeClassifier(face_data)
#It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. 
#It is then used to detect objects in other images.

facepoints = model.detectMultiScale(img)                       #for detecting multiple images/scales

for x,y,w,h in facepoints:                                            #loop for multiple faces
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=3)          #plots the quadilateral box on the face
    
plt.imshow(img)            #plots the final image in the plot
plt.show()
