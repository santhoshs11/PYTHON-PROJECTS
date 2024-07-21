from turtle import Turtle,Screen
from turtle4 import snake
import time

s= Screen()
s.tracer(0)

s.setup(height =600,width =600)
s.bgcolor('black')
s.title('SNAKE GAME...')
t=Turtle('square')
Snake =snake()
s.listen()
s.onkey(Snake.up, "Up")
s.onkey(Snake.down, "Down")
s.onkey(Snake.left, "Left")
s.onkey(Snake.right, "Right")


ison = True
while ison:
    s.update()
    time.sleep(0.1)
    Snake.move()
    
    


s.exitonclick()