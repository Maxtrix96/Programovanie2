import tkinter as tk
import random

MAX_WIDTH = 600
MAX_HEIGHT = 600
MAX_DEVIATION = 2

root = tk.Tk()
root.title("Random squares")

canvas = tk.Canvas(root, bg="white", height=MAX_HEIGHT, width=MAX_WIDTH)
canvas.pack()

def get_random_hex_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

def get_random_size():
    limit = min(MAX_WIDTH, MAX_HEIGHT)
    num = random.randint(1, limit // MAX_DEVIATION)
    return num

def create_square(color):
    size = get_random_size()
    x1 = random.randrange(1, MAX_WIDTH-size)
    x2 = x1 + size

    y1 = random.randrange(1, MAX_HEIGHT-size)
    y2 = y1 + size

    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def generate_random_squares(amount):
    for i in range(amount):
        create_square(get_random_hex_color())

button1 = tk.Button(root, text="Create random square", command=lambda: generate_random_squares(1))
button1.pack()
button2 = tk.Button(root, text="Create 20 random squares", command=lambda: generate_random_squares(20))
button2.pack()
button3 = tk.Button(root, text="Clear canvas", command=lambda: canvas.delete("all"))
button3.pack()

root.mainloop()