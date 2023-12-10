import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create main window
root = tk.Tk()
root.title("Tkinter Example")

# Create widgets
label = tk.Label(root, text="Hello, Tkinter!")
button = tk.Button(root, text="Click Me", command=on_button_click)

# Organize widgets
label.pack()
button.pack()

# Start the event loop
root.mainloop()
