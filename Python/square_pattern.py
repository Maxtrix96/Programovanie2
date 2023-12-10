import turtle

pero = turtle.Turtle()
pero.pensize(5)
tabula = turtle.Screen()
pero.color("black")

pero.left(90)

def stvorec(dlzka):
    pero.fillcolor("black")
    pero.begin_fill()
    for i in range(2):
        pero.forward(dlzka)
        pero.right(90)
        pero.forward(dlzka * (4/10))
        pero.right(90)
    pero.end_fill()

def dvojica(dlzka):
    stvorec(dlzka)
    pero.penup()
    pero.forward(dlzka)
    pero.right(90)
    pero.forward(dlzka * (10/10))
    pero.pendown()
    pero.right(90)
    stvorec(dlzka)
    pero.left(90)
    pero.penup()
    pero.forward(dlzka * (2/10))
    pero.pendown()

def obratena_dvojica(dlzka):
    pero.right(90)
    stvorec(dlzka)
    pero.left(90)
    pero.penup()
    pero.forward(dlzka * (6/10))
    pero.pendown()
    pero.right(90)
    stvorec(dlzka)


def dvojica_dvojice(dlzka):
    for i in range(2):
        dvojica(dlzka)
    pero.left(180)
    pero.penup()
    pero.forward(dlzka * (2/10))
    pero.right(90)
    pero.forward(dlzka * (2/10))
    pero.pendown()
    pero.left(90)

def riadok(dlzka, stvorice_riadok):
    for i in range(stvorice_riadok):
        dvojica_dvojice(dlzka)
    
def stlpce(dlzka, stvorice_riadok, stlpcov):
    for i in range (stlpcov / 2): #treba novu funkciu, ktora urobi riadok ale inaok obratenu
        riadok(dlzka, stvorice_riadok)
        pero.left(90)
        pero.penup()
        pero.forward(dlzka * (48/10))
        pero.left(90)
        pero.forward(dlzka * (12/10))
        pero.left(180)
        pero.pendown()


obratena_dvojica(60)

tabula.mainloop()
