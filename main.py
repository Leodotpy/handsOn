from Physics import Math as M
from Physics import Ball as B
import time
import WinGUI
import pygame
from pingPong.constants import Constants as c

width, height = 1920, 1080

bounds = [M.BoundRect(M.Vector3(-500, -500, 0), M.Vector3(500, 500, 1000), M.Vector3(0, 0, 0), True)]

player_paddle = M.BoundRect(M.Vector3(-200, -200, 0), M.Vector3(200, 200, 100), M.Vector3(0, 0, 50), False)
ai_paddle = M.BoundRect(M.Vector3(-50, -50, 970), M.Vector3(50, 50, 1000), M.Vector3(0, 0, 985), False)

bounds.append(player_paddle)
bounds.append(ai_paddle)

ball = B.Ball(50, M.Vector3(0, 0, 500), M.Vector3(1000, 100, 1000), bounds)

w = WinGUI.DrawableWin(ball)

running = True

lastTime = time.time()
prevMouseX, prevMouseY = pygame.mouse.get_pos()
while running:
    # Calculate delta time in seconds
    currentTime = time.time()
    deltaTime = (currentTime - lastTime)
    lastTime = currentTime

    ball.PhysicsTick(deltaTime)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouseX, mouseY = pygame.mouse.get_pos()

    deltaBlock = M.Vector3(mouseX - c.halfDims[0], c.windowDims[1]-mouseY-c.halfDims[1], 50)
    ball.bounds[1].moveBlock(deltaBlock)
    ball.bounds[2].moveBlock(M.Vector3(ball.pos.x, ball.pos.y, 0))

    w.drawFrame()


pygame.quit()
