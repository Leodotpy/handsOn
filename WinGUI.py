import time as t

import numpy
import pygame
from pygame import *
from Physics import Ball as b
from pingPong.constants import Constants as c
from Physics.ColorMath import Color as co


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

    def drawFrameMenu(self, mouseCoords, button1Fac, button2Fac):
        pygame.mouse.set_visible(False)
        self.screen.fill(self.backCol)
        pygame.draw.rect(self.screen, (179, 120, 43), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.windowDims[1] - 100))
        pygame.draw.rect(self.screen, (255, 163, 43), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, (c.windowDims[1] - 100) * button1Fac))
        pygame.draw.rect(self.screen, (179, 43, 43), pygame.Rect(50, 50, 400, 200))
        pygame.draw.rect(self.screen, (237, 14, 14), pygame.Rect(50, 50, 400, 200 * button2Fac))

        for i in range(len(mouseCoords)):
            co.draw_circle_alpha(self.screen, (255, 255, 255, 255*(i/(len(mouseCoords)-1))), mouseCoords[i], 50, 5)
        pygame.display.flip()
        pygame.display.update()

    def activateGame(self):
        for i in range(5):
            self.screen.fill(self.backCol)
            pygame.draw.rect(self.screen, (207, 154, 85), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.windowDims[1] - 100))
            pygame.display.flip()
            pygame.display.update()
            t.sleep(0.05)
            pygame.draw.rect(self.screen, (179, 120, 43), pygame.Rect(c.halfDims[0] + 50, 50, c.halfDims[0] - 100, c.windowDims[1] - 100))
            pygame.display.flip()
            pygame.display.update()
            t.sleep(0.05)

        for i in range(50):
            self.drawFrameGame(False)
            co.draw_rect_alpha(self.screen, (self.backCol[0], self.backCol[1], self.backCol[2], 255*(1-(i/49))), pygame.Rect(0,0, c.windowDims[0], c.windowDims[1]))
            pygame.display.flip()
            pygame.display.update()
            t.sleep(0.005)

        for i in range(3):
            self.drawFrameGame(False)
            font = pygame.font.SysFont(None, 500)
            img = font.render(str(3-i), True, (255, 255, 255))
            self.screen.blit(img, (c.halfDims[0] - 100, c.halfDims[1] - 150))
            pygame.display.flip()
            pygame.display.update()
            t.sleep(0.7)
        self.drawFrameGame(False)
        font = pygame.font.SysFont(None, 500)
        img = font.render("GO!", True, (255, 255, 255))
        self.screen.blit(img, (c.halfDims[0] - 330, c.halfDims[1] - 150))
        pygame.display.flip()
        pygame.display.update()
        t.sleep(0.7)
        return True


    def drawFrameGame(self, update):
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

        if update:
            pygame.display.flip()
            pygame.display.update()
