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
    pero.penup()
    pero.right(90)
    pero.forward(dlzka * (6/10))
    pero.pendown()
    pero.left(90)

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
    pero.penup()
    pero.forward(dlzka * (12/10))
    pero.pendown()
    pero.left(90)

def riadok_hor(dlzka, sirka):
    for i in range(sirka):
        stvorec_hor(dlzka)
        stvorec_vert(dlzka)
    pero.penup()
    pero.left(90)
    pero.forward(dlzka * (48/10))
    pero.right(90)

def riadok_vert(dlzka, sirka):
    for i in range(sirka):
        stvorec_vert(dlzka)
        stvorec_hor(dlzka)
    pero.penup()
    pero.left(90)
    pero.forward(dlzka * (48/10))
    pero.right(90)

def vytvor_stlpce(dlzka, sirka, vyska):
    for i in range(vyska):
        riadok_hor(dlzka, sirka)
        pero.penup()
        pero.right(180)
        pero.forward(dlzka * (12/10))
        pero.left(180)
        pero.pendown()
        riadok_vert(dlzka, sirka)
        pero.penup()
        pero.right(180)
        pero.forward(dlzka * (12/10))
        pero.left(180)
        pero.pendown()

    
vytvor_stlpce(60, 2, 2)

tabula.mainloop()