import Math as m
import main.main as main


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
        self.velocity = self.velocity.Add(main.gravity)