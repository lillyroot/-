from random import *
from tkinter import *

size = 311
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
x = randint(0, size)
y = randint(0, size)
d = randint(0, size // 5)
canvas.create_oval(x, y, x+d, y+d, fill='#ffff00')
root.update()