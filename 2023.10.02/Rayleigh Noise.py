import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_rayleigh_noise_manual(image, scale):
    # Generate Rayleigh noise using the square root of the sum of squared Gaussian random variables
    noise = np.sqrt(-2 * scale**2 * np.log(np.random.rand(*image.shape)))

    # Add noise to the image
    noisy_image = image + noise

    # Clip values to be in the valid range [0, 255]
    noisy_image = np.clip(noisy_image, 0, 255)

    return noisy_image.astype(np.uint8)

def add_rayleigh_noise_builtin(image, scale):
    # Generate Rayleigh noise using NumPy built-in function
    noise = np.random.rayleigh(scale, size=image.shape)

    # Add noise to the image
    noisy_image = image + noise

    # Clip values to be in the valid range [0, 255]
    noisy_image = np.clip(noisy_image, 0, 255)

    return noisy_image.astype(np.uint8)

# Load an image using OpenCV
img = cv2.imread(r'forest.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if img is None:
    print("Error: Unable to load the image. Please check the file path.")
    exit()

# Add Rayleigh noise without inbuilt function
scale_parameter_manual = 30
noisy_img_manual = add_rayleigh_noise_manual(img, scale_parameter_manual)

# Add Rayleigh noise with inbuilt function
scale_parameter_builtin = 30
noisy_img_builtin = add_rayleigh_noise_builtin(img, scale_parameter_builtin)

# Display the original and noisy images
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 3, 2), plt.imshow(noisy_img_manual, cmap='gray'), plt.title('Noisy Image (Manual)')
plt.subplot(1, 3, 3), plt.imshow(noisy_img_builtin, cmap='gray'), plt.title('Noisy Image (Built-in)')
plt.show()
