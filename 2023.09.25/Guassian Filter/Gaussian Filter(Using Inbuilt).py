import cv2
image = cv2.imread('lena.jpg')
kernel_size = 5
sigma = 1.0
smoothed_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image (Gaussian Filter)', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
