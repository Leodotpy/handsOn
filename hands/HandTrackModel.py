import cv2
import mediapipe as mp
from mediapipe import solutions
import numpy as np
import os
import ctypes
import time
import pyautogui as mouse

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2)
mpDraw = mp.solutions.drawing_utils

#Gets hand positions --> returns list: hand_list[integer: hand
def get_hand_position(frame):
    frame = cv2.flip(frame, 1)
    camRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hand_list = []
    results = hands.process(camRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            hand_list.append(handLms.landmark)
    return hand_list

#Returns a cleaned point into an integer value (x,y,z)
#Input: point = (x, y, z), w/h = w and h of frame, mons = window width/height
def clean_point_to_int(point, w, h, monWidth, monHeight):
    offsetX = int(w / 10)
    offsetY = int(h / 8)
    x = (point[0] - offsetX) / (w - (offsetX * 2)) * monWidth
    y = (point[1] - offsetY) / (h - (offsetY * 2)) * monHeight
    z = point[2]
    return (x, y, z)