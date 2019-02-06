import cv2
import math
import numpy as np

capture = cv2.VideoCapture(0)

kernel = np.ones((5, 5), np.uint8)

while capture.isOpened():
    ret, frame = capture.read()
    frame = cv2.flip(frame, 180)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
    frame = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)
    face_img = frame.copy()

    cv2.imshow('video', face_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
