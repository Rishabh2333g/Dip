import cv2
import numpy as np
image = cv2.imread('lena.jpg')
kernel_size = 5
height, width, channels = image.shape
smoothed_image = np.copy(image)
half_kernel = kernel_size // 2
for i in range(half_kernel, height - half_kernel):
    for j in range(half_kernel, width - half_kernel):
        for c in range(channels):

            average = np.mean(image[i - half_kernel:i + half_kernel + 1, j - half_kernel:j + half_kernel + 1, c])
            smoothed_image[i, j, c] = average
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image (Average Filter)', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
