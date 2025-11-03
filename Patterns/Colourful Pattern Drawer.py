import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')
colours = ['red','yellow','blue','green','purple','orange']

for i in range(100):
    t.pencolor(random.choice(colours))
    t.width(2)
    t.forward(i*4)
    t.right(121)
    for j in range(3):
        t.forward(i)
        t.left(60)

t.hideturtle()
turtle.done()