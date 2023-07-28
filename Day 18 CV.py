# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:46:36 2023

@author: CTTC
"""

#'computer vision', otherwise known as image processing, enable machines to read and interpret images
#a image with 100px by 100px states that a image is stored in a pixels matrix of 100x100
#color intensity ranges from 0 to 255, also known as 'Gray Scale'
#the primary color is the intensity combination for R, G and B
#the range of each color of R,G and B is also from 0 to 255
#the 0 on 'gray scale' is black and 255 on 'gray scale' is white.
#R-255,G-0,B-0 is Red color; R-0,G-255,B-0 is Green color; R-0,G-0,B-255 is Blue color
#'506x900' is the pixel size, stored in a pixel matrix
#'3' indicates 3 channels, RGB/colorful image; 1 channel is for black and white image
#the table in purple highlighted is colour combination
#0->R; 1->G; 2->B colour tables
#in hstack, the tables are joined horizontally; while in vstack, the tables are joined vertically
#for images there is 'depth_stack' the images are stored at the back of each other, that gives different color combinations


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\CTTC\Downloads\einstein.webp")  #reading image from folder location

cv2.imshow('Albert',img)      #display the image stored in 'img' variable, with the name
cv2.waitKey(0)                #close after 'n' milliseconds, for '0' don't close, for '2' milliseconds, close after 2ms
cv2.destroyAllWindows()       #close the window that is opening after the time of the 'waitKey'

plt.imshow(img)               #by default the plotting stores the images in 'BGR'
plt.show()

#image slicing-> img[row,column,scale]
#'img[:,:,::-1]'-> the last 'scale' has 'start,stop+1,step', for RGB the start is 0 and stop+1 is 3

plt.imshow(img[:,:,::-1])     #changes the scaling from 'BGR' to 'RGB'
plt.axis('off')
plt.show()

#'BGR' to 'RGB' conversion usingcv2 convert function
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)                  #uses function 'cvtColor' attribute 'BGR2RGB'
plt.imshow(rgb_img)
plt.show()

#Convert to Gray Scale
gray_img = cv2.cvtColor(rgb_img,cv2.COLOR_RGB2GRAY)           #uses function 'cvtColor' attribute 'RGB2GRAY'
cv2.imshow('Gray Albert',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Image Blurring
blur = cv2.GaussianBlur(gray_img,(5,5),2)                     
#the (4,4) is the size of GaussianBlur and the blur intensity->Gaussian Kernel Size. [height width]
#'2' is the sigmaX value, Kernel standard deviation along X-axis (horizontal direction)
cv2.imshow('Blur Albert',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

#capturing image from web cam
#This will return video from the first webcam on your computer. 
#If you are watching the tutorial videos, you will see I am using 1, since my first webcam is recording me 
#and the second webcam is used for the actual tutorial feed.
cap = cv2.VideoCapture(0) 
if cap.isOpened():                             #checks if the camera is opended
    ret,frame = cap.read()                     #if the camera is opened then strore the pixels
    #'ret' is a boolean variable that returns true if the frame is available.
    #'frame' is an image array vector captured based on the default frames per second defined explicitly or implicitly 
    print(ret)
    print(frame)
else:
    ret=False
    
img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)     #as by default the img is in 'BGR', thus we need to convert to 'RGB'
plt.imshow()
plt.title('My Picture')
plt.axis('off')
plt.show()
cap.release()                                    #close the camera after capturing

