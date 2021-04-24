import cv2
import mediapipe as mp
from mediapipe import solutions
import numpy as np
import os
import ctypes
import time
import pyautogui as mouse

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
monWidth, monHeight = mouse.size()

def create_video_stream():
    cap = cv2.VideoCapture(1)

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
                cz = handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].z

                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
