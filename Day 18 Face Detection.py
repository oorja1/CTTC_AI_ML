# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:49:38 2023

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


box = cv2.rectangle(rgb_img,(300,450),(760,30),(255,0,0),thickness=2)       #stores the created box
plt.imshow(rgb_img)
plt.show()