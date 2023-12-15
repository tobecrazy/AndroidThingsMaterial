#!/usr/bin/python3
import cv2
import numpy
import textwrap3

blank = numpy.zeros((900, 900, 3), dtype=numpy.uint8)
blank[0:850, 0:850] = 255, 255, 255
cv2.imshow("Draw picture", blank)

# draw a rectangle
'''
The rectangle will be drawn on rook_image
Two opposite vertices of the rectangle are defined by ( 0, 0) and ( w, w )
The color of the rectangle is given by ( 0, 255, 255 ) which is the BGR value for yellow
Since the thickness value is given by FILLED (-1), the rectangle will be filled. Use 20
'''
cv2.rectangle(blank, (0, 0), (blank.shape[1], blank.shape[0]), (0, 255, 255),  thickness=20 )
cv2.imshow("Rectangle", blank)

# draw a circle
'''
The image where the circle will be displayed (img)
The center of the circle denoted as the point center
The radius of the circle: w/32
The color of the circle: ( 0, 0, 255 ) which means Red in BGR
Since thickness = -1, the circle will be drawn filled.
'''
cv2.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), blank.shape[1] // 32, (0, 0, 255), thickness=-1)
cv2.imshow("Circle", blank)

# draw a line
'''
Draw a line from Point start to Point end
The line is displayed in the image img
The line color is defined by ( 0, 0, 0 ) which is the RGB value correspondent to Black
The line thickness is set to thickness (in this case 2)
The line is a 8-connected one (lineType = 8)
'''
cv2.line(blank, (blank.shape[1] // 2, blank.shape[0] // 2), (blank.shape[1]//2, blank.shape[0]), (255, 0, 0), thickness=10, lineType= cv2.LINE_AA)
cv2.imshow("Line", blank)
# write text

# draw an ellipse
'''
From the code above, we can observe that the function ellipse() draws an ellipse such that:
The ellipse is displayed in the image img
The ellipse center is located in the point (w/2, w/2) and is enclosed in a box of size (w/4, w/16)
The ellipse is rotated angle degrees
The ellipse extends an arc between 0 and 360 degrees
The color of the figure will be ( 255, 0, 0 ) which means blue in BGR value.
The ellipse's thickness is 2.
'''
cv2.ellipse(blank, (blank.shape[1] // 2, blank.shape[0] // 2), (blank.shape[1] // 4, blank.shape[0] // 16), 0, 0, 360,
            (255, 0, 0), 2)
cv2.imshow("Ellipse1", blank)
cv2.ellipse(blank, (blank.shape[1] // 2, blank.shape[0] // 2), (blank.shape[1] // 4, blank.shape[0] // 16), 90, 0, 360,
            (255, 0, 0), 2)
cv2.imshow("Ellipse2", blank)
cv2.ellipse(blank, (blank.shape[1] // 2, blank.shape[0] // 2), (blank.shape[1] // 4, blank.shape[0] // 16), 45, 0, 360,
            (255, 0, 0), 2)
cv2.imshow("Ellipse3", blank)
cv2.ellipse(blank, (blank.shape[1] // 2, blank.shape[0] // 2), (blank.shape[1] // 4, blank.shape[0] // 16), -45, 0, 360,
            (255, 0, 0), 2)
cv2.imshow("Ellipse4", blank)
# draw a polygon

text = 'Life is short, you need Python!'
text = textwrap3.fill(text, width=50)
cv2.putText(blank, text, (100, 100), cv2.FONT_ITALIC, 1.0, (0, 255, 0), thickness=2)
cv2.imshow("Text", blank)

img_gray = cv2.cvtColor(blank, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", img_gray)

# write to a file
cv2.imwrite("../../images/draw.png", blank)

cv2.waitKey(0)
cv2.destroyAllWindows()
