import cv2
import numpy as np
import matplotlib.pyplot as plt

#safforn
red = np.full((20,90),244)
green = np.full((20,90),120)
blue =  np.full((20,90),48)
rgb1 = np.dstack((red,green,blue))
plt.imshow(rgb1)
plt.axis('off')
plt.show()

#green
red = np.full((20,90),0)
green = np.full((20,90),102)
blue =  np.full((20,90),51)
rgb2 = np.dstack((red,green,blue))
plt.imshow(rgb2)
plt.axis('off')
plt.show()

#white
red = np.full((20,30),255)
green = np.full((20,30),255)
blue =  np.full((20,30),255)
rgb3 = np.dstack((red,green,blue))
plt.imshow(rgb3)
plt.axis('off')
plt.show()

#image import for 'ashoka chakra'
ashoka = cv2.imread(r"C:\Users\Hp\Downloads\360_F_311134651_RXMvbUB3h089Js0ODvuHrttmsON9Tpik.jpg")

aimage = cv2.cvtColor(ashoka,cv2.COLOR_BGR2RGB)

image_resize = cv2.resize(aimage,(30,20), interpolation= cv2.INTER_LINEAR)

#middle part of the flag
middle = np.hstack((rgb3,image_resize,rgb3))
plt.imshow(middle)
plt.axis('off')
plt.show()

#total national flag
national_flag = np.vstack((rgb1,middle,rgb2))
plt.imshow(national_flag)
plt.axis('off')
plt.show()

