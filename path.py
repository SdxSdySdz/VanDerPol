import numpy as np


class Path:
    def __init__(self, window):
        self.vertexes = []
        self.window = window

    def append(self, z):
        self.vertexes.append(z.conjugate())

    def draw(self, fill="#ff7675"):
        for i in range(len(self.vertexes) - 1):
            self.window.canvas.create_line(self.vertexes[i].real * self.window.scale + self.window.width / 2,
                                    self.vertexes[i].imag * self.window.scale + self.window.height / 2,
                                    self.vertexes[i + 1].real * self.window.scale + self.window.width / 2,
                                    self.vertexes[i + 1].imag * self.window.scale + self.window.height / 2,
                                    width=1,
                                    fill=fill)