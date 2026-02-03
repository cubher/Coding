import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread('peacock.jpg')
plt.figure(1)
plt.imshow(img)
plt.title('Original Image')
imgR=img[:,:,0]
imgG=img[:,:,1]
imgB=img[:,:,2]
plt.figure(2)
plt.imshow(imgR,cmap='gray')
plt.title('Red Channel')
plt.figure(3)
plt.imshow(imgG,cmap='gray')
plt.title('Green Channel')
plt.figure(4)
plt.imshow(imgB,cmap='gray')
plt.title('Blue Channel')
plt.show()