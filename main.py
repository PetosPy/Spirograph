import turtle as t
from turtle import Screen
import random

pet = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


pet.speed("fastest")
pet.pensize(3)
def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        pet.pencolor(random_color())
        pet.circle(100)
        pet.setheading(pet.heading() + size_of_gap)


spirograph(5)











screen = Screen()
screen.exitonclick()