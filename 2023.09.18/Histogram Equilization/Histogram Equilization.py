import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv.imread("forest.jpg")

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Equalize the histogram
equ = cv.equalizeHist(gray)

# Display the original and equalized images
plt.subplot(121), plt.imshow(gray, cmap="gray")
plt.title("Original Image"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(equ, cmap="gray")
plt.title("Equalized Image"), plt.xticks([]), plt.yticks([])
plt.show()

img = cv2.imread('equ', 0)
window_name = 'Original_Figure'
# find frequency of pixels in range 0-255
histr = cv2.calcHist([img], [0], None, [256], [0, 256])

# show the plotting graph of an image
plt.plot(histr)
plt.show()
