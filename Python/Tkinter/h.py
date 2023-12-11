import tkinter as tk

def display_text(event):
    x, y = event.x, event.y
    canvas.create_text(x, y, text="Hello, Clicked Here!", fill="black", font=("Helvetica", 12))

root = tk.Tk()
root.title("Display Text on Click")

# Increase canvas size to include the border
canvas = tk.Canvas(root, width=402, height=302, bg="white", borderwidth=2, highlightthickness=0)
canvas.pack()

# Bind the click event to the display_text function
canvas.bind("<Button-1>", display_text)

root.mainloop()