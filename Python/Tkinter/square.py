import tkinter as tk

def draw_square():
    # Coordinates of the square (x1, y1, x2, y2)
    x1, y1 = 50, 50
    x2, y2 = 150, 150

    # Draw the square on the canvas
    canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

# Create main window
root = tk.Tk()
root.title("Draw Square Example")

# Create a canvas widget
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create a button to trigger square drawing
button = tk.Button(root, text="Draw Square", command=draw_square)
button.pack()

# Start the event loop
root.mainloop()
