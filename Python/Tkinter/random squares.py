import tkinter as tk
import random

MAX_HEIGHT = 700
MAX_WIDTH = 700

def get_random_color():
    color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    return color

def draw_square():
    size = random.randrange(0, int(MAX_HEIGHT/5))

    x1 = random.randrange(MAX_HEIGHT - size)
    y1 = random.randrange(MAX_HEIGHT - size)
    
    x2 = min(x1 + size, MAX_HEIGHT)
    y2 = min(y1 + size, MAX_HEIGHT)

    color = get_random_color()
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def draw_square_on_click(click):
    size = random.randrange(0, int(MAX_HEIGHT/5))

    x1 = click.x
    y1 = click.y
    
    x2 = min(x1 + size, MAX_HEIGHT)
    y2 = min(y1 + size, MAX_HEIGHT)

    color = get_random_color()
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

root = tk.Tk()
root.title("Random squares test")

canvas = tk.Canvas(root, width=MAX_WIDTH, height=MAX_HEIGHT)
canvas.pack()

canvas.bind("<Button-1>", draw_square_on_click)

button = tk.Button(root, text="Draw Square", command=draw_square)
button.pack()

root.mainloop()