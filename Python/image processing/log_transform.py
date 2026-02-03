import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('child.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_float = gray.astype(np.float32)
c = 255 / np.log(1 + np.max(gray_float))
log_img = c * np.log(1 + gray_float)
log_img = np.uint8(log_img)

# Display Original Image
plt.figure(1)
plt.imshow(gray, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis('off')

# Histogram of Original Image
plt.figure(2)
plt.hist(gray.ravel(), bins=256)
plt.title("Histogram of Original Image")

# Display Log Transformed Image
plt.figure(3)
plt.imshow(log_img, cmap='gray')
plt.title("Log Transformed Image")
plt.axis('off')

# Histogram of Log Transformed Image
plt.figure(4)
plt.hist(log_img.ravel(), bins=256)
plt.title("Histogram of Log Transformed Image")
plt.show()
