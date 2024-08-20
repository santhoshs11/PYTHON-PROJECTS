from turtle import Screen
from snakeobject import snake
from snakefood import Food
from snakescore import scoreboard

import time

s= Screen()
s.tracer(0)

s.setup(height =600,width =600)
s.bgcolor('black')
s.title('SNAKE GAME...')

#import snake class...from snakeobject
Snake =snake()
#import food class...from snakefood

food = Food()
score =scoreboard()
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
    if Snake.head.distance(food)< 15:
        food.refresh()
        Snake.extend()
        score.increasescore()
        

    if Snake.head.xcor() > 280 or Snake.head.xcor() < -280 or Snake.head.ycor() > 280 or Snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()  
        
    for segment in Snake.segments[1:]:
        
        if Snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over() 



s.exitonclick()