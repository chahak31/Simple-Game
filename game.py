import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup() #no tail
player.speed(0)

speed = 1

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def gofw():
    player.forward(30)

def gobw():
    player.backward(30)
    
#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(gofw, "Up")
turtle.onkey(gobw, "Down")



while True:
    player.forward(speed)
