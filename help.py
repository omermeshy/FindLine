import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while(capture.isOpened()):
    ret, frame = capture.read()
    frame = cv2.flip(frame, 180)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    kernel = np.ones((5, 5), np.uint8)

    erosion = cv2.erode(frame, kernel, iterations=1)
    dilation = cv2.dilate(frame, kernel, iterations=1)
    opening = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow('orig', frame)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    cv2.imshow('gradient', gradient)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
