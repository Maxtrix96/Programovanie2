import tkinter as tk

root = tk.Tk()
root.title("Positioning Example")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me")
button.pack()

root.mainloop()
