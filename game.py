#Turtle Graphics Game
import turtle
import math
import random

#Set up screen
window = turtle.Screen()
window.bgcolor("lightgreen")

#Draw Border
mypen = turtle.Turtle()
mypen.penup()
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

#create goal
goal = turtle.Turtle()
goal.shape("circle")
goal.color("red")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-300,300),random.randint(-300,300))

#set speed variable
speed = 1

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

    #collision checking
    if isCollision(player, goal):
        goal.setposition(random.randint(-300,300),random.randint(-300,300))
        goal.right(random.randint(0,360))
        
    #move the goal
    goal.forward(3)

    #Boundary Checking
    if goal.xcor()>300 or goal.xcor()<-300:
        goal.right(180)

    if goal.ycor()>300 or goal.ycor()<-300:
        goal.right(180)
