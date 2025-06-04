import tkinter as tk 

MAX_DIMENSION = 700
SPEED = 60 # ms
LENGTH = 50

root = tk.Tk()
root.title("Pohybujúci sa stvorec sprava dolava")

canvas = tk.Canvas(root, height=MAX_DIMENSION, width=MAX_DIMENSION)
canvas.pack()

stvorec = canvas.create_rectangle(0, MAX_DIMENSION//2 - LENGTH // 2, LENGTH, MAX_DIMENSION//2 + LENGTH//2, fill="blue") # priblizne v strede obrazovky

class WORK_PLS():
    def __init__(self) -> None:
        self.distance = 50
        self.pos_x = 0

    def move_square(self):
        canvas.move(stvorec, self.distance, 0)
        self.pos_x += self.distance
        if MAX_DIMENSION - LENGTH <= self.pos_x <= MAX_DIMENSION or self.pos_x == 0:
            self.distance *= -1
        canvas.after(SPEED, self.move_square)

amogus = WORK_PLS()
amogus.move_square()

root.mainloop()