#!/usr/bin/python3
import cv2


def resizeFrame(frame, scale=0.7):
    print(frame.shape)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_NEAREST)


img = cv2.imread("../../images/large_image.png")
cv2.imshow("Image", resizeFrame(img, .2))
cv2.waitKey(0)
cv2.destroyAllWindows()
