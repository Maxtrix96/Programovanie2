import turtle

screen=turtle.Screen()
pero=turtle.Turtle()

pero.pensize(1)
pero.color("orange")

for krok in range(40, 200, 10):
    pero.forward(krok)
    pero.forward(-krok)
    pero.right(360/32)
    

for krok in range(200, 40, -10):
    pero.forward(krok)
    pero.forward(-krok)
    pero.right(360/32)



pero.color("red")
pero.dot(50)

screen.mainloop()