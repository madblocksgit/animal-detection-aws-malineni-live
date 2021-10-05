import cv2
import time

cam=cv2.VideoCapture(0)
while True:
 result,frame=cam.read()
 if(result):
  cv2.imwrite('test.png',frame)
  cv2.imshow('capture window',frame)
  cv2.waitKey(1)
  
