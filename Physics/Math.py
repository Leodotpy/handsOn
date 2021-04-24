import math


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


class BoundRect:
    C1, C2 = Vector3(0, 0, 0), Vector3(0, 0, 0)
    concave = False

    def __init__(self, C1, C2, concave):
        self.C1 = C1
        self.C2 = C2
        self.concave = concave
