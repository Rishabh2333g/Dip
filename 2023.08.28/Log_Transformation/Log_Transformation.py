import cv2 
import matplotlib.pyplot as plt 
import math
import numpy as np 

# Read an image
image = cv2.imread(r'fourierspectrum.jpg')

# Apply log transformation method 
c = 255 / np.log(1 + np.max(image)) 
log_image = c * (np.log(image + 1)) 
   

log_image = np.array(log_image, dtype = np.uint8) 
   
# Display both images 
plt.imshow(image) 
plt.show()
plt.imshow(log_image) 
plt.show() 
