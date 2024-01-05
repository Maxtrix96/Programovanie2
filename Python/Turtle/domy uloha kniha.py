from turtle import *

screen = Screen()

def stvorec(d):
    for i in range(4):
        fd(d)
        rt(90)
        
def trojuh(strana):
    for i in range(3):
        fd(strana)
        lt(120)

def dom(velkost):
    stvorec(velkost)
    trojuh(velkost)
    up()
    fd(velkost/2)
    rt(90)
    fd(velkost/8)
    lt(90)
    fd(velkost/8)
    down()
    stvorec(velkost/3)
    up()
    lt(90)
    fd(velkost/8)
    rt(90)
    fd(velkost/2)
    down()

def domy9(velkost:int=30):
    for i in range(9):
        dom(velkost) 
        up()
        fd(velkost/6)
        down()

speed(0)
domy9()

screen.mainloop()