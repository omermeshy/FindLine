import cv2
import numpy as np
import matplotlib.pyplot as plt

capture = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
while(capture.isOpened()):
    ret, frame = capture.read()
    frame = cv2.flip(frame, 180)
    cv2.imshow('frame01', frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, frame = cv2.threshold(frame, 230, 255, cv2.THRESH_BINARY)
    # frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
    cv2.imshow('frame02', frame)
    frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel, iterations=1)
    #frame = cv2.morphologyEx(frame, cv2.MORPH_DILATE, kernel, iterations=2)
    # frame = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow('frame03', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
