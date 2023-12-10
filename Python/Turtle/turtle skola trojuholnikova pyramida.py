# pyramida.py
import turtle
pero = turtle.Turtle()
pero.width(3)
tabula = turtle.Screen()
def trojuholnik(dlzka):
#'''Nakreslí trojuholník so zadanou dĺžkou strany
#:param dlzka: dĺžka strany
#:type dlzka: int|float
#'''
    for i in range(3):
        pero.forward(dlzka)
        pero.left(120)

def rad_trojuholnikov(pocet, dlzka):
#'''Nakreslí rad trojuholnikov. V rade je pocet trojuholníkov
#s dĺžkou strany dlzka.
#:param pocet: počet trojuholníkov
#:type pocet: int
#:param dlzka: dĺžka strany trojuholníka
#:type dlzka: int|float
#'''
    for i in range(pocet):
        trojuholnik(dlzka)
        pero.forward(dlzka)
    pero.forward(-dlzka * pocet)

def pyramida(pocet, dlzka):
#'''Nakreslí pyramídu z trojuholníkov. V spodnom rade pyramídy
#je pocet trojuholníkov. Dĺžka strany trojuholníka je dlzka.
#:param pocet: počet trojuholníkov v spodnom rade
#:type pocet: int
#:param dlzka: dĺžka strany trojuholníka
#:type dlzka: int|float
#'''

    for i in range(pocet, 0, -1):
        rad_trojuholnikov(i, dlzka)
        pero.left(60)
        pero.forward(dlzka)
        pero.right(60)


pyramida(5, 30)
tabula.mainloop()