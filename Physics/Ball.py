import Math as m

class Ball:
    radius = 0
    pos = m.Vector3(0, 0, 0)
    velocity = m.Vector3(0, 0, 0)
    bounds = m.BoundRect(m.Vector3(0, 0, 0), m.Vector3(0, 0, 0), True)
    balls = []

    def __init__(self, radius, pos, velocity, bounds, balls):
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.bounds = bounds
        self.balls = balls