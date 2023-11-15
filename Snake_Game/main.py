import turtle
import time
import random

waitTime = 0.1

#######################################################################
# Screen definition
wn = turtle.Screen()
def screenDefinition():
    wn.title("Snake!")
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.tracer(0)


#######################################################################
# Black mamba head
head = turtle.Turtle()
def blackMambaInitialization():
    head.speed(0)
    head.shape("square")
    head.penup()
    head.goto(0,0)
    head.color("white")
    head.direction = "stop"
def createNewPointTail():
    tailPoint = turtle.Turtle()
    tailPoint.speed(0)
    tailPoint.shape("square")
    tailPoint.penup()
    tailPoint.color("grey")
    return tailPoint


#######################################################################
# Apple
apple = turtle.Turtle()
def appleCreation():
    apple.speed(0)
    apple.shape("circle")
    apple.penup()
    apple.goto(0,100)
    apple.color("red")

#######################################################################
# Snake tail 
tail = []

#######################################################################
# Text Score
score = turtle.Turtle()
actualscore = 0
highscore = 0
def createScore():
    score.speed(0)
    score.penup()
    score.hideturtle()
    score.color("white")
    score.goto(0,260)
    score.write("Score: {}   High Score: {}".format(actualscore, highscore), align="center", font=("Courier", 24, "normal"))
    
#######################################################################
# Movement control
def up():
    head.direction = "up"
def down():
    head.direction = "down"
def left():
    head.direction = "left"
def right():
    head.direction = "right"

def movement():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def listeningForKey():
    wn.listen()
    wn.onkeypress(up, "Up")
    wn.onkeypress(down, "Down")
    wn.onkeypress(left, "Left")
    wn.onkeypress(right, "Right")

#######################################################################
# Colision Snake with apple
def checkColision():
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x,y)
        tail.append(createNewPointTail())
        return True
    return False

        
#######################################################################
# Move Tail
def moveTail():
    total = len(tail)
    for index in range(total -1, 0, -1):
        x = tail[index-1].xcor()
        y = tail[index-1].ycor()
        tail[index].goto(x, y)
    
    if total > 0:
        x = head.xcor()
        y = head.ycor()
        tail[0].goto(x,y)


#######################################################################
# Check Collision With Screen 
def checkCollisionWithScreen():
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for element in tail:
            element.goto(1000,1000)
        tail.clear()
        return True
    return False
        
#######################################################################
# Check Collision With Tail

def checkCollisionWithTail():
    for element in tail:
        if element.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for element in tail:
                element.goto(1000,1000)
            tail.clear()
            return True
    return False
        

#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
# Game 
screenDefinition()
createScore()
blackMambaInitialization()
appleCreation()
listeningForKey()

while True:
    wn.update()
    #update score
    score.clear()
    score.write("Score: {}   High Score: {}".format(actualscore, highscore), align="center", font=("Courier", 24, "normal"))
    #snake movement
    moveTail()
    movement()
    #collisions and updates
    if checkCollisionWithScreen() or checkCollisionWithTail():
        actualscore = 0
    #update score and check apple
    if checkColision():
        actualscore += 10
        if actualscore > highscore:
            highscore = actualscore
    time.sleep(waitTime)


