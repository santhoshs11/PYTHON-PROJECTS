from turtle import Turtle as t,Screen as s



def function():
    t.forward(10)

s.listen()
s.onkey(key ='space',Fun =function())
s.exitonclick()