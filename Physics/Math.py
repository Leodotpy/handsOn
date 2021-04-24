import math
import pygame

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
        return self.Add(B.Invert())

    # Multiply Vector by float
    def multiply(self, B):
        return Vector3(self.x * B, self.y * B, self.z * B)

    # Divide Vector by float
    def divide(self, B):
        if B == 0:
            return Vector3(0, 0, 0)

        return self.Multiply(1 / B)

    # Calculate Dot Product of this vector and another
    def dot(self, B):
        return self.x * B.x + self.y * B.y + self.z * B.z

    def length2(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def length(self):
        return math.sqrt(self.Length2())

    def normalized(self):
        return self.Divide(self.Length())

    def depthAdjustFactor(self):
        if self.z == 0:
            return 0
        else:
            return 500/self.z


class BoundRect:
    C1, C2 = Vector3(0, 0, 0), Vector3(0, 0, 0)
    concave = False

    def __init__(self, C1, C2, concave):
        self.C1 = C1
        self.C2 = C2
        self.concave = concave

    def draw(self, screen, width):
        c1Fac = self.C1.depthAdjustFactor()
        c2Fac = self.C2.depthAdjustFactor()
        # Front Right
        pygame.draw.line(screen, (200, 200, 200), (self.C2.x*c1Fac, self.C1.y*c1Fac), (self.C2.x*c1Fac, self.C2.y*c1Fac), width)
        # Front Left
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c1Fac, self.C1.y*c1Fac), (self.C1.x*c1Fac, self.C2.y*c1Fac), width)
        # Front Top
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c1Fac, self.C2.y*c1Fac), (self.C2.x*c1Fac, self.C2.y*c1Fac), width)
        # Front Bottom
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c1Fac, self.C1.y*c1Fac), (self.C2.x*c1Fac, self.C1.y*c1Fac), width)

        # Back Right
        pygame.draw.line(screen, (200, 200, 200), (self.C2.x*c2Fac, self.C1.y*c2Fac), (self.C2.x*c2Fac, self.C2.y*c2Fac), width)
        # Back Left
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c2Fac, self.C1.y*c2Fac), (self.C1.x*c2Fac, self.C2.y*c2Fac), width)
        # Back Top
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c2Fac, self.C2.y*c2Fac), (self.C2.x*c2Fac, self.C2.y*c2Fac), width)
        # Back Bottom
        pygame.draw.line(screen, (200, 200, 200), (self.C1.x*c2Fac, self.C1.y*c2Fac), (self.C2.x*c2Fac, self.C1.y*c2Fac), width)
