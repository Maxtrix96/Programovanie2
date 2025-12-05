import turtle as t
import random

ferdinand = t.Turtle()
obrazovka = t.Screen()
ferdinand.shape("turtle")
ferdinand.speed(0)

dlzkaKroku = 40
ferdinand.penup()

def nahodnaFarba():
    r = random.randint(50, 200)
    g = random.randint(50, 200)
    b = random.randint(50, 200)
    color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return color

def stvorec(dlzka):
    # si otocena doprava
    # rob v D > C > B > A
    ferdinand.fillcolor(nahodnaFarba())
    ferdinand.begin_fill()
    for i in range(4):
        ferdinand.forward(dlzka)
        ferdinand.right(90)
    ferdinand.end_fill()

def dlazdica1():
    stvorec(dlzkaKroku)
    ferdinand.forward(dlzkaKroku / 8)
    ferdinand.right(90)
    ferdinand.forward(dlzkaKroku / 8)
    ferdinand.left(90)
    stvorec(dlzkaKroku * 3 / 4)
    ferdinand.left(90)
    ferdinand.forward(dlzkaKroku / 8)
    ferdinand.left(90)
    ferdinand.forward(dlzkaKroku / 8)
    ferdinand.right(180)

def dlazdica2():
    stvorec(dlzkaKroku)
    ferdinand.forward(dlzkaKroku / 2)
    ferdinand.right(90)
    ferdinand.forward(dlzkaKroku / 2)
    ferdinand.dot(dlzkaKroku, nahodnaFarba())
    ferdinand.left(180)
    ferdinand.forward(dlzkaKroku / 2)
    ferdinand.left(90)
    ferdinand.forward(dlzkaKroku / 2)
    ferdinand.right(180)

def mozaika(dlzka):
    ferdinand.setposition(-5 * dlzka, 5 * dlzka)
    for i in range(10):
        for j in range(10):
            random.choice((dlazdica1, dlazdica2))()
            ferdinand.forward(dlzka)
        ferdinand.backward(dlzka * 10)
        ferdinand.right(90)
        ferdinand.forward(dlzka)
        ferdinand.left(90)

mozaika(dlzkaKroku)
obrazovka.mainloop()


