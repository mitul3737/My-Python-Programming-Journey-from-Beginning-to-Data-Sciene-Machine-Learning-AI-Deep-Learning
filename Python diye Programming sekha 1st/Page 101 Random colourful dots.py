import turtle
import random

colors = ["red", "green", "blue", "yellow", "orange", "black", "purple"]

turtle.penup()

for i in range(50):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    turtle.setposition(x, y)
    i = random.randint(0, len(colors) - 1)
    turtle.dot(colors[i])  # setting colors

turtle.done