import cv2
import numpy as np
from stack_images import stackImages
from get_contours import getContours
from resize import resize
from picamera import PiCamera
from time import sleep
from motor import start, stop, right, left, clear
from ir_sensor import objectDetected


def empty(a):
    pass

# TODO: delete next lines after threshold found
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 40, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 40, 255, empty)
cv2.createTrackbar("Area", "Parameters", 5000, 30000, empty)

def classifyForm(form):
    # By form
    if form.corners == 4:
        print("Patrulater")
        sleep(1)
        left()
        sleep(1)
        start()
    if form.corners == 3:
        print("Triunghi")
        sleep(1)
        right()
        sleep(1)
        start()
    if form.corners == 6:
        print("Hexagon")

    # By size
    #if (form.area <= 35792):
        #print("Small")
        #start()
        #left()
    #if (form.area > 35792):
        #print("Big")
        #start()
        #right()

    # TODO: By color
    

def run():
    start()
    sleep(1)
    while True:
      if objectDetected():
          print("Object detected")
          sleep(2)
          stop()
          break
    #left()
    #GPIO.cleanup()
    camera = PiCamera()
    #camera.crop(0.25, 0.25, 0.5, 0.5)
    #camera.start_preview()
    camera.capture('image.jpg')
    #camera.stop_preview()
    ogImg = cv2.imread('image.jpg')
    colorImg = ogImg.copy()
    img = resize(ogImg, 50)
    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)


    # TODO: delete next two lines after threshold found
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    print(threshold1)
    print(threshold2)

    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((5, 5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    form = getContours(imgDil, imgContour)
    classifyForm(form)

    imgStack = stackImages(0.8, ([img, imgCanny],
                                 [imgDil, imgContour]))
    cv2.imshow("Result", imgStack)
    cv2.waitKey(0)
    stop()
    clear()
run()