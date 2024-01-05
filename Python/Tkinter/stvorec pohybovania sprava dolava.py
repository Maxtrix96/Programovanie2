import tkinter as tk 

MAX_LENGTH = 700
SPEED = 50 # ms

root = tk.Tk()
root.title("Pohybujúci sa stvorec sprava dolava")

canvas = tk.Canvas(root, height=MAX_LENGTH, width=MAX_LENGTH)
canvas.pack()

stvorec = canvas.create_rectangle(0, MAX_LENGTH//2, 50, MAX_LENGTH//2 + 50, fill="blue")

class WORK_PLS():
    def move_square(self):
        canvas.move(stvorec, self.distance, 0)
        self.pos_x += self.distance
        if self.pos_x == MAX_LENGTH - self.distance or self.pos_x == 0:
            self.distance *= -1
        canvas.after(SPEED, self.move_square)

    def __init__(self) -> None:
        self.distance = 50
        self.pos_x = 0
        self.moving_right = True
        #canvas.move(stvorec, self.distance, 0)

amogus = WORK_PLS()
amogus.move_square()

root.mainloop()