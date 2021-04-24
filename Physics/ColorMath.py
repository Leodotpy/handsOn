class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def interpColors(self, col2, t):
        return Color(self.r * t + col2.r * (1 - t), self.g * t + col2.g * (1 - t), self.b * t + col2.b * (1 - t))
