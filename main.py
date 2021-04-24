from Physics import Math as M
from Physics import Ball as B
import time
import WinGUI
import pygame

width, height = 1920, 1080
gravity = M.Vector3(0, -9.8, 0)

bounds = [M.BoundRect(M.Vector3(-500, -500, 100), M.Vector3(500, 500, 1100), True)]

player_paddle = M.BoundRect(M.Vector3(-250, 0, 100), M.Vector3(-100, 100, 101), False)
ai_paddle = M.BoundRect(M.Vector3(-250, 0, 1100), M.Vector3(-100, 100, 1099), False)

bounds.append(player_paddle)
bounds.append(ai_paddle)

ball = B.Ball(50, M.Vector3(0, 100, 0), M.Vector3(100, 100, 100), bounds)

w = WinGUI.DrawableWin(ball)

running = True

lastTime = time.time()
while running:
    # Calculate delta time in seconds
    currentTime = time.time()
    deltaTime = (currentTime - lastTime)
    lastTime = currentTime

    ball.PhysicsTick(deltaTime)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    w.drawFrame()

pygame.quit()
