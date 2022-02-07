import cv2
import numpy as np

img = cv2.imread("image_2.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Working on the Green Colour
lower_green = np.array([40, 200, 120]) 
upper_green = np.array([70, 255, 255])

# Masking the image with the colour
masked_image = cv2.inRange(img_hsv, lower_green, upper_green)

# Creating a copy of the image and finding contours
img1 = img.copy()
contours, hierarchy = cv2.findContours(masked_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(contour, 0.1 * cv2.arcLength(contour, True), True)
      
    # using drawContours() function
    cv2.drawContours(img1,[contour], 0, (0, 0, 255), 5)
  
    # finding center point of shape
    M = cv2.moments(contour)
    if M['m00'] >4:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        if len(approx) == 3:
            cv2.putText(img1, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
  
        elif len(approx) == 4:
            cv2.putText(img1, 'Quadrilateral', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
  
        elif len(approx) == 5:
            cv2.putText(img1, 'Pentagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
  
        elif len(approx) == 6:
            cv2.putText(img1, 'Hexagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
  
        else:
            cv2.putText(img1, 'circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

cv2.imwrite("Answer3a.jpg", img1)

# Working on the Blue Colour
lower_blue = np.array([70, 250, 200]) 
upper_blue = np.array([130, 255, 255])

# Masking the image with the colour
masked_image2 = cv2.inRange(img_hsv, lower_blue, upper_blue)

# Creating a copy of the image and finding contours
img2 = img.copy()
contours, hierarchy = cv2.findContours(masked_image2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(contour, 0.1 * cv2.arcLength(contour, True), True)
      
    # using drawContours() function
    cv2.drawContours(img2,[contour], 0, (0, 0, 255), 5)
  
    # finding center point of shape
    M = cv2.moments(contour)
    if M['m00']>3:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        if len(approx) == 3:
            cv2.putText(img2, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
  
        elif len(approx) == 4:
            cv2.putText(img2, 'Quadrilateral', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
  
        elif len(approx) == 5:
            cv2.putText(img2, 'Pentagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
  
        elif len(approx) == 6:
            cv2.putText(img2, 'Hexagon', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)
  
        else:
            cv2.putText(img2, 'Circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 2)

cv2.imwrite("Answer3b.jpg", img2)


cv2.waitKey(0)
cv2.destroyAllWindows()