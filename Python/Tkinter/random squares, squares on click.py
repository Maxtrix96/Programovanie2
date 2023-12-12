import tkinter as tk
import random

MAX_HEIGHT = 700
MAX_WIDTH = 700

root = tk.Tk()
root.title("Random squares test")

canvas = tk.Canvas(root, width=MAX_WIDTH, height=MAX_HEIGHT, bg="white")
canvas.pack()


def get_random_hex_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return color

def set_size():
    minDimension = min(MAX_WIDTH, MAX_HEIGHT)
    size = random.randrange(0, int(minDimension / 2))
    return size

def draw_square():
    size = set_size()

    x1 = random.randrange(MAX_WIDTH - size)
    y1 = random.randrange(MAX_HEIGHT - size)
    
    x2 = x1 + size
    y2 = y1 + size

    color = get_random_hex_color()
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def draw_square_on_click(click):
    size = set_size()

    x1 = click.x
    y1 = click.y
    
    x2 = min(x1 + size, MAX_WIDTH)
    y2 = min(y1 + size, MAX_HEIGHT)

    color = get_random_hex_color()
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

canvas.bind("<Button-1>", draw_square_on_click)
canvas.bind("<KeyPress - a>", draw_square) # ????
'''
<KeyPress>: Triggered when any key on the keyboard is pressed.
<KeyRelease>: Triggered when any key on the keyboard is released.
<KeyPress-A>: Triggered when the 'A' key is pressed. Replace 'A' with the desired key.
<KeyRelease-A>: Triggered when the 'A' key is released. Replace 'A' with the desired key.
<Control-KeyPress-a>: Triggered when the 'a' key is pressed while the Control key is held down.
'''

def draw_20_squares():
    for i in range(20):
        draw_square()

button = tk.Button(root, text="Draw 20 squares", command=draw_20_squares)
button.pack()
button2 = tk.Button(root, text="Draw a square", command=draw_square)
button2.pack()

root.mainloop()