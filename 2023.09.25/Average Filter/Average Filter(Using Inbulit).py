import cv2
import numpy as np
image = cv2.imread('lena.jpg')
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)
smoothed_image = cv2.filter2D(image, -1, kernel)
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image (Average Filter)', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
