import cv2
import mediapipe as mp
from mediapipe import solutions
import numpy as np
import os
import ctypes
import time
import pyautogui as mouse

mpHands = mp.solutions.hands
hands = mpHands.Hands(min_tracking_confidence=0.5,
                      min_detection_confidence=0.5)
mpDraw = mp.solutions.drawing_utils
monWidth, monHeight = mouse.size()


def moveMouse(cx, cy, w, h):
    offsetX = int(w / 10)
    offsetY = int(h / 10)
    mouse.moveTo((cx - offsetX) / (w - (offsetX * 2)) * monWidth,
                 (cy - offsetY) / (h - (offsetY * 2)) * monHeight)


cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    camRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(camRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            w, h, c = frame.shape
            cx = int(handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].x * w)
            cy = int(handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y * h)
            # cz = handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].z
            # print(cz)
            # moveMouse(cx, cy, w, h)

            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()