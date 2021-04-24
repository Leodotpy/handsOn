import numpy
import pygame
from pygame import *
from Physics import Ball as b


class DrawableWin:
    # Declare Width and Height of window
    width, height = 1920, 1080
    #background color
    backCol = [16, 16, 16]
    ballCol = [200, 200, 200]

    ball = b.Ball
    screen = pygame.display.set_mode([width, height])

    def __init__(self, ball):
        self.ball = ball
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        running = True
        # Fill the background with white
        self.screen.fill(self.backCol)
        #pygame.mouse.set_visible(False)
        clock = pygame.time.Clock()

    def drawFrame(self):
        self.screen.fill(self.backCol)
        for i in range(len(self.ball.bounds)):
            self.ball.bounds[i].drawFillRight(self.screen, [255, 100, 100, 50])
        self.ball.draw(self.screen)
        pygame.display.flip()
        pygame.display.update()
