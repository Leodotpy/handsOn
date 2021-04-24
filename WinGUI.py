import numpy
import pygame
from pygame import *
from Physics import Ball as b
from pingPong.constants import Constants as c


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
        font = pygame.font.SysFont(None, 70)
        img = font.render('Score:' + str(c.score), True, (255, 255, 255))
        self.screen.blit(img, (30, c.halfDims[1]))

        # Draw arena first
        self.ball.bounds[0].drawFillBack(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[0].drawFillRight(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[0].drawFillLeft(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[0].drawFillTop(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[0].drawFillBottom(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[0].drawFillFront(self.screen, (255, 0, 0, 255), (100, 100, 100, 20))
        self.ball.bounds[0].drawWire(self.screen, 2)

        # Draw opponent second
        self.ball.bounds[2].drawFillBack(self.screen, (100, 100, 100, 100), (150, 100, 100, 20))
        self.ball.bounds[2].drawFillRight(self.screen, (100, 100, 100, 100), (150, 100, 100, 20))
        self.ball.bounds[2].drawFillLeft(self.screen, (100, 100, 100, 100), (150, 100, 100, 20))
        self.ball.bounds[2].drawFillTop(self.screen, (100, 100, 100, 100), (150, 100, 100, 20))
        self.ball.bounds[2].drawFillBottom(self.screen, (100, 100, 100, 100), (150, 100, 100, 20))
        self.ball.bounds[2].drawFillFront(self.screen, (255, 0, 0, 255), (150, 100, 100, 20))
        self.ball.bounds[2].drawWire(self.screen, 2)

        # Draw player on top
        self.ball.bounds[1].drawFillBack(self.screen, (100, 255, 130, 255), (100, 100, 100, 20))
        self.ball.bounds[1].drawFillRight(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[1].drawFillLeft(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[1].drawFillTop(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[1].drawFillBottom(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[1].drawFillFront(self.screen, (100, 100, 100, 100), (100, 100, 100, 20))
        self.ball.bounds[1].drawWire(self.screen, 2)

        self.ball.draw(self.screen)

        pygame.display.flip()
        pygame.display.update()
