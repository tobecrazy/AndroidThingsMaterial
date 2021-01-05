import cv2
from time import sleep

cap = cv2.VideoCapture(0)
  
while True:
  ret,frame = cap.read()
  # Our operations on the frame come here
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Display the resulting frame
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  
sleep(1) 
cap.release()
cv2.destroyAllWindows() 