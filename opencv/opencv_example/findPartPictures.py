import cv2
import numpy as np

# Read image
img = cv2.imread("../../images/limeng1.png").astype(np.float32)
H, W, C = img.shape

# Read template image
temp = cv2.imread("../../images/limeng_part.jpeg").astype(np.float32)
Ht, Wt, Ct = temp.shape


# Template matching
i, j = -1, -1
v = 255 * H * W * C
for y in range(H-Ht):
    for x in range(W-Wt):
        _v = np.sum((img[y:y+Ht, x:x+Wt] - temp) ** 2)
        if _v < v:
            v = _v
            i, j = x, y

out = img.copy()
cv2.rectangle(out, pt1=(i, j), pt2=(i+Wt, j+Ht), color=(0,0,255), thickness=1)
out = out.astype(np.uint8)
                
# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
