import cv2
from matplotlib import pyplot as plt


def calculate_histogram(image):

  histogram = [0] * 256

  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      histogram[image[i, j]] += 1
  return histogram

image = cv2.imread('forest.jpg', 0)

histogram = calculate_histogram(image)

plt.plot(histogram)
cv2.imshow("fig1", image)


#with inbuilt function
img = cv2.imread('forest.jpg', 0)
window_name = 'Original_Figure'
# find frequency of pixels in range 0-255
histr = cv2.calcHist([img], [0], None, [256], [0, 256])

# show the plotting graph of an image
plt.plot(histr)
plt.show()

#If there is difference in the two graphs then it will show tow plots and if there is no difference then it will show only one plot.
