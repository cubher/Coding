import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread('peppers.png')

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

img_gray=rgb2gray(img)
plt.figure(1)
plt.imshow(img_gray,cmap='gray')
plt.figure(2)
plt.show()
plt.hist(img_gray)
plt.title("Histogram of given image")
plt.xlabel("Pixel values")
plt.ylabel("Frequency of pixel occurance")
plt.xlim([0, 255])
plt.imshow(img_gray,cmap='gray')