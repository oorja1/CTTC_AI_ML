# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 20:42:14 2023

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

while ret:                                       #for capturing each individual frame in the video
    ret,frame = cap.read()                           #if the camera is opened return true to 'ret' and stores the image in 'frame'
    
    cap = cv2.VideoCapture(0)                        #opens up the live camera for capturing the frames            
    if cap.isOpened():                               #checks if the camera is opened         
        ret,frame = cap.read()                       #if the camera is opened return true to 'ret' and stores the image in 'frame'
    else:
        ret=False                                    #if no frames are captured, close the window
        
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)      #change the color of the image from 'BGR' to 'RGB'

    face_data = r"C:\Users\Hp\ML Practise\Datasets\haarcascades\haarcascade_frontalface_default.xml"
    #call the 'haarcascade', a kaggle dataset, an Object Detection Algorithm used to identify faces in an image or a real time video. 

    model = cv2.CascadeClassifier(face_data)
    #It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. 
    #It is then used to detect objects in other images.

    facepoints = model.detectMultiScale(img)                       #for detecting multiple images/scales

    for x,y,w,h in facepoints:                                            #loop for multiple faces
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=3)          #plots the quadilateral box on the face
        
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
    if ret==False:                                   #exit the loop if no frames are captured
        break                                        #used to exit the loop and close video window
    if cv2.waitKey(1)==27:                           #the numeric value of 'esc' key is '27'
        break                                        #will close the video capturing window and exit the loop of while
    