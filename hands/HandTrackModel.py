import cv2
import mediapipe as mp
from mediapipe import solutions
import numpy as np
import os
import ctypes
import time
import pyautogui as mouse


class Track:
    def __init__(self, fw, fh):

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(max_num_hands=1, min_tracking_confidence=0.5,
                                        min_detection_confidence=0.5)
        self.hand_list = []
        self.mpHands = mp.solutions.hands

        self.mpDraw = mp.solutions.drawing_utils

        self.w = fw
        self.h = fh

    # Gets hand positions --> returns list: hand_list[integer: hand
    def get_hand_position(self, frame, pointList):
        point = 0
        coordList = []

        frame = cv2.flip(frame, 1)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(frame)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):

                    cx, cy = int(lm.x * self.w), int(lm.y * self.h)
                    # print(id, cx, cy)

                    # print(point, pointList[point])
                    if point <= len(pointList) - 1:
                        if id == int(pointList[point]):
                            coordList.append([cx, cy])

                            point += 1

                #self.mpDraw.draw_landmarks(frame, handLms, self.mpHands.HAND_CONNECTIONS)

        return frame, coordList
        # self.hand_list.append(handLms.landmark)ZA
        # return self.hand_list
