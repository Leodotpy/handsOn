import Physics.Math as m
#
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
        #self.velocity = self.velocity.Add(main.gravity.Multiply(t))

        for i in range(len(self.bounds)):
            # Case for solid rectangular prism
            if not self.bounds[i].concave:
                # Left of sphere hits right of box
                if self.pos.x - self.radius < self.bounds[i].C2.x:
                    self.pos.x = self.bounds[i].C2.x + self.radius
                    self.velocity.x = -self.velocity.x
                # Right of sphere hits left of box
                if self.pos.x + self.radius > self.bounds[i].C1.x:
                    self.pos.x = self.bounds[i].C1.x - self.radius
                    self.velocity.x = -self.velocity.x

                # Bottom of sphere hits top of box
                if self.pos.y - self.radius < self.bounds[i].C2.y:
                    self.pos.y = self.bounds[i].C2.y + self.radius
                    self.velocity.y = -self.velocity.y
                # Top of sphere hits bottom of box
                if self.pos.y + self.radius > self.bounds[i].C1.y:
                    self.pos.y = self.bounds[i].C1.y - self.radius
                    self.velocity.y = -self.velocity.y

                # Back of sphere hits front of box
                if self.pos.z - self.radius < self.bounds[i].C2.z:
                    self.pos.z = self.bounds[i].C2.z + self.radius
                    self.velocity.z = -self.velocity.z
                # Front of sphere hits back of box
                if self.pos.z + self.radius > self.bounds[i].C1.z:
                    self.pos.z = self.bounds[i].C1.z - self.radius
                    self.velocity.z = -self.velocity.z

