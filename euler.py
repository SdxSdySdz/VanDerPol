from path import *
from van_der_pol import *


class Euler:
    def __init__(self, window, start, T, N):
        self.path = Path(window)
        self.h = T / N
        self.T = T
        self.N = N

        self.start = start

        self.van = VanDerPol(1, 1.2, 2)

        self.calculate()

    def calculate(self):
        y_1 = self.start.real
        y_2 = self.start.imag

        for i in range(self.N + 1):
            t = i * self.h

            y_1 = y_1 + self.h * self.van.f_1(t, y_1, y_2)
            y_2 = y_2 + self.h * self.van.f_2(t, y_1, y_2)

            self.path.append((complex(y_1, y_2)))


class Runge:
    def __init__(self, window, start, T, N):
        self.path = Path(window)
        self.h = T / N
        self.T = T
        self.N = N

        self.start = start

        self.van = VanDerPol(1, 1.2, 2)

        self.calculate()

    def calculate(self):
        y_1 = self.start.real
        y_2 = self.start.imag

        for i in range(1, self.N + 1):
            t = i * self.h

            k11 = self.h * self.van.f_1(t, y_1, y_2)
            k12 = self.h * self.van.f_2(t, y_1, y_2)

            k21 = self.h * self.van.f_1(t + self.h / 2, y_1 + k11 / 2, y_2 + k12 / 2)
            k22 = self.h * self.van.f_2(t + self.h / 2, y_1 + k11 / 2, y_2 + k12 / 2)

            k31 = self.h * self.van.f_1(t + self.h / 2, y_1 + k21 / 2, y_2 + k22 / 2)
            k32 = self.h * self.van.f_2(t + self.h / 2, y_1 + k21 / 2, y_2 + k22 / 2)

            k41 = self.h * self.van.f_1(t + self.h, y_1 + k31, y_2 + k32)
            k42 = self.h * self.van.f_2(t + self.h, y_1 + k31, y_2 + k32)

            y_1 = y_1 + (k11 + 2*k21 + 2*k31 + k41) / 6
            y_2 = y_2 + (k12 + 2*k22 + 2*k32 + k42) / 6

            self.path.append((complex(y_1, y_2)))