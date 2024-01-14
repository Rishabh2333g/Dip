import cv2 as cv
import numpy as np

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

array = [[0,10,20],[15,35,100],[150,200,255]]
array = np.array(array, dtype=np.uint8)

hist_dict = {}

for intensity in range(256):
    hist_dict[intensity] = 0
    
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        hist_dict[array[i][j]]+=1


# print(hist_dict)

keys = list(hist_dict.keys())
values = list(hist_dict.values())

fig, ax = plt.subplots()

ax.bar(keys, values)

ax.set_xlabel('Intensity')
ax.set_ylabel('Frequency')
ax.set_title('Histogram from Dictionary')

plt.savefig('histogram_making1.png')
