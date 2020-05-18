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
            
            M = cv2.moments(cnt)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            hsv = cv2.cvtColor(imgContour, cv2.COLOR_BGR2HSV)
            color = hsv[cY][cX] * [2, 1/2.55, 1/2.55]
            
            form = Form(corners, area, color)

            # Draw result on image
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)
    return form
