from math import *


class VanDerPol:
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

    def f_1(self, t, y_1, y_2):
        return y_2

    def f_2(self, t, y_1, y_2):
        return self.a * (1 - y_1 * y_1) * y_2 - y_1 + self.b * cos(self.w * t)
