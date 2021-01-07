#!/usr/bin/python3
import cv2
import numpy
import textwrap3

blank = numpy.zeros((700, 800, 3), dtype='uint8')
blank[0:700, 0:800] = 0, 255, 255
cv2.imshow("Draw picture", blank)

# draw a rectangle
cv2.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 0, 255), thickness=3)
cv2.imshow("Rectangle", blank)

# draw a circle

cv2.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 60, (0, 0, 255), thickness= -1)
cv2.imshow("Circle", blank)

# draw a line

cv2.line(blank,(blank.shape[1] // 2, blank.shape[0] // 2),(blank.shape[1],blank.shape[0]),(255,0,0),thickness= 10)
cv2.imshow("Line", blank)
# write text

text= 'Life is short, you need Python!'
text=textwrap3.fill(text, width=50)
cv2.putText(blank,text,(100,100),cv2.FONT_ITALIC,1.0,(0,255,0),thickness= 2)
cv2.imshow("Text", blank)

img_gray =cv2.cvtColor(blank,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", img_gray)

# write to a file
cv2.imwrite("../../images/draw.png",blank)

cv2.waitKey(0)
cv2.destroyAllWindows()
