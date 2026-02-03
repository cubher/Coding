import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

img = cv2.imread('peacock.jpg')

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

# Trying 4 gamma values.
a=rgb2gray(img)
plt.figure()
plt.imshow(a, cmap='gray')
plt.title("Original image")

for gamma in [0.1, 0.5, 1.2, 2.2]:
    gamma_corrected = np.array(255*(a / 255) ** gamma, dtype = 'uint8')
    print('gamma_transformed '+str(gamma)+'.jpg')
    plt.figure()
    plt.imshow(gamma_corrected, cmap='gray')
    plt.title(f"Transformed image (Gamma={gamma})")
plt.show()