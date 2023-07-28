# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:07:28 2023

@author: CTTC
"""

import cv2
import numpy as np
import pandas as pd

vd = r"C:\Users\CTTC\Downloads\mixkit-waterfall-in-forest-2213-medium.mp4"    #read the video from the location
cv2.namedWindow(vd)                  #creates a window to display the video in it
cap = cv2.VideoCapture(vd)           #capture the item stored in 'vd', giving '0' opens up the camera

if cap.isOpened():                   #checks if the video is available or not
    ret,frame = cap.read()           #stores the video frame, if it exists
    print(ret)
    print(frame)
else:
    ret = False
    
while ret:                                 #for capturing each individual frame in the video
    ret,frame = cap.read()
    if ret==False:
        break
    cv2.imshow(vd,frame)                     #displays the video stored in the 'vd' variable with 'frame'
    
    if cv2.waitKey(1)==27:                 #the numeric value of 'esc' key is '27'
        break                              #when the 'esc' key is pressed, the video will be stopped
cv2.destroyAllWindows()
cap.release()