import random

from Physics import Math as M
from Physics import Ball as B
import time
import WinGUI
import pygame
from pingPong.constants import Constants as c
import hands.HandTrackModel as HandTrackModel
import cv2

bounds = [M.BoundRect(M.Vector3(-500, -500, 0), M.Vector3(500, 500, 1000), M.Vector3(0, 0, 0), True)]
player_paddle = M.BoundRect(M.Vector3(-200, -200, 0), M.Vector3(200, 200, 100), M.Vector3(0, 0, 50), False)
ai_paddle = M.BoundRect(M.Vector3(-50, -50, 970), M.Vector3(50, 50, 1000), M.Vector3(0, 0, 985), False)

bounds.append(player_paddle)
bounds.append(ai_paddle)

ball = B.Ball(50, M.Vector3(0, 0, 500), M.Vector3(1000, 100, 1000), bounds)
w = WinGUI.DrawableWin(ball)


running = True
hasCamera = False

lastTime = time.time()
# set up webcam video capture device
for i in range(4):
    cap = cv2.VideoCapture(0)
    try:
        print(cap.read())
        break
    except:
        pass


#prevPaddleX, prevPaddleY = pygame.mouse.get_pos()
prevPaddleX, prevPaddleY = 0,0
myHands = None


# points stored in memory for averaging
pointLength = 6
lastPoints = [(0, 0)] * pointLength


# calculate the average of the last points
def averageOfLast(points):
    # average = [int(np.mean(points[0])),int(np.mean(points[1]))]
    vx = 0
    vy = 0
    for v in range(len(points) - 1):
        vx = points[v][0]*3 + vx
        vy = points[v][1]*3 + vy
    average = (int(vx / (len(points) - 1)), int(vy / (len(points) - 1)))
    # print(points)
    # print(average)
    return average


def setPoints(coordList):
    # remove the last point in the list and add the new one
    if coordList:
        lastPoints.pop(0)
        lastPoints.append(coordList[0])



    # get the average of the points
    average = averageOfLast(lastPoints)

    posX = c.windowDims[0] * (average[0] / myHands.w) / 2
    posY = c.windowDims[1] * (average[1] / myHands.h) / 2

    return posX, posY




average = (0,0)
paddleX, paddleY = average

frame_state = 'menu'

button1Fac = 0
button2Fac = 0

pygame.init()

while running:
    # Calculate delta time in seconds
    currentTime = time.time()
    deltaTime = (currentTime - lastTime)
    lastTime = currentTime

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if hasCamera:
        ret, frame = cap.read()
        # setup hands model if it does not exist
        if myHands is None:
            myHands = HandTrackModel.Track(len(frame[0]), len(frame))
            print('set')
            mouseCoords = (0, 0)
        else:
            # pass the frame and list of points for tracking
            frame, coordList = (myHands.get_hand_position(frame, [4]))

            # remove the last point in the list and add the new one
            if coordList:
                lastPoints.pop(0)
                lastPoints.append(coordList[0])
            #mouseCoords = setPoints(coordList)

            posX = c.windowDims[0] * (average[0] / myHands.w) * 2
            posY = c.windowDims[1] * (average[1] / myHands.h) * 2

            mouseCoords = (posX, posY)
            '''for i in range(len(lastPoints)-1):
                cv2.circle(frame, (lastPoints[i][0],lastPoints[i][1]), 15, [255, 255, 0])'''

            # get the average of the points
            average = averageOfLast(lastPoints)

            # circle each of the last points and the average point
            '''for coord in lastPoints:
                cv2.circle(frame, (coord[0], coord[1]), 15, [255, 255, 0], 2)'''


            #cv2.circle(frame, (average[0], average[1]), 15, [0, 255, 255], 2)

            # display the resulting frame
            cv2.imshow('frame', frame)
    if not hasCamera:
        mouseCoords = pygame.mouse.get_pos()

    paddleX, paddleY = mouseCoords
    lastPoints.pop(0)
    lastPoints.append(mouseCoords)

    deltaBlock = M.Vector3(paddleX - c.halfDims[0], c.windowDims[1] - paddleY - c.halfDims[1], 50)
    ball.bounds[1].moveBlock(deltaBlock)
    # ball.bounds[2].moveBlock(M.Vector3(ball.pos.x, ball.pos.y, 0))

    if frame_state == 'game':
        ball.PhysicsTick(deltaTime)
        w.drawFrameGame(True)
        if ball.lives <= 0:
            w.activateGameOver()
            frame_state = 'gameover'
            c.score = 0
            ball.lives = 3
            ball.pos = M.Vector3(0, 0, 500)
            ball.velocity = M.Vector3(random.randint(-1000, 1000), random.randint(-1000, 1000), 1000)
    elif frame_state == 'menu':
        # c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.windowDims[1] - 100
        if c.halfDims[0] + 50 < paddleX < c.windowDims[0] - 50 and 50 < paddleY < c.windowDims[1] - 50:
            button1Fac += 0.007
            if button1Fac > 1:
                button1Fac = 1
                if w.activateGame(True):
                    lastTime = time.time()
                    frame_state = 'game'
        else:
            button1Fac -= 0.01
            if button1Fac < 0:
                button1Fac = 0

        if 50 < paddleX < 450 and 50 < paddleY < 250:
            button2Fac += 0.007
            if button2Fac > 1:
                button2Fac = 1
        else:
            button2Fac -= 0.01
            if button2Fac < 0:
                button2Fac = 0

        w.drawFrameMenu(lastPoints, button1Fac, button2Fac)
    elif frame_state == 'gameover':
        # c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.halfDims[1] - 100
        if c.halfDims[0] + 50 < paddleX < c.windowDims[0] - 50 and 50 < paddleY < c.halfDims[1] - 50:
            button1Fac += 0.007
            if button1Fac > 1:
                button1Fac = 1
                if w.activateGame(False):
                    lastTime = time.time()
                    frame_state = 'game'
        else:
            button1Fac -= 0.01
            if button1Fac < 0:
                button1Fac = 0

        # 50, 50, c.halfDims[0] - 100, c.halfDims[1] - 100
        if 50 < paddleX < c.halfDims[0] - 50 and 50 < paddleY < c.halfDims[1] - 50:
            button2Fac += 0.007
            if button2Fac > 1:
                button2Fac = 1
                break
        else:
            button2Fac -= 0.01
            if button2Fac < 0:
                button2Fac = 0
        w.drawFrameGameover(lastPoints, button1Fac, button2Fac, True)

pygame.quit()