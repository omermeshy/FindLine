import cv2
import numpy as np
import matplotlib.pyplot as plt

num_of_corners_to_detect = int(input("How much corners you want to find?"))
capture = cv2.VideoCapture(0)

while(capture.isOpened()):
    ret, frame = capture.read()
    frame = cv2.flip(frame, 180)


    frame_corners = frame
    frame_corners = cv2.cvtColor(frame_corners,cv2.COLOR_BGR2RGB)

    gray_frame_corners = cv2.cvtColor(frame_corners,cv2.COLOR_BGR2GRAY)

    #run the function with defaults
    corners = cv2.goodFeaturesToTrack(gray_frame_corners, num_of_corners_to_detect, 0.01, 10)
    #convert corners to integers
    corners = np.int0(corners)
    #drawing the circles/dots
    for i in corners:
        x, y = i.ravel()
        cv2.circle(frame, (x, y), 3, 255, -1)
    plt.figure(figsize=(10, 10))
    plt.imshow(frame)

    cv2.imshow('frame1', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
