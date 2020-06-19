from math import *
from tkinter import *
from window import *
from euler import *

T = 20
N = 500
Scale = 100
Width = 1000
Height = 1000


root = Tk()

canvas = Canvas(root, width=Width, height=Height, bg="white")
canvas.create_line(0, Height / 2, Width, Height / 2, width=2,arrow=LAST)
canvas.create_line(Width / 2, 0, Width / 2, Height, width=2, arrow=FIRST)

canvas.configure(bg="#ecf0f1")

#First_x = -500

# for i in range(16000):
#     if i % 800 == 0:
#         k = First_x + (1 / 16) * i
#         canv.create_line(k + C.x, -3 + C.y, k + C.x, 3 + C.y, width = 0.5, fill = 'black')
#         canv.create_text(k + C.x + 15, -10 + C.y, text=str(k), fill="purple", font=("Helvectica", "10"))
#         if k != 0:
#             canv.create_line(-3 + 500, k + 500, 3 + 500, k + 500, width = 0.5, fill = 'black')
#             canv.create_text(20 + 500, k + 500, text=str(k), fill="purple", font=("Helvectica", "10"))

t = np.linspace(0, T, N)

x = np.cos(t) * Scale
y = np.sin(t) * Scale


if __name__ == '__main__':
    window = Window(canvas, Width, Height, Scale)
    
    euler = Euler(window, complex(0, 0), T, N)

    euler.path.draw()

    runge = Runge(window, complex(0, 0), T, N)

    runge.path.draw(fill="#0984e3")


    canvas.pack()
    root.mainloop()
