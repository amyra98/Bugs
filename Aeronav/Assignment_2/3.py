import numpy as np
import cv2

img = cv2.imread("image_2.jpg") 
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([50,70,100 ])
upper_green = np.array([70,255,255])

masked_image = cv2.inRange(img_hsv, lower_green, upper_green)
cv2.imshow('masked', masked_image)
cv2.imwrite("req3.1.jpg",masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()