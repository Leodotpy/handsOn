import Physics.Math as m
import math
import pygame


class Ball:

    def __init__(self, radius, pos, velocity, bounds):
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.bounds = bounds


    def PhysicsTick(self, t):
        # Move with velocity
        self.pos = self.pos.add(self.velocity.multiply(t))
        # Gravity application
        self.velocity.y -= 9.8*t

        for i in range(len(self.bounds)):
            # Case for solid rectangular prism
            if not self.bounds[i].concave:

                if self.bounds[i].C1.y < self.pos.y < self.bounds[i].C2.y and self.bounds[i].C1.z < self.pos.z < self.bounds[i].C2.z:
                    # Left of sphere hits right of box
                    if self.pos.x - self.radius < self.bounds[i].C2.x < self.pos.x + self.radius:
                        self.pos.x = self.bounds[i].C2.x + self.radius
                        self.velocity.x = -self.velocity.x
                    # Right of sphere hits left of box
                    if self.pos.x + self.radius > self.bounds[i].C1.x > self.pos.x - self.radius:
                        self.pos.x = self.bounds[i].C1.x - self.radius
                        self.velocity.x = -self.velocity.x

                if self.bounds[i].C1.x < self.pos.x < self.bounds[i].C2.x and self.bounds[i].C1.z < self.pos.z < self.bounds[i].C2.z:
                    # Bottom of sphere hits top of box
                    if self.pos.y - self.radius < self.bounds[i].C2.y < self.pos.y + self.radius:
                        self.pos.y = self.bounds[i].C2.y + self.radius
                        self.velocity.y = -self.velocity.y
                    # Top of sphere hits bottom of box case
                    if self.pos.y + self.radius > self.bounds[i].C1.y > self.pos.y - self.radius:
                        self.pos.y = self.bounds[i].C1.y - self.radius
                        self.velocity.y = -self.velocity.y

                if self.bounds[i].C1.x < self.pos.x < self.bounds[i].C2.x and self.bounds[i].C1.y < self.pos.y < self.bounds[i].C2.y:
                    # Back of sphere hits front of box
                    if self.pos.z - self.radius < self.bounds[i].C2.z < self.pos.z + self.radius:
                        self.pos.z = self.bounds[i].C2.z + self.radius
                        self.velocity.z = -self.velocity.z
                    # Front of sphere hits back of box
                    if self.pos.z + self.radius > self.bounds[i].C1.z > self.pos.z - self.radius:
                        self.pos.z = self.bounds[i].C1.z - self.radius
                        self.velocity.z = -self.velocity.z


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.pos.x + (1920/2), 1080-self.pos.y - (1080/2)), self.radius)