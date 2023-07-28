# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:41:28 2023

@author: CTTC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\CTTC\Downloads\Road.jpg")  #reading image from folder location

plt.imshow(img[:,:,::-1])     #changes the scaling from 'BGR' to 'RGB'
plt.axis('off')
plt.show()

#detecting edges inside the image
canny = cv2.Canny(img,30,120)
#'img'->detects the edges on the given image
#'30' is T_lower: Lower threshold value in Hysteresis Thresholding
#'120' is T_upper: Upper threshold value in Hysteresis Thresholding
cv2.imshow('Canny detection',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()