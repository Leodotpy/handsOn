import cv2
import mediapipe as mp
from mediapipe import solutions
import numpy as np
import os
import ctypes
import time
import pyautogui

class Constants(object):
    gravity = -9.8
    simulationScale = 500
    timeMultiplier = 1
    windowDims = [1920, 1080]
    halfDims = [windowDims[0]/2, windowDims[1]/2]

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()

    mpDraw = mp.solutions.drawing_utils
    monWidth, monHeight = pyautogui.size()