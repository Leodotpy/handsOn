import Physics.Math as m
import Physics.Powers as p
import math
import pygame
from pingPong.constants import Constants as c


class Ball:

    lives = 3

    def __init__(self, radius, pos, velocity, bounds):
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.bounds = bounds

    def PhysicsTick(self, t):
        # Move with velocity
        self.pos = self.pos.add(self.velocity.multiply(t))
        # Gravity application
        self.velocity.y -= 9.8 * t

        for i in range(len(self.bounds)):
            hit = False
            # Case for solid rectangular prism
            if not self.bounds[i].concave:
                if self.bounds[i].C1.y < self.pos.y < self.bounds[i].C2.y and self.bounds[i].C1.z < self.pos.z < \
                        self.bounds[i].C2.z:
                    # Left of sphere hits right of box
                    if self.pos.x - self.radius < self.bounds[i].C2.x < self.pos.x + self.radius:
                        self.pos.x = self.bounds[i].C2.x + self.radius
                        self.velocity.x = -self.velocity.x
                        self.bounds[i].rightVal = 1
                        if i != 1:
                            hit = True
                    # Right of sphere hits left of box
                    if self.pos.x + self.radius > self.bounds[i].C1.x > self.pos.x - self.radius:
                        self.pos.x = self.bounds[i].C1.x - self.radius
                        self.velocity.x = -self.velocity.x
                        self.bounds[i].leftVal = 1
                        if i != 1:
                            hit = True

                if self.bounds[i].C1.x < self.pos.x < self.bounds[i].C2.x and self.bounds[i].C1.z < self.pos.z < \
                        self.bounds[i].C2.z:
                    # Bottom of sphere hits top of box
                    if self.pos.y - self.radius < self.bounds[i].C2.y < self.pos.y + self.radius:
                        self.pos.y = self.bounds[i].C2.y + self.radius
                        self.velocity.y = -self.velocity.y
                        self.bounds[i].topVal = 1
                        if i != 1:
                            hit = True
                    # Top of sphere hits bottom of box case
                    if self.pos.y + self.radius > self.bounds[i].C1.y > self.pos.y - self.radius:
                        self.pos.y = self.bounds[i].C1.y - self.radius
                        self.velocity.y = -self.velocity.y
                        self.bounds[i].botVal = 1
                        if i != 1:
                            hit = True

                if self.bounds[i].C1.x < self.pos.x < self.bounds[i].C2.x and self.bounds[i].C1.y < self.pos.y < \
                        self.bounds[i].C2.y:
                    # Back of sphere hits front of box
                    if self.pos.z - self.radius < self.bounds[i].C2.z < self.pos.z + self.radius:
                        self.pos.z = self.bounds[i].C2.z + self.radius
                        self.velocity.z = -self.velocity.z
                        self.bounds[i].backVal = 1
                        hit = True
                        if i == 1:
                            zVel = self.velocity.z
                            self.velocity = self.velocity.add(self.pos.subtract(self.bounds[i].pos).normalized().multiply(50))
                            self.velocity.z = zVel
                    # Front of sphere hits back of box
                    if self.pos.z + self.radius > self.bounds[i].C1.z > self.pos.z - self.radius:
                        self.pos.z = self.bounds[i].C1.z - self.radius
                        self.velocity.z = -self.velocity.z
                        self.bounds[i].frontVal = 1
                        if i != 1:
                            hit = True
            else:
                # Left of sphere hits left of box
                if self.pos.x - self.radius < self.bounds[i].C1.x:
                    self.pos.x = self.bounds[i].C1.x + self.radius
                    self.velocity.x = -self.velocity.x
                    self.bounds[i].leftVal = 1
                    hit = True
                # Right of sphere hits right of box
                if self.pos.x + self.radius > self.bounds[i].C2.x:
                    self.pos.x = self.bounds[i].C2.x - self.radius
                    self.velocity.x = -self.velocity.x
                    self.bounds[i].rightVal = 1
                    hit = True

                # Bottom of sphere hits bottom of box
                if self.pos.y - self.radius < self.bounds[i].C1.y:
                    self.pos.y = self.bounds[i].C1.y + self.radius
                    self.velocity.y = -self.velocity.y
                    self.bounds[i].botVal = 1
                    hit = True
                # Top of sphere hits top of box
                if self.pos.y + self.radius > self.bounds[i].C2.y:
                    self.pos.y = self.bounds[i].C2.y - self.radius
                    self.velocity.y = -self.velocity.y
                    self.bounds[i].topVal = 1
                    hit = True

                # Back of sphere hits back of box
                if self.pos.z - self.radius < self.bounds[i].C1.z:
                    self.pos.z = self.bounds[i].C1.z + self.radius
                    self.velocity.z = -self.velocity.z
                    self.bounds[i].frontVal = 1
                    hit = True
                    if i == 0:
                        self.lives -= 1
                # Front of sphere hits front of box
                if self.pos.z + self.radius > self.bounds[i].C2.z:
                    self.pos.z = self.bounds[i].C2.z - self.radius
                    self.velocity.z = -self.velocity.z
                    self.bounds[i].backVal = 1
                    hit = True
            if i == 1:
                if hit:
                    c.score += 1
                    self.velocity = self.velocity.add(self.velocity.normalized().multiply(20))
                    if c.score % 10 == 0 and len(self.bounds) != 4:
                        self.bounds.append(p.slowPower())
            if i == 3:
                if hit:
                    self.bounds[3].apply_power(self)
                    self.bounds.pop(3)

    def draw(self, screen):
        if self.pos.z == 0:
            self.pos.z = 1
        factor = self.pos.depthAdjustFactor()
        pygame.draw.circle(screen, (255*factor, 255*factor, 255*factor), (self.pos.x*factor + (1920 / 2), 1080 - self.pos.y*factor - (1080 / 2)),
                           self.radius * factor)

    def drawRed(self, screen):
        if self.pos.z == 0:
            self.pos.z = 1
        factor = self.pos.depthAdjustFactor()
        pygame.draw.circle(screen, (255, 0, 0), (self.pos.x*factor + (1920 / 2), 1080 - self.pos.y*factor - (1080 / 2)),
                           self.radius * factor)
