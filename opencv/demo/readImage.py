#!/usr/bin/python3
import cv2

img = cv2.imread("../../images/large_image.png")
cv2.namedWindow("Image", cv2.WINDOW_FULLSCREEN)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
