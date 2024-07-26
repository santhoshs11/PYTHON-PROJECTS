import turtle as t
from turtle import Screen
import random
tim = t.Turtle()

def side(num_sides):
    for i in range(num_sides):
        degree = 360/num_sides
        colors =['red','blue','green','brown','yellow',]
        rc = random.choice(colors)
        t.pencolor(rc)
        t.forward(33)
        t.pu()
        t.forward(33)
        t.pd()
        t.forward(33)
        t.lt(degree)

for l in range(3,11):
    t.speed('fastest')
    a= side(l)
    t.clearscreen()

def sid(num_sides):
    for i in range(num_sides):
        degree = 360/num_sides
        colors =['red','blue','green','brown','yellow',]
        rc = random.choice(colors)
        t.pencolor(rc)
        t.forward(33)
        t.pu()
        t.forward(33)
        t.pd()
        t.forward(30)
        t.rt(degree)
for m in range(3,11):
    t.speed("fastest")
    b= sid(m)
    
sc = Screen()
sc.exitonclick()