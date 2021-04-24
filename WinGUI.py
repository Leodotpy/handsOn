import numpy
import pygame
from pygame import *
import Physics.Ball as b


class DrawableWin:
    # Declare Width and Height of window
    width, height = 500, 500
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
        pygame.mouse.set_visible(False)
        clock = pygame.time.Clock()

    def drawFrame(self):
        self.screen.fill(self.backCol)
        pygame.draw.circle(self.screen, (255, 255, 255), (self.ball.pos.x, self.ball.pos.y), 100)
        pygame.display.flip()
        pygame.display.update()
