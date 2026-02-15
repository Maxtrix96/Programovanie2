import turtle 

kain = turtle.Turtle()
screen = turtle.Screen()
kain.shape("turtle")
kain.speed(0)

dlzka = 20

def kachlicka(dlzka:float) -> None:
    startPosition = kain.position()
    startHeading = kain.heading()
    # si v uplnom strede, tak sa pohni do laveho vrchola
    kain.penup()
    kain.left(180)
    kain.forward(dlzka)
    kain.right(90)
    kain.forward(dlzka * 2)
    kain.pendown()

    # kresli ohranicenia
    
    kain.begin_fill()
    for _ in range(4):
        kain.right(90)
        kain.forward(dlzka)
        kain.right(90)
        kain.forward(dlzka)
        kain.left(90)
        kain.forward(dlzka * 2)
    kain.end_fill()

    # vrat sa do stredu
    kain.penup()
    kain.setpos(startPosition)
    kain.setheading(startHeading)
    kain.pendown()

def podlaha(dlzka:float, pocet:int, farba1, farba2) -> None:
    # natoc sa spravne, kedze to ma byt cele otocene
    kain.left(45)
    for i in range(pocet):
        farby = (farba1, farba2)
        kain.fillcolor(farby[i % 2])
        kachlicka(dlzka)

        # pohni sa do stredu nasledujucej kachle
        kain.penup()
        kain.right(45)
        kain.forward(2 * (dlzka * (2 ** (1/2))))
        kain.left(45)

podlaha(dlzka, 7, "cyan", "yellow")

screen.mainloop()