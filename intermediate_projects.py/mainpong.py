from turtle import Screen
from paddlepong import paddle
from pongball import ball
from pongscore import Scoreboard
import time
s=Screen()
s.setup(width=800,height=600)
s.bgcolor("black")
s.title("PONG GAME")
s.tracer(0)

r_paddle=paddle((350,0))
l_paddle=paddle((-350,0))

Ball= ball()
score =Scoreboard()

s.listen()
s.onkey(r_paddle.go_up,"Up")
s.onkey(r_paddle.go_down,"Down")
s.onkey(l_paddle.go_up,"w")
s.onkey(l_paddle.go_down,"s")


ison = True
while ison: 
    time.sleep(0.01)
    s.update() 
    Ball.move()  
    #detect collison with wall
    if Ball.ycor()>280 or Ball.ycor()<-280:
        Ball.bounce_y()

    #detect collison with paddle   
    if (Ball.distance(r_paddle)<50 and Ball.xcor() > 320) or (Ball.distance(l_paddle)<50 and Ball.xcor()<-320):
        Ball.bounce_x()
    if Ball.xcor()>380 :
        Ball.restart()
        score.l_point()
    if Ball.xcor()<-380:
        Ball.restart()
        score.r_point()    

s.exitonclick()