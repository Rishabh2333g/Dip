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

# Set the initial and maximum kernel size for degradation
initial_kernel_size = 3
max_kernel_size = 15

# Display the original image
plt.subplot(1, 5, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

# Display three intermediate degradation steps
degradation_steps = [5, 9, 13]  # Adjust as needed

for step, kernel_size in enumerate(degradation_steps, start=2):
    # Apply arithmetic mean filter without inbuilt function
    degraded_img = apply_arithmetic_mean_filter_manual(img.copy(), kernel_size)

    # Display the degraded image
    plt.subplot(1, 5, step)
    plt.imshow(degraded_img, cmap='gray')
    plt.title(f'Degraded (Kernel {kernel_size})')

plt.show()
