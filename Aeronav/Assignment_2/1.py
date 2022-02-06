import numpy as np
import cv2

img = cv2.imread("image_1.jpg") 
img2 = cv2.imread("image_2.jpg") 
cv2.imshow('image', img)
cv2.imshow('immage', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()