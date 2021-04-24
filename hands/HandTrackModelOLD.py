import cv2
import mediapipe as mp
from mediapipe import solutions
import numpy as np
import os
import ctypes
import time
import pyautogui as mouse


class Track:
    def __init__(self, frame, fw, fh, monWidth, monHeight):

        mpHands = mp.solutions.hands
        hands = mpHands.Hands(min_tracking_confidence=0.5,
                              min_detection_confidence=0.5)
        self.frame = frame

        self.results = hands.process(self.frame)
        self.hand_list = []
        self.camRGB = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        self.mpHands = mp.solutions.hands
        self.hands = mpHands.Hands(max_num_hands=2)
        self.mpDraw = mp.solutions.drawing_utils

        self.w = fw
        self.h = fh

        self.monWidth = monWidth
        self.monHeight = monHeight

    # Gets hand positions --> returns list: hand_list[integer: hand
    def get_hand_position(self, frame):

        self.frame = cv2.flip(self.frame, 1)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                self.hand_list.append(handLms.landmark)
        return self.hand_list

    # Returns a cleaned point into an integer value (x,y,z)
    # Input: point = (x, y, z), w/h = w and h of frame, mons = window width/height
    def clean_point_to_int(self, point):
        offsetX = int(self.w / 10)
        offsetY = int(self.h / 8)
        x = (point[0] - offsetX) / (self.w - (offsetX * 2)) * self.monWidth
        y = (point[1] - offsetY) / (self.h - (offsetY * 2)) * self.monHeight
        z = point[2]
        return x, y, z
