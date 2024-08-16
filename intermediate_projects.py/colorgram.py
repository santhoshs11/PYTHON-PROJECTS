from turtle import Turtle ,Screen 


t=Turtle()
s=Screen()
def function():
    t.forward(10)

s.listen()
s.onkey(function,'space')
s.exitonclick()