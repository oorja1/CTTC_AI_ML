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

img = cv2.imread(r"C:\Users\Hp\Downloads\download (2).jpg")  #reading image from folder location

cv2.imshow('Baraak',img)      #display the image stored in 'img' variable
cv2.waitKey(0)                #close after 'n' milliseconds, for '0' don't close, for '2' milliseconds, close after 2ms
cv2.destroyAllWindows()       #close the window that is opening

plt.imshow(img)               #by default the plotting stores the images in 'BGR'
plt.show()

#image slicing-> img[row,column,scale]
#'img[:,:,::-1]'-> the last 'scale' has 'start,stop+1,step', for RGB the start is 0 and stop+1 is 3

plt.imshow(img[:,:,::-1])     #changes the scaling from 'BGR' to 'RGB'
plt.axis('off')
plt.show()

#color combination

#for red, R-255,G-0,B-0
red = np.full((50,50),255)              #array to represent red in depth stacking
green = np.full((50,50),0)              #array to represent green in depth stacking
blue =  np.full((50,50),0)              #array to represent blue in depth stacking
rgb = np.dstack((red,green,blue))       #stacking is more important, the sequence in which R, G and B are put
plt.imshow(rgb)
plt.axis('off')
plt.show()

#for green, R-0,G-255,B-0
red = np.full((50,50),0)
green = np.full((50,50),255)
blue =  np.full((50,50),0)
rgb = np.dstack((red,green,blue))
plt.imshow(rgb)
plt.axis('off')
plt.show()

#for blue, R-0,G-0,B-255
red = np.full((50,50),0)
green = np.full((50,50),0)
blue =  np.full((50,50),255)
rgb = np.dstack((red,green,blue))
plt.imshow(rgb)
plt.axis('off')
plt.show()


#for skyblue, R-0,G-255,B-255
red = np.full((50,50),0)
green = np.full((50,50),255)
blue =  np.full((50,50),255)
rgb = np.dstack((red,green,blue))
plt.imshow(rgb)
plt.axis('off')
plt.show()

#for pink, R-0,G-0,B-255
red = np.full((50,50),255)
green = np.full((50,50),0)
blue =  np.full((50,50),255)
rgb = np.dstack((red,green,blue))
plt.imshow(rgb)
plt.axis('off')
plt.show()

#for yellow, R-0,G-0,B-255
red = np.full((50,50),255)
green = np.full((50,50),255)
blue =  np.full((50,50),0)
rgb = np.dstack((red,green,blue))
plt.imshow(rgb)
plt.axis('off')
plt.show()

#for black, R->0;G->0;B->0
red = np.full((50,50),0)
green = np.full((50,50),0)
blue =  np.full((50,50),0)
rgb = np.dstack((red,green,blue))
plt.imshow(rgb)
plt.axis('off')
plt.show()

#for white, R->255;G->255;B->255
red = np.full((50,50),255)
green = np.full((50,50),255)
blue =  np.full((50,50),255)
rgb = np.dstack((red,green,blue))
plt.imshow(rgb)
plt.axis('off')
plt.show()

#National Flag of India
#safforn
red = np.full((20,90),244)
green = np.full((20,90),120)
blue =  np.full((20,90),48)
rgb1 = np.dstack((red,green,blue))
plt.imshow(rgb1)
plt.axis('off')
plt.show()
#white
red = np.full((20,90),255)
green = np.full((20,90),255)
blue =  np.full((20,90),255)
rgb2 = np.dstack((red,green,blue))
plt.imshow(rgb2)
plt.axis('off')
plt.show()
#green
red = np.full((20,90),0)
green = np.full((20,90),102)
blue =  np.full((20,90),51)
rgb3 = np.dstack((red,green,blue))
plt.imshow(rgb3)
plt.axis('off')
plt.show()

#variable for national flag
national_flag = np.vstack((rgb1,rgb2,rgb3))
plt.imshow(national_flag)
plt.axis('off')
plt.show()