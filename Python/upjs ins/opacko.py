import turtle as t
import random

franklin = t.Turtle()
screen = t.Screen()
franklin.speed(10)
franklin.setheading(90)

def up_arrow(stepLength:float) -> None:
    franklin.forward(stepLength)
    franklin.dot(5)
    franklin.penup()
    franklin.fd(-stepLength)
    franklin.pendown()

def down_arrow(stepLength:float) -> None:
    franklin.dot(5)
    franklin.fd(stepLength)
    franklin.fd(-stepLength)

def draw_sequence(stepLength:int, givenSequences:tuple) -> None: 
    # zoberie dlzku kroku a zoznam postupnosti, t. j. zoznam aku funkciu ma vykonat a kolko krat
    for sequence in givenSequences:
        for _ in range(sequence[1]):
            sequence[0](stepLength)
            # teraz sa pohni doprava a priprav na dalsie
            franklin.penup()
            franklin.right(90)
            franklin.forward(7)
            franklin.right(-90)
            franklin.pendown()

test_sequence = []

def run_test():
    for _ in range(3):
        test_sequence.append((random.choice([down_arrow, up_arrow]), random.randint(2, 5)))


    for _ in range(len(test_sequence)):
        draw_sequence(15, tuple(test_sequence))

#run_test()

draw_sequence(15, ((up_arrow, 3), (down_arrow, 2), (up_arrow, 6)))


print("finished")

screen.mainloop()