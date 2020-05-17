import cv2
import numpy
from form import Form

def getContours(img, imgContour, ogImage):
    contours, image = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    form = None
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = 5000
        if area > areaMin:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            corners = len(approx)
            area = int(area)
            #x,y,w,h = cv2.boundingRect(cnt) # offsets - with this you get 'mask'
            #cv2.rectangle(ogImage,(x,y),(x+w,y+h),(0,255,0),2)
            #rint('Average color (BGR): ',numpy.array(cv2.mean(ogImage[y:y+h,x:x+w])).astype(numpy.uint8))
            mask = numpy.zeros(img.shape, numpy.uint8)
            cv2.drawContours(mask, cnt, -1, 255, -1)
            mean = cv2.mean(ogImage, mask=mask)
            print(mean)
            
            form = Form(corners, area, 'red')

            # Draw result on image
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)
    return form
