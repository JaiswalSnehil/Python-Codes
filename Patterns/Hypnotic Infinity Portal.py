import turtle, math

t = turtle.Turtle()
t.speed()
screen = turtle.Screen()
screen.bgcolor('black')
t.color('cyan')

for i in range(300):
    t.forward(i/2)
    t.left(59)
    t.width(1 + i%3)

turtle.done()