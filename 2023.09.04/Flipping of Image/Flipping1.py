import cv2

img = cv2.imread(r'C:\Users\RISHABH\OneDrive - st.niituniversity.in\BOOKS\Digital Image Processing\DIP Codes\28.08.2023\contrast_Stretching\forest.jpg',0)
cv2.imshow('original image',img)

row, col = img.shape

img = img[row-1: :-1, :]

cv2.imshow("Flipped", img);
cv2.waitKey(0)
cv2.destroyAllWindows()
