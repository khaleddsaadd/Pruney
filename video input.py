import numpy as np
import  cv2
inputvideo = input("Enter your video name \n")
cap = cv2.VideoCapture(r'C:\xampp\htdocs\GraduationProject\Videos'+inputvideo+'.mp4')
while(cap.isOpened()):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',gray)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()