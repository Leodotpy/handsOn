import math

import cv2
import mediapipe as mp
from mediapipe import solutions
import numpy as np
import os
import ctypes
import time
import pyautogui
import HandTrackModel
from rich import print

# setup pyautogui for moving the mouse
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

# set up webcam video capture device
cap = cv2.VideoCapture(1)

# set up hand tracking using mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# get size of user's monitor
monWidth, monHeight = pyautogui.size()
print(monWidth, monHeight)


# move mouse cursor to hand
def moveMouse(cx, cy, w, h):
    offsetX = int(w / 10)
    offsetY = int(h / 8)  #

    # mouse.click(button="left")
    # mouse.move(cx/w*monWidth,cy/h*monHeight)
    pyautogui.moveTo((cx - offsetX) / (w - (offsetX * 2)) * monWidth,
                     (cy - offsetY) / (h - (offsetY * 2)) * monHeight)


myHands = None

# points stored in memory for averaging
pointLength = 16
lastPoints = [(0, 0)] * pointLength


# calculate the average of the last points
def averageOfLast(points):
    # average = [int(np.mean(points[0])),int(np.mean(points[1]))]
    vx = 0
    vy = 0

    for v in range(len(points) - 1):
        vx = points[v][0] + vx
        vy = points[v][1] + vy

    average = (int(vx / (len(points) - 1)), int(vy / (len(points) - 1)))

    # print(points)
    # print(average)
    return average


# loop
while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # setup hands model if it does not exist
    if myHands is None:
        myHands = HandTrackModel.Track(len(frame[0]), len(frame), monWidth, monHeight)
        print('set')
    else:
        # pass the frame and list of points for tracking
        frame, coordList = (myHands.get_hand_position(frame, [4]))

        # remove the last point in the list and add the new one
        if coordList:
            lastPoints.pop(0)
            lastPoints.append(coordList[0])

            '''for i in range(len(lastPoints)-1):
                cv2.circle(frame, (lastPoints[i][0],lastPoints[i][1]), 15, [255, 255, 0])'''

        # get the average of the points
        average = averageOfLast(lastPoints)

        # circle each of the last points and the average point
        for coord in lastPoints:
            cv2.circle(frame, (coord[0], coord[1]), 15, [255, 255, 0], 2)

        cv2.circle(frame, (average[0], average[1]), 15, [0, 255, 255], 2)

        # display the resulting frame
        cv2.imshow('frame', frame)

    # end if user presses q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
