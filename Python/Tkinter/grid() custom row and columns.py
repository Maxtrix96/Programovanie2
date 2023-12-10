import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Custom Row and Column Sizes")

# Create a label and a button
label = tk.Label(root, text="Hello, Tkinter!")
button = tk.Button(root, text="Click Me", command=on_button_click)

# Configure row 0 to have a minimum size of 50 pixels
root.rowconfigure(0, minsize=50)

# Configure column 0 to have a weight of 1 (1:1 ratio with other columns)
root.columnconfigure(0, weight=1)

# Grid the label and button
label.grid(row=0, column=0, sticky="ew")  # "ew" makes the label expand horizontally
button.grid(row=1, column=0, pady=10)  # pady adds vertical padding

root.mainloop()
