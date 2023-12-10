import tkinter as tk

root = tk.Tk()
root.title("Positioning Example")

label = tk.Label(root, text="Hello, Tkinter!")
label.grid(row=0, column=0)

button = tk.Button(root, text="Click Me")
button.grid(row=1, column=0)

root.mainloop()
