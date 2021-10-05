import cv2

frame=cv2.imread('bird.jpg',1)
cv2.imshow('image source',frame)
cv2.waitKey(0)
