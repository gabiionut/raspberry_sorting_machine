import numpy as np
import cv2
img = cv2.imread('image.jpg',1)
cp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(cp,150,255,0)
cv2.imshow('img',thresh) 
cv2.waitKey(0)
im2,contours,hierarchy = cv2.findContours(thresh.astype(np.uint8), 1, 2)
cnts = contours
for cnt in cnts:
    if cv2.contourArea(cnt) >800: # filter small contours
        x,y,w,h = cv2.boundingRect(cnt) # offsets - with this you get 'mask'
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('cutted contour',img[y:y+h,x:x+w])
        print('Average color (BGR): ',np.array(cv2.mean(img[y:y+h,x:x+w])).astype(np.uint8))
        cv2.waitKey(0)
cv2.imshow('img',img) 
cv2.waitKey(0)
cv2.destroyAllWindows()