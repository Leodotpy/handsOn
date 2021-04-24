from pingPong.constants import Constants as c
import Physics.Math as M
import math
import random

class slowPower(M.BoundRect):
    def __init__(self):
        self.delta_velocity = 100
        length = 50
        pos = (random.randint(-500+length, 500-length),random.randint(-500+length, 500-length),0)
        super().__init__(M.Vector3(pos[0]-length, pos[1]-length, 500 - length), M.Vector3(pos[0]+length, pos[1]+length, 500 + length), M.Vector3(pos[0], pos[1], pos[2]), False)

    def apply_power(self, ball):
        ball.velocity = ball.velocity.subtract(ball.velocity.normalized().multiply(self.delta_velocity))
