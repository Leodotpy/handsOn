import math
import pygame
from pingPong.constants import Constants as c
from Physics.ColorMath import Color as co

class Vector3:
    x, y, z = 0, 0, 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Returns new vector of addition
    def add(self, B):
        return Vector3(self.x + B.x, self.y + B.y, self.z + B.z)

    # Returns inverse of this vector
    def invert(self):
        return Vector3(-self.x, -self.y, -self.z)

    # Subtract Vector from this vector
    def subtract(self, B):
        return self.add(B.invert())

    # Multiply Vector by float
    def multiply(self, B):
        return Vector3(self.x * B, self.y * B, self.z * B)

    # Divide Vector by float
    def divide(self, B):
        if B == 0:
            return Vector3(0, 0, 0)

        return self.multiply(1 / B)

    # Calculate Dot Product of this vector and another
    def dot(self, B):
        return self.x * B.x + self.y * B.y + self.z * B.z

    def length2(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def length(self):
        return math.sqrt(self.length2())

    def normalized(self):
        return self.divide(self.length())

    def depthAdjustFactor(self):
        return 1-(self.z/2000)


class BoundRect:
    C1, C2 = Vector3(0, 0, 0), Vector3(0, 0, 0)
    concave = False

    leftVal, rightVal, topVal, botVal, backVal, frontVal = 0, 0, 0, 0, 0, 0
    fadeAmount = 0.02

    def __init__(self, C1, C2, pos, concave):
        self.pos = pos
        self.diff1 = C1
        self.diff2 = C2
        self.C1 = C1
        self.C2 = C2
        self.concave = concave

    def moveBlock(self, position):
        self.pos = position
        self.C1 = self.diff1.add(position)
        self.C2 = self.diff2.add(position)

    def drawWire(self, screen, width):
        c1Fac = self.C1.depthAdjustFactor()
        c2Fac = self.C2.depthAdjustFactor()

        # Front Right
        pygame.draw.line(screen, (200, 200, 200), (self.C2.x*c1Fac+c.halfDims[0], c.windowDims[1]-self.C1.y*c1Fac-c.halfDims[1]), (self.C2.x*c1Fac+c.halfDims[0], c.windowDims[1]-self.C2.y*c1Fac-c.halfDims[1]), width)
        # Front Left
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c1Fac+c.halfDims[0], c.windowDims[1]-self.C1.y*c1Fac-c.halfDims[1]), (self.C1.x*c1Fac+c.halfDims[0], c.windowDims[1]-self.C2.y*c1Fac-c.halfDims[1]), width)
        # Front Top
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c1Fac+c.halfDims[0], c.windowDims[1]-self.C2.y*c1Fac-c.halfDims[1]), (self.C2.x*c1Fac+c.halfDims[0], c.windowDims[1]-self.C2.y*c1Fac-c.halfDims[1]), width)
        # Front Bottom
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c1Fac+c.halfDims[0], c.windowDims[1]-self.C1.y*c1Fac-c.halfDims[1]), (self.C2.x*c1Fac+c.halfDims[0], c.windowDims[1]-self.C1.y*c1Fac-c.halfDims[1]), width)

        # Back Right
        pygame.draw.line(screen, (200, 200, 200), (self.C2.x*c2Fac+c.halfDims[0], c.windowDims[1]-self.C1.y*c2Fac-c.halfDims[1]), (self.C2.x*c2Fac+c.halfDims[0], c.windowDims[1]-self.C2.y*c2Fac-c.halfDims[1]), width)
        # Back Left
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c2Fac+c.halfDims[0], c.windowDims[1]-self.C1.y*c2Fac-c.halfDims[1]), (self.C1.x*c2Fac+c.halfDims[0], c.windowDims[1]-self.C2.y*c2Fac-c.halfDims[1]), width)
        # Back Top
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c2Fac+c.halfDims[0], c.windowDims[1]-self.C2.y*c2Fac-c.halfDims[1]), (self.C2.x*c2Fac+c.halfDims[0], c.windowDims[1]-self.C2.y*c2Fac-c.halfDims[1]), width)
        # Back Bottom
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c2Fac+c.halfDims[0], c.windowDims[1]-self.C1.y*c2Fac-c.halfDims[1]), (self.C2.x*c2Fac+c.halfDims[0], c.windowDims[1]-self.C1.y*c2Fac-c.halfDims[1]), width)

        # Bottom Left
        pygame.draw.line(screen, (255, 255, 255),
                         (self.C1.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c1Fac - c.halfDims[1]),
                         (self.C1.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c2Fac - c.halfDims[1]),
                         width)

        # Bottom Right
        pygame.draw.line(screen, (200, 200, 200),
                         (self.C2.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c1Fac - c.halfDims[1]),
                         (self.C2.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c2Fac - c.halfDims[1]),
                         width)

        # Top Left
        pygame.draw.line(screen, (200, 200, 200),
                         (self.C1.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c1Fac - c.halfDims[1]),
                         (self.C1.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c2Fac - c.halfDims[1]),
                         width)

        # Top Right
        pygame.draw.line(screen, (200, 200, 200),
                         (self.C2.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c1Fac - c.halfDims[1]),
                         (self.C2.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c2Fac - c.halfDims[1]),
                         width)


    def drawFillRight(self, screen, c1, c2):
        c1Fac = self.C1.depthAdjustFactor()
        c2Fac = self.C2.depthAdjustFactor()

        col = co(c1).interpColors(c2, self.rightVal)

        points = [(self.C2.x*c1Fac + c.halfDims[0], c.windowDims[1] - self.C1.y*c1Fac - c.halfDims[1]),
                (self.C2.x*c2Fac + c.halfDims[0], c.windowDims[1] - self.C1.y*c2Fac - c.halfDims[1]),
                (self.C2.x*c2Fac + c.halfDims[0], c.windowDims[1] - self.C2.y*c2Fac - c.halfDims[1]),
                (self.C2.x*c1Fac + c.halfDims[0], c.windowDims[1] - self.C2.y*c1Fac - c.halfDims[1])]

        co.drawPoly(screen, col, points)
        if (self.rightVal > 0):
            self.rightVal -= self.fadeAmount
        else:
            self.rightVal = 0

    def drawFillLeft(self, screen, c1, c2):
        c1Fac = self.C1.depthAdjustFactor()
        c2Fac = self.C2.depthAdjustFactor()

        col = co(c1).interpColors(c2, self.leftVal)

        points = [(self.C1.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c1Fac - c.halfDims[1]),
                  (self.C1.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c2Fac - c.halfDims[1]),
                  (self.C1.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c2Fac - c.halfDims[1]),
                  (self.C1.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c1Fac - c.halfDims[1])]

        co.drawPoly(screen, col, points)
        if (self.leftVal > 0):
            self.leftVal -= self.fadeAmount
        else:
            self.leftVal = 0

    def drawFillTop(self, screen, c1, c2):
        c1Fac = self.C1.depthAdjustFactor()
        c2Fac = self.C2.depthAdjustFactor()

        col = co(c1).interpColors(c2, self.topVal)

        points = [(self.C1.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c1Fac - c.halfDims[1]),
                  (self.C1.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c2Fac - c.halfDims[1]),
                  (self.C2.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c2Fac - c.halfDims[1]),
                  (self.C2.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c1Fac - c.halfDims[1])]

        co.drawPoly(screen, col, points)
        if (self.topVal > 0):
            self.topVal -= self.fadeAmount
        else:
            self.topVal = 0

    def drawFillBottom(self, screen, c1, c2):
        c1Fac = self.C1.depthAdjustFactor()
        c2Fac = self.C2.depthAdjustFactor()

        col = co(c1).interpColors(c2, self.botVal)

        points = [(self.C1.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c1Fac - c.halfDims[1]),
                  (self.C1.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c2Fac - c.halfDims[1]),
                  (self.C2.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c2Fac - c.halfDims[1]),
                  (self.C2.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c1Fac - c.halfDims[1])]

        co.drawPoly(screen, col, points)
        if (self.botVal > 0):
            self.botVal -= self.fadeAmount
        else:
            self.botVal = 0

    def drawFillFront(self, screen, c1, c2):
        c1Fac = self.C1.depthAdjustFactor()
        c2Fac = self.C2.depthAdjustFactor()

        col = co(c1).interpColors(c2, self.frontVal)

        points = [(self.C1.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c1Fac - c.halfDims[1]),
                  (self.C2.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c1Fac - c.halfDims[1]),
                  (self.C2.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c1Fac - c.halfDims[1]),
                  (self.C1.x * c1Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c1Fac - c.halfDims[1])]

        co.drawPoly(screen, col, points)
        if (self.frontVal > 0):
            self.frontVal -= self.fadeAmount
        else:
            self.frontVal = 0

    def drawFillBack(self, screen, c1, c2):
        c1Fac = self.C1.depthAdjustFactor()
        c2Fac = self.C2.depthAdjustFactor()

        col = co(c1).interpColors(c2, self.backVal)

        points = [(self.C1.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c2Fac - c.halfDims[1]),
                  (self.C2.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C1.y * c2Fac - c.halfDims[1]),
                  (self.C2.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c2Fac - c.halfDims[1]),
                  (self.C1.x * c2Fac + c.halfDims[0], c.windowDims[1] - self.C2.y * c2Fac - c.halfDims[1])]

        co.drawPoly(screen, col, points)
        if (self.backVal > 0):
            self.backVal -= self.fadeAmount
        else:
            self.backVal = 0
