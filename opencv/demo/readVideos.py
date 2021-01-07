#!/usr/bin/python3
import cv2

def resizeFrame(frame, scale=0.7):
    print(frame.shape)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
def changeRes(width,height):
    capture = cv2.VideoCapture(0)
    capture.set(3,width)
    capture.set(4,height)
    return capture


#reading video
# capture = cv2.VideoCapture("../../video/spiderman.mp4")
# read from camare
capture = cv2.VideoCapture(0)
# capture.set(3, 1000)
# capture.set(4, 900)
while True:
   isTrue,frame = capture.read()
   cv2.imshow('Origin',frame)
   cv2.imshow('Resize video',resizeFrame(frame,.2))
   if cv2.waitKey(20) & 0xFF == ord('q') :
   	   break
capture.release()
cv2.destroyAllWindows()
