import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

# Load the original image
img = cv2.imread('forest.jpg', cv2.IMREAD_GRAYSCALE)

# Generate a random histogram with the same number of bins as the original image
rand_hist, _ = np.histogram(np.random.randint(0, 256, size=img.size), 256, [0, 256])

# Calculate the CDF of the random histogram and normalize it to the range [0, 255]
rand_cdf = np.cumsum(rand_hist)
rand_cdf = (rand_cdf - rand_cdf.min()) * 255 / (rand_cdf.max() - rand_cdf.min())
rand_lookup = np.interp(np.arange(256), rand_cdf.astype('int'), np.arange(256))

# Calculate the CDF of the original image's histogram and normalize it to the range [0, 255]
orig_hist, _ = np.histogram(img.ravel(), 256, [0, 256])
orig_cdf = np.cumsum(orig_hist)
orig_cdf = (orig_cdf - orig_cdf.min()) * 255 / (orig_cdf.max() - orig_cdf.min())

# Create a lookup table that maps each intensity value in the original image to its new value based on the normalized CDFs
lookup = np.interp(orig_cdf, rand_cdf, np.arange(256))

# Use the lookup table to create a new image with the matched histogram
matched_img = cv2.LUT(img, lookup.astype('uint8'))

# Display the original and matched images side by side
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(img, cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(matched_img, cmap='gray')
ax[1].set_title('Matched Image')
plt.savefig('histogram_matching.png')
