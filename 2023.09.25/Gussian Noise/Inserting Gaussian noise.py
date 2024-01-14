import cv2
import numpy as np
original_img = cv2.imread('lena.jpg')
mean = 0
stddev = 180
noise = np.zeros(original_img.shape, np.uint8)
cv2.randn(noise, mean, stddev)
noisy_img = cv2.add(original_img, noise)
cv2.imwrite('noisy_img.jpg', noisy_img)
cv2.imshow('Original Image', original_img)
cv2.imshow('Noisy Image', noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
