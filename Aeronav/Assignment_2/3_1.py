import numpy as np
import cv2

img = cv2.imread("image_2.jpg") 
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

masked_image = cv2.inRange(img_hsv, lower_blue, upper_blue)
cv2.imshow('masked', masked_image)
cv2.imwrite("req3.2.jpg",masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()