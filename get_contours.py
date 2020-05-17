import cv2
import numpy
from form import Form

def getContours(img, imgContour):
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
            
            grain = numpy.int0(cv2.boxPoints(cv2.minAreaRect(cnt)))
            centroid = grain[2][1] - (grain[2][1]-grain[0][1])//2, grain[2][0] - (grain[2][0]-grain[0][0])//2
            print(centroid)
            color = image[centroid]
            print(image)
            form = Form(corners, area, 'red')

            # Draw result on image
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)
    return form
