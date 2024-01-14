import cv2

img = cv2.imread(r'C:\Users\RISHABH\OneDrive - st.niituniversity.in\BOOKS\Digital Image Processing\DIP Codes\28.08.2023\Gamma_transformation\forest.jpg')
cv2.imshow("fig1", img)

img_v = cv2.flip(img, 0)

cv2.imshow("Vertical Flip", img_v)
cv2.waitKey(0)
cv2.destroyAllWindows()
