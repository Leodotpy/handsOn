import numpy
import pygame
from pygame import *


class DrawableWin:
    # Declare Width and Height of window
    width, height = 1920, 1080
    #background color
    backCol = [16, 16, 16]
    ballCol = [200, 200, 200]

    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode([self.width, self.height])
        running = True


circleColorR, circleColorG, circleColorB = 140, 136, 138

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

while running:

    clock.tick(600)
    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((backR, backG, backB))


    def getMouseCoords():
        x, y = pygame.mouse.get_pos()
        return (x, y)


    # Draw a solid blue circle in the center

    lastPoints.pop(0)
    lastPoints.append(getMouseCoords())

    for i in range(trailLength):
        # circleColorR, circleColorG, circleColorB

        temp = i / trailLength

        currentColorR, currentColorG, currentColorB = int(circleColorR * temp + backR * (1 - temp)), int(
            circleColorG * temp + backG * (1 - temp)), int(circleColorB * temp + backB * (1 - temp))

        # print(currentColorR, currentColorG, currentColorB)
        pygame.draw.circle(screen, (currentColorR, currentColorG, currentColorB), (lastPoints[i]), 100)

    # Flip the display

    pygame.display.flip()

# Done! Time to quit.

pygame.quit()
