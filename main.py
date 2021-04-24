from Physics import Math as M
from Physics import Ball as B
import time
import WinGUI
import pygame

width, height = 1920, 1080
gravity = M.Vector3(0, -9.8, 0)

floor = [M.BoundRect(M.Vector3(-20, 0, -20), M.Vector3(20, 1, 20), False)]
ball = B.Ball(50, M.Vector3(0, 100, 0), M.Vector3(2, 0, 0), floor)
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
