import Jetson.GPIO as GPIO
import freenect
import cv2
import frame_convert2
import numpy as np


threshold = 500
current_depth = 500

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while 1:
    depth, timestamp = freenect.sync_get_depth()
    depth = 255 * np.logical_and(depth >= 0, depth <= 400)
    depth = depth.astype(np.uint8)
    #cv2.imshow('Depth', depth)

    kernel = np.ones((2,2),np.uint8)
    depth = cv2.erode(depth,kernel, iterations = 1)
    kernel = np.ones((10000,10000),np.uint8) #decrease the 10000 to improve performance probably, but reliability takes hit
    depth = cv2.dilate(depth,kernel, iterations = 1)

    #cv2.imshow('Obstacle', depth)

    if depth[0][0] == 255:
        GPIO.output(17, GPIO.HIGH)
        print("Obstacle")
    else:
        GPIO.output(17, GPIO.LOW)
        print("ok")

    if cv2.waitKey(10) == 27:
        break
