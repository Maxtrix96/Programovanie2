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

trojuholnik(60)
tabula.mainloop()