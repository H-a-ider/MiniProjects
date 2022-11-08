from turtle import *

setup(500, 500)
 # Set Brush
speed(10)
bgcolor("pink")
shape("turtle")
colormode(255)

def drawRound(size, filled):
    pendown()
    if filled==True:
        begin_fill()
    setheading(180)
    circle(size, 360)
    if filled==True:
        end_fill()

def drawRect(length, width, filled):
    setheading(0)
    pendown()
    if filled==True:
        begin_fill()
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    if filled==True:
        end_fill() 

# Head
def head():
    color("blue", "blue")
    penup()
    goto(0, 100)
    drawRound(75, True)

    color("white", "white")
    penup()
    goto(0, 72)
    drawRound(60, True)

def eyes():
# Left Eye Socket
    color("black", "white")
    penup()
    goto(-15, 80)
    drawRound(17, True)

# Right Eye Socket
    color("black", "white")
    penup()
    goto(19, 80)
    drawRound(17, True)

    color("black", "black")
    penup()
    goto(-8, 70)
    drawRound(6, True)
    color("white", "white")
    penup()
    goto(-8, 66)
    drawRound(2, True)

# Right Eyeball
    color("black", "black")
    penup()
    goto(12, 70)
    drawRound(6, True)
    color("white", "white")
    penup()
    goto(12, 66)
    drawRound(2, True)

# Nose
def nose():
    color("red", "red")
    penup()
    goto(0, 40)
    drawRound(7, True)

# Mouth
def mouth():
    color("black", "black")
    penup()
    goto(-30, -20)
    pendown()
    setheading(-27)
    circle(70, 55)

    penup()
    goto(0, 26)
    pendown()
    goto(0, -25)

def whiskers():
    color("black", "black")
    # The beard in the middle of the left
    penup()
    goto(10, 5)
    pendown()
    goto(-40, 5)

    # The beard in the middle of the right
    penup()
    goto(10, 5)
    pendown()
    goto(40, 5)

    # Left Upper Beard
    penup()
    goto(-10, 15)
    pendown()
    goto(-40, 20)
    
    # The Beard on the upper Right
    penup()
    goto(10, 15)
    pendown()
    goto(40, 20)

    # Left Beard
    penup()
    goto(-10, -15)
    pendown()
    goto(-40, -10)

    # Beard on the Lower Right
    penup()
    goto(10, -5)
    pendown()
    goto(40, -10)

def body():
    # Blue Body
    color("blue", "blue")
    penup()
    goto(-50, -40)
    drawRect(100, 80, True)

    # White Belly
    color("white", "white")
    penup()
    goto(0, -30)
    drawRound(40, True)

    # Red Ribbon
    color("red", "red")
    penup()
    goto(-60, -35)
    drawRect(120, 10, True)

    # White Legs
    color("white", "white")
    penup()
    goto(15, -127)
    pendown()
    setheading(90)
    begin_fill()
    circle(14, 180)
    end_fill()

def feet():
    # Left Foot
    color("black", "white")
    penup()
    goto(-30, -110)
    drawRound(20, True)

    # Right Foot
    color("black", "white")
    penup()
    goto(30, -110)
    drawRound(20, True)

def arms():
    # Left Arm
    color("blue", "blue")
    penup()
    begin_fill()
    goto(-51, -50)
    pendown()
    goto(-51, -75)
    left(70)
    goto(-76, -85)
    left(70)
    goto(-86, -70)
    left(70)
    goto(-51, -50)
    end_fill()

    # Right Arm
    color("blue", "blue")
    penup()
    begin_fill()
    goto(49, -50)
    pendown()
    goto(49, -75)
    left(70)
    goto(74, -85)
    left(70)
    goto(84, -70)
    left(70)
    goto(49, -50)
    end_fill()

def hands():
    # Left Hand
    color("black", "white")
    penup()
    goto(-90, -71)
    drawRound(15, True)

    # Right Hand
    color("black", "white")
    penup()
    goto(90, -71)
    drawRound(15, True)

def bell():
    # Yellow solid circle indicates copper bell
    color("yellow", "yellow")
    penup()
    goto(0, -41)
    drawRound(8, True)

    # Black Rectangle indicates pattern
    color("black", "black")
    penup()
    goto(-10, -47)
    drawRect(20, 4, False)

    # The black Solid Circle indicates the impacted metal pill
    color("black", "black")
    penup()
    goto(0, -53)
    drawRound(2, True)

def package():
    # Semi Circle
    color("black", "black")
    penup()
    goto(-25, -70)
    pendown()
    setheading(-90)
    circle(25, 180)
    goto(-25, -70)
    hideturtle()

head()
eyes()
nose()
mouth()
whiskers()
body()
feet()
arms()
hands()
bell()
package()