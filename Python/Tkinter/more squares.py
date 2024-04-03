import tkinter as tk
import random

MAX_dimension = 600
MIN_SIZE = 30
MAX_DEVIATION = 4

root = tk.Tk()
root.title("random squares yet again")

canvas = tk.Canvas(root, width=MAX_dimension, height=MAX_dimension, background="white")
canvas.pack()

def get_random_size(MAX_SIZE = MAX_dimension) -> int:
    limit = MAX_SIZE # smallest window dimension, if there are two different dimensions -> use min()
    size = random.randint(MIN_SIZE, limit // MAX_DEVIATION)
    return size

def get_random_color() -> str:
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

def generate_square() -> None:
    size = get_random_size()
    x1, y1 = random.randint(0, MAX_dimension-size), random.randint(0, MAX_dimension-size)  
    x2, y2 = x1 + size, y1 + size  
    canvas.create_rectangle(x1, y1, x2, y2, fill=get_random_color())

def generate_multiple_squares(x:int) -> None:
    for _ in range(x):
        generate_square()


root.mainloop()