import tkinter as tk
from random import randint

MAX_RESOLUTION = 700

root = tk.Tk()
root.title("Zapamataj cislo!")

canvas = tk.Canvas(root, width=MAX_RESOLUTION, height=MAX_RESOLUTION)
canvas.pack()

def play_game():
    my_number = randint(10000, 100001)
    text = canvas.create_text(MAX_RESOLUTION//2, MAX_RESOLUTION//2, text=str(my_number), font=("Helvetica", 44), fill = "black", anchor="center")
    canvas.after(1000, lambda: canvas.delete(text))
    print("Ake bolo moje cislo?")
    user_answer = input("Tvoja odpoved: ")
    if user_answer == str(my_number):
        result_text = canvas.create_text(MAX_RESOLUTION//2, MAX_RESOLUTION//2, text="SUPER!", font=("Helvetica", 44), fill = "green", anchor="center")
    else:
        result_text = canvas.create_text(MAX_RESOLUTION//2, MAX_RESOLUTION//2, text=f"Nesprávne si uhádol!\nMoje čislo bolo: {my_number}", font=("Helvetica", 30), fill = "red", anchor="center")
    

play_game()

root.mainloop()