import numpy as np
import cv2

img = cv2.imread("image_1.jpg") 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,binary_inv=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('threshold binary inv', binary_inv)
cv2.imwrite("req2.jpg", binary_inv)
cv2.waitKey(0) 
cv2.destroyAllWindows()