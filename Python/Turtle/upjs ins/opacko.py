import turtle as t
import random

franklin = t.Turtle()
screen = t.Screen()
franklin.speed(2)
franklin.setheading(90)

def up_arrow(stepLength:float) -> None:
    franklin.forward(stepLength)
    franklin.dot(5)
    franklin.penup()
    franklin.fd(-stepLength)
    franklin.pendown()

def down_arrow(stepLength:float) -> None:
    franklin.bk(stepLength)
    franklin.dot(5)
    franklin.penup()
    franklin.bk(-stepLength)
    franklin.pendown()

def draw_sequence(stepLength, givenSequences) -> None: 
    # zoberie dlzku a tuple s tuplami so strukturou (funkcia, pocet opakovani funkcie)
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
    for _ in range(10):
        test_sequence.append((random.choice([down_arrow, up_arrow]), random.randint(1, 7)))


    for _ in range(len(test_sequence)):
        draw_sequence(15, test_sequence)

run_test()

screen.mainloop()