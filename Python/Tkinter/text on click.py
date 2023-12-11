import tkinter as tk

def display_text(event):
    x, y = event.x, event.y
    canvas.create_text(x, y, text="Hello, Clicked Here!", fill="black", font=("Helvetica", 12))

root = tk.Tk()
root.title("Display Text on Click")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.bind("<Button-1>", display_text)

root.mainloop()
