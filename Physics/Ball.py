import Math as m
import main
import pygame


class Ball:
    radius = 0
    pos = m.Vector3(0, 0, 0)
    velocity = m.Vector3(0, 0, 0)
    bounds = [m.BoundRect]

    def __init__(self, radius, pos, velocity, bounds):
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.bounds = bounds

    def PhysicsTick(self, t):
        # Move with velocity
        self.pos = self.pos.Add(self.velocity.Multiply(t))
        # Gravity application
        self.velocity = self.velocity.Add(main.gravity.Multiply(t))

        for bound in self.bounds:
            # Case for solid rectangular prism
            if not bound.concave:
                # Left of sphere hits right of box
                if self.pos.x - self.radius < bound.C2.x:
                    self.pos.x = bound.C2.x + self.radius
                    self.velocity.x = -self.velocity.x
                # Right of sphere hits left of box
                if self.pos.x + self.radius > bound.C1.x:
                    self.pos.x = bound.C1.x - self.radius
                    self.velocity.x = -self.velocity.x

                # Bottom of sphere hits top of box
                if self.pos.y - self.radius < bound.C2.y:
                    self.pos.y = bound.C2.y + self.radius
                    self.velocity.y = -self.velocity.y
                # Top of sphere hits bottom of box
                if self.pos.y + self.radius > bound.C1.y:
                    self.pos.y = bound.C1.y - self.radius
                    self.velocity.y = -self.velocity.y

                # Back of sphere hits front of box
                if self.pos.z - self.radius < bound.C2.z:
                    self.pos.z = bound.C2.z + self.radius
                    self.velocity.z = -self.velocity.z
                # Front of sphere hits back of box
                if self.pos.z + self.radius > bound.C1.z:
                    self.pos.z = bound.C1.z - self.radius
                    self.velocity.z = -self.velocity.z

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)