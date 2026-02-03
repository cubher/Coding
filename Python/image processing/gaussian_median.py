import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage # Multi-dimensional image processing

img=mpimg.imread('C:/Users/vitcc/Desktop/VIT-Admin/Vision-VAP-2021/Course-Materials/Python-Exercises/imgMed.JPG')

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

img=rgb2gray(img)
img_noise = img + 0.05* np.random.randn(*img.shape)
blurred_img1=ndimage.gaussian_filter(img_noise, sigma=1.5) # Multidimensional Gaussian filter
blurred_img2=ndimage.median_filter(img_noise,5) # Calculate a multidimensional median filter