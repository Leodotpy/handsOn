from pingPong.constants import Constants as c
import Physics.Math as m
import math
import random

class slowPower(m.BoundRect):
    def __init__(self):
        length = 50
        pos = (random.randint(-500+length, 500-length),random.randint(-500+length, 500-length),0)
        super().__init__(M.Vector3(pos[0]-length, pos[1]-length, -length), M.Vector3(pos[0]+length, pos[1]+length, length), M.Vector3(pos[0], pos[1], pos[2]), False)


