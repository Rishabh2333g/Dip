import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_arithmetic_mean_filter_manual(image, kernel_size):
    # Get image dimensions
    rows, cols = image.shape

    # Create an output image to store the filtered result
    filtered_image = np.zeros_like(image, dtype=np.float32)

    # Define half of the kernel size
    half_kernel = kernel_size // 2

    # Iterate over each pixel in the image
    for i in range(half_kernel, rows - half_kernel):
        for j in range(half_kernel, cols - half_kernel):
            # Extract the neighborhood
            neighborhood = image[i - half_kernel:i + half_kernel + 1, j - half_kernel:j + half_kernel + 1]

            # Calculate the average and assign it to the corresponding pixel in the output image
            filtered_image[i, j] = np.mean(neighborhood)

    return filtered_image.astype(np.uint8)

# Load an image using OpenCV
img = cv2.imread('forest.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load the image. Please check the file path.")
    exit()

# Set the kernel size for the arithmetic mean filter
kernel_size = 5

# Apply arithmetic mean filter without inbuilt function
filtered_img_manual = apply_arithmetic_mean_filter_manual(img.copy(), kernel_size)

# Display the original and filtered images
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(filtered_img_manual, cmap='gray'), plt.title('Filtered Image (Manual)')
plt.show()
