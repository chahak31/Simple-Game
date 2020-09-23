#Turtle Graphics Game
import turtle
import math
import random

#Set up screen
window = turtle.Screen()
window.bgcolor("black")
#works faster
window.tracer(2)

#Draw Border
mypen = turtle.Turtle()
mypen.penup()
mypen.color("white")
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup() #no tail
player.speed(0)

#create goals
maxGoals=6
goals=[]

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].shape("circle")
    goals[count].color("red")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300),random.randint(-300,300))

#set speed variable
speed = 1
#score variable
score = 0

#Define functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed+=1

def gobw():
    player.backward(30)

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if d<20:
        return True
    else:
        return False
    
#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(gobw, "Down")

while True:
    player.forward(speed)

    #Boundary Checking
    if player.xcor()>300 or player.xcor()<-300:
        player.right(180)

    if player.ycor()>300 or player.ycor()<-300:
        player.right(180)
        
    #move the goal
    for count in range(maxGoals): 
        goals[count].forward(3)

        #Boundary Checking
        if goals[count].xcor()>300 or goals[count].xcor()<-300:
            goals[count].right(180)

        if goals[count].ycor()>300 or goals[count].ycor()<-300:
            goals[count].right(180)

        #collision checking
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-300,300),random.randint(-300,300))
            goals[count].right(random.randint(0,360))
            score+=1
            #draw score on screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290,310)
            scorestring ="Score: "+ str(score)
            mypen.write(scorestring, False, align="left", font=("Arial",14,"normal"))

#window.exitonclick()          
