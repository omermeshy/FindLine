import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

listImgs = os.listdir("C:\Projects\FindLine\output40")
print(listImgs)
#cv2.imshow('frame', listImgs)
kernel = np.ones((5, 5), np.uint8)
name = ["frame1", "frame2", "frame3", "frame4", "frame5", "frame6", "frame7", "frame8", "frame9", "frame10", "frame11", "frame12", "frame13", "frame14", "frame15", "frame16", "frame17", "frame18", "frame19", "frame20"]
x = 0
for frame in listImgs:
    frame = cv2.imread("C:/Projects/FindLine/output40/" + frame)
    cv2.imshow(name[x] + "org", frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, frame = cv2.threshold(frame, 230, 255, cv2.THRESH_BINARY)
    frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)
    frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel, iterations=2)
    frame = cv2.morphologyEx(frame, cv2.MORPH_DILATE, kernel, iterations=2)
    #frame = cv2.morphologyEx(frame, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow(name[x] + "after", frame)
    x+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
