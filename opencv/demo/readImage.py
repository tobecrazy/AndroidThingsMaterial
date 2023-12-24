#!/usr/bin/python3
import cv2
import numpy as np

print("Wait for image load")
img = cv2.imread("../../images/Lenna.png")
b, g, r = cv2.split(img)
_, _, chanel = img.shape

print(chanel)
cv2.namedWindow("Image", cv2.WINDOW_FULLSCREEN)
# grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(img)
# cv2.imshow("Image", b)
# cv2.imshow("Image", g)
# cv2.imshow("Image", r)

img2 = cv2.merge((b, g, r))
cv2.imshow('merged', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
