from turtle import Turtle
alignment ="center"
Font=("courier,25,normal")
class scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.updatescore()
        
    def updatescore(self):
        self.write(f"Score :{self.score}",align=alignment,font=Font)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("|___GAME OVER___|", align=alignment, font=Font)

    def increasescore(self):
        self.score+=1
        self.clear()
        self.updatescore()    

    