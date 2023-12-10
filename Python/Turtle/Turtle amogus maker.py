import turtle

pero = turtle.Turtle()
tabula = turtle.Screen()
pero.color("black")

pero.pensize(5)
pero.left(90)

def obdlznik(dlzka):
    pero.fillcolor("black")
    pero.begin_fill()
    for i in range(2):
        pero.forward(dlzka)
        pero.right(90)
        pero.forward(dlzka * (4/10))
        pero.right(90)
    pero.end_fill()

def stvorec_hor(dlzka):
    obdlznik(dlzka)
    pero.right(90)
    pero.penup()
    pero.forward(dlzka * (6/10))
    pero.pendown()
    pero.left(90)
    obdlznik(dlzka)

def stvorec_vert(dlzka):
    pero.penup()
    pero.forward(dlzka)
    pero.right(90)
    pero.pendown()
    obdlznik(dlzka)
    pero.right(90)
    pero.penup()
    pero.forward(dlzka * (6/10))
    pero.pendown()
    pero.left(90)
    obdlznik(dlzka)
    pero.right(90)
    pero.forward(dlzka * (4/10))
    pero.left(90)

def riadok_hor(dlzka, pocet):
    for i in range(pocet):
        stvorec_hor(dlzka)
        stvorec_vert(dlzka)
    pero.penup
    pero.forward(30)
    pero.left(90)
    pero.forward(30)



    

riadok_hor(60, 2)

tabula.mainloop()