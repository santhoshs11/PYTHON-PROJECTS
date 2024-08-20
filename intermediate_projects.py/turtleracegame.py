from turtle import *
import random
s=Screen()
s.setup(height=600,width=600)
user=s.textinput(title="***TURTLE RACING***",prompt="which turtle will win.......")

colors =['red','yellow','blue','green','black','brown']
y_position=[-70,-40,-10,20,50,80]
allturtle =[]
is_on =False
for index in range(0,6):
    newturtle= Turtle()
    newturtle.shape('turtle')
    newturtle.color(colors[index])
    newturtle.penup()
    newturtle.goto(x=-230,y=y_position[index])
    allturtle.append(newturtle)
while not is_on:
    
    for tu in allturtle:
        if tu.xcor() > 270:
            is_on=True
            wcolor = tu.pencolor()
            if wcolor ==user:
                print(f"you are win!! {wcolor} is the winner...")
            else:
               print(f'you are lose!!..{wcolor} is the winner...')    
        
        direction = random.randint(0,10)
        tu.speed('fastest')
        tu.fd(direction)
s.exitonclick()