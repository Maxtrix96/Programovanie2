import tkinter as tk
import random

root = tk.Tk()
root.title("Predpoved pocasia")

canvas = tk.Canvas(root, bg="white", width=700, height=350)
canvas.pack()

global rocneObdobie
rocneObdobie = "zima"

def zvolNahodneObdobie():
    rocneObdobie = random.choice(("Jar", "Leto", "Jeseň", "Zima"))





root.mainloop()