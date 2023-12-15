import tkinter as tk

def process_input():
    user_input = sussous.get()
    # Do something with user_input, for example, print it
    print("User input:", user_input)

root = tk.Tk()
root.title("Text Entry Example")

# Create an Entry widget
sussous = tk.Entry(root, width=30)
sussous.pack(pady=10, padx=10)

# Create a button to process the input
button = tk.Button(root, text="Process Input", command=process_input)
button.pack()

root.mainloop()
