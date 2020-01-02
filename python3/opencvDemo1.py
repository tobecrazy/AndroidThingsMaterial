#!/usr/bin/python3
import cv2
img=cv2.imread("../images/opencvDemo1.jpg",1)
cv2.imshow("Image",img)
cv2.waitKey(2000)
cv2.destroyAllWindows()