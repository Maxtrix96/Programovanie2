import turtle

# Set up the turtle
my_turtle = turtle.Turtle()
my_turtle.speed(2)  # Set the turtle speed

# Draw a simple turtle with legs and a mouth
my_turtle.circle(50)  # Draw the turtle's body
my_turtle.penup()
my_turtle.left(90)
my_turtle.forward(10)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.pendown()
my_turtle.circle(40)  # Draw the turtle's head

# Draw four legs
leg_length = 20
leg_width = 5
my_turtle.penup()
my_turtle.goto(0, 30)
my_turtle.pendown()
for _ in range(2):
    my_turtle.forward(leg_length)
    my_turtle.backward(leg_length)
    my_turtle.right(90)
    my_turtle.forward(leg_width)
    my_turtle.left(90)

# Draw a mouth
my_turtle.penup()
my_turtle.goto(10, 45)
my_turtle.pendown()
my_turtle.right(45)
my_turtle.circle(15, -90)

# Close the window when clicked
turtle.done()
