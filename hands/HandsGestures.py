import cv2
import mediapipe as mp
from mediapipe import solutions
import numpy as np
import os
import ctypes
import time
import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

monWidth, monHeight = pyautogui.size()

print(monWidth, monHeight)


def moveMouse(cx, cy, w, h):
    offsetX = int(w / 10)
    offsetY = int(h / 8)

    # mouse.click(button="left")
    # mouse.move(cx/w*monWidth,cy/h*monHeight)
    pyautogui.moveTo((cx - offsetX) / (w - (offsetX * 2)) * monWidth,
               (cy - offsetY) / (h - (offsetY * 2)) * monHeight)


while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    # Our operations on the frame come here
    camRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(camRGB)
    # print(results.multi_hand_landmarks)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if results.multi_hand_landmarks:

        for handLms in results.multi_hand_landmarks:

            # get landmark and index number for landmark
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)

                w, h, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx,cy)

                if id == 8:
                    moveMouse(cx, cy, w, h)

            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

    # perform a naive attempt to find the (x, y) coordinates of
    # the area of the image with the largest intensity value
    '''(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    cv2.circle(cam, maxLoc, 5, (255, 0, 0), 2)'''

    # Display the resulting frame

    # frame = cv2.resize(frame,2)

    cv2.imshow('frame', frame)

    # print(len(frame[0]), len(frame))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
