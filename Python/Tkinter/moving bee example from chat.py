import tkinter as tk

def move_bee():
    canvas.move(bee, 5, 0)  # Update the bee's position
    root.after(50, move_bee)  # Call move_bee() again after 50 milliseconds

root = tk.Tk()
root.title("Bee Animation")

canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

bee = canvas.create_oval(50, 100, 70, 120, fill="yellow")  # Bee shape

move_bee()  # Start the animation loop

root.mainloop()
