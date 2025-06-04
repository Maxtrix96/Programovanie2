import tkinter as tk

MAX_WIDTH = 1000
MAX_HEIGHT = 1000

root = tk.Tk()
root.title("odd/even numbers")

canvas = tk.Canvas(root, bg="white", height=MAX_HEIGHT, width=MAX_WIDTH)
canvas.pack()

def create_table(start, end):
    color:str = "green"
    for i in range(start, end):
        for j in range(start, end):
            x = j*30
            y = i*15
            if i*j % 2 == 0:
                color = "blue"
            else:
                color = "red"
            canvas.create_text(x, y, text=str(i*j), fill=color, font=("Calibri", 12))

create_table(1, 11)

root.mainloop()