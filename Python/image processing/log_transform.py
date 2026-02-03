import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

img=cv2.imread('test_images/einstein_low.jpg')
a=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#a=rgb2gray(img)
c=255 / np.log(1 + np.max(a))
#c=1.5
log_a = c * (np.log(a + 1))
log_a=np.array(log_a, dtype=np.uint8)
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.figure(1)
plt.imshow(a, cmap='gray')
plt.figure(2)
plt.hist(a)
plt.title("Histogram of original image")
plt.figure(3)
plt.imshow(log_a, cmap='gray')
plt.figure(4)
plt.hist(log_a)
plt.title("Histogram of log transformed image")