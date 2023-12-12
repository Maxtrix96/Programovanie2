import tkinter as tk
import random

MAX_WIDTH, MAX_HEIGHT = 600, 600

root = tk.Tk()
root.title("Make 20 random squares")

canvas = tk.Canvas(root, bg="white", width=MAX_WIDTH, height=MAX_HEIGHT)
canvas.pack()

def get_random_hex_color():
    randomColor = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return randomColor

def set_size():
    minSize = min(MAX_WIDTH, MAX_HEIGHT)
    size = random.randint(0, int(minSize / 2))
    return size

def draw_square():
    size = set_size()

    x1 = random.randint(0, MAX_WIDTH - size)
    y1 = random.randint(0, MAX_HEIGHT - size)

    x2 = x1 + size
    y2 = y1 + size

    color = get_random_hex_color()
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def draw_square_on_click(clickLocation):
    size = set_size()

    x1 = clickLocation.x
    y1 = clickLocation.y

    x2 = x1 + size
    y2 = y1 + size

    color = get_random_hex_color()
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def write_on_click(clickLocation):
    x, y = clickLocation.x, clickLocation.y
    canvas.create_text(x, y, text="Hi there!", fill=get_random_hex_color(), font=("Calibri", 12))

def draw_20_random_squares():
    for i in range(20):
        draw_square()

button1 = tk.Button(root, text="Draw 20 random squares.", command=draw_20_random_squares)
button1.pack()
button2 = tk.Button(root, text="Draw a random square.", command=draw_square)
button2.pack()

canvas.bind("<Button-1>", draw_square_on_click)
canvas.bind("<Button-3>", write_on_click)

root.mainloop()