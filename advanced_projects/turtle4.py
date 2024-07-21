from turtle import Turtle,Screen

STARTING= [(0,0),(0,0),(-20,0),(-40,0)]
movement =20
UP =90
DOWN =270
RIGHT=0
LEFT=180
class snake:
    
    
    def __init__(self) -> None:
        self.segments =[]
        self.createsnake()
        self.head =self.segments[0]
        

    def createsnake(self):
        
        for position in STARTING:
            new_segment = Turtle('square')
            new_segment.color('blue')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)    

    def move(self):
            for seg in range(3,0,-1):
                xcor =self.segments[seg-1].xcor()
                ycor = self.segments[seg-1].ycor()
                self.segments[seg].goto(xcor,ycor)

            self.segments[0].forward(10)
                  
    def up(self):
         if self.head.heading() !=DOWN:
            self.head.setheading(UP)               

    def down(self):
         if self.head.heading() !=UP:
            self.segments[0].setheading(DOWN)                 

    def right(self):
         if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)                 

    def left(self):
         if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)                                