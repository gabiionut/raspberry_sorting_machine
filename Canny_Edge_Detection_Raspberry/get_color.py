import numpy as np
import cv2
from picamera import PiCamera

camera = PiCamera()
camera.capture('image.jpg')
img = cv2.imread('image.jpg',1)
img = img[50:400, 0:500]
cv2.imshow('img',img) 
cv2.waitKey(0)

