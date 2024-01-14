import cv2 
import matplotlib.pyplot as plt
import numpy as np 

# Read an image 
image = cv2.imread(r'forest.jpg')
plt.imshow(image)
plt.show()

# Trying 4 gamma values. 
for gamma in [0.1, 1.2, 2.2, 3.2, 6.2]:

    # Apply gamma correction. 
    gamma_corrected = np.array(255*(image / 255) ** gamma, dtype = 'uint8') 
    plt.imshow(gamma_corrected) 
    plt.show() 
