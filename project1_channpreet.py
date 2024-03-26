import turtle
import random
import math

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("blue")

# Create a Turtle for drawing
pen_turtle = turtle.Turtle()
pen_turtle.speed(0)  # Set the maximum drawing speed
pen_turtle.shape("blank")

def draw_circle(t, x, y, radius, color):
    """
    Function to draw a filled circle with the given radius and color at location(x, y)
    """
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_sun_beams(t, x, y, color, outer_radius, beam_length):
    """
    #Function to draw a beam with the given color, outer_radius, beam_length at location(x, y)
    """
    t.seth(0)
    t.goto(x, y)
    t.up()
    t.color(color)
    for _ in range(12): # 12 beams
        t.forward(outer_radius - beam_length)
        t.down()
        t.forward(beam_length)
        t.up()
        t.backward(outer_radius)
        t.left(360/12)

draw_circle(pen_turtle, 140, 200, 60, "yellow")
draw_sun_beams(pen_turtle, 140, 200, "yellow", 95, 25)

def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
# Define a function to draw and fill an equalateral right
# triangle with the given hypotenuse length and color. This
# is used to create a roof shape.
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()
# Define a function to draw and fill a parallelogram, used to
# draw the side of the house
def drawParallelogram(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(30)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(120)
    t.forward(width)
    t.left(60)
    t.forward(height)
    t.left(90)
    t.end_fill()
# Draw and fill the front of the house
pen_turtle.penup()
pen_turtle.goto(-150, -120)
pen_turtle.pendown()
drawRectangle(pen_turtle, 100, 110, "blue")

# Draw and fill the front door
pen_turtle.penup()
pen_turtle.goto(-120, -120)
pen_turtle.pendown()
drawRectangle(pen_turtle, 40, 60, "lightgreen")

# Front roof
pen_turtle.penup()
pen_turtle.goto(-150, -10)
pen_turtle.pendown()
drawTriangle(pen_turtle, 100, "magenta")

# Side of the house
pen_turtle.penup()
pen_turtle.goto(-50, -120)
pen_turtle.pendown()
drawParallelogram(pen_turtle, 120, 110, "yellow")

# Window
pen_turtle.penup()
pen_turtle.goto(-15, -60)
pen_turtle.pendown()
drawParallelogram(pen_turtle, 40, 30, "brown")


# Side roof
pen_turtle.penup()
pen_turtle.goto(-50, -10)
pen_turtle.pendown()
pen_turtle.fillcolor("orange")
pen_turtle.begin_fill()
pen_turtle.left(30)
pen_turtle.forward(120)
pen_turtle.left(105)
pen_turtle.forward(100 / math.sqrt(2))
pen_turtle.left(75)
pen_turtle.forward(120)
pen_turtle.left(105)
pen_turtle.forward(100 / math.sqrt(2))
pen_turtle.left(45)
pen_turtle.end_fill()






# Function to draw rectangle 
def drawTreeRectangle(t, width, height, color): 
	t.fillcolor(color) 
	t.begin_fill() 
	t.forward(width) 
	t.left(90) 
	t.forward(height) 
	t.left(90) 
	t.forward(width) 
	t.left(90) 
	t.forward(height) 
	t.left(90) 
	t.end_fill() 

	
# Function to draw triangle	 
def drawTreeTriangle(t, length, color): 
	t.fillcolor(color) 
	t.begin_fill() 
	t.forward(length) 
	t.left(135) 
	t.forward(length / math.sqrt(2)) 
	t.left(90) 
	t.forward(length / math.sqrt(2)) 
	t.left(135) 
	t.end_fill() 




# Tree base 
pen_turtle.penup() 
pen_turtle.goto(155, -175) 
pen_turtle.pendown() 
drawTreeRectangle(pen_turtle, 20, 45, "brown") 


# Tree top 
pen_turtle.penup() 
pen_turtle.goto(115, -130) 
pen_turtle.pendown() 
drawTreeTriangle(pen_turtle, 100, "green") 

pen_turtle.penup() 
pen_turtle.goto(120, -80) 
pen_turtle.pendown() 
drawTreeTriangle(pen_turtle, 90, "green") 

pen_turtle.penup() 
pen_turtle.goto(125, -35) 
pen_turtle.pendown() 
drawTreeTriangle(pen_turtle, 80, "green")

 


# Function to draw ground rectangle
def drawGroundRectangle(t, width, height, color): 
	t.fillcolor(color) 
	t.begin_fill() 
	t.forward(width) 
	t.left(90) 
	t.forward(height) 
	t.left(90) 
	t.forward(width) 
	t.left(90) 
	t.forward(height) 
	t.left(90) 
	t.end_fill() 

pen_turtle.penup() 
pen_turtle.goto(-370, -325) 
pen_turtle.pendown() 
drawGroundRectangle(pen_turtle, 800, 150, "green") 

#cloud
pen_turtle.penup()
pen_turtle.goto(-200,200)
pen_turtle.pendown()
pen_turtle.color("white")
pen_turtle.begin_fill()
pen_turtle.circle(25)
pen_turtle.end_fill()

pen_turtle.penup()
pen_turtle.goto(-220,240)
pen_turtle.pendown()
pen_turtle.color("white")
pen_turtle.begin_fill()
pen_turtle.circle(25)
pen_turtle.end_fill()

pen_turtle.penup()
pen_turtle.goto(-240,215)
pen_turtle.pendown()
pen_turtle.color("white")
pen_turtle.begin_fill()
pen_turtle.circle(25)
pen_turtle.end_fill()

pen_turtle.penup()
pen_turtle.goto(-180,225)
pen_turtle.pendown()
pen_turtle.color("white")
pen_turtle.begin_fill()
pen_turtle.circle(25)
pen_turtle.end_fill()



#Flowers

pen_turtle.penup()
pen_turtle.goto(-280,-210)
pen_turtle.pendown()
for i in range(5):
     pen_turtle.color("orange")
     pen_turtle.begin_fill()
     pen_turtle.circle(10,180)
     pen_turtle.right(108)
     pen_turtle.end_fill()

pen_turtle.penup()
pen_turtle.goto(-200,-250)
pen_turtle.pendown()
for i in range(5):
     pen_turtle.color("red")
     pen_turtle.begin_fill()
     pen_turtle.circle(10,180)
     pen_turtle.right(108)
     pen_turtle.end_fill()


pen_turtle.penup()
pen_turtle.goto(-140,-230)
pen_turtle.pendown()
for i in range(5):
     pen_turtle.color("yellow")
     pen_turtle.begin_fill()
     pen_turtle.circle(10,180)
     pen_turtle.right(108)
     pen_turtle.end_fill()

pen_turtle.penup()
pen_turtle.goto(-70,-250)
pen_turtle.pendown()

for i in range(5):
     pen_turtle.color("pink")
     pen_turtle.begin_fill()
     pen_turtle.circle(10,180)
     pen_turtle.right(108)
     pen_turtle.end_fill()

pen_turtle.penup()
pen_turtle.goto(10,-240)
pen_turtle.pendown()

for i in range(5):
     pen_turtle.color("pink")
     pen_turtle.begin_fill()
     pen_turtle.circle(10,180)
     pen_turtle.right(108)
     pen_turtle.end_fill()


pen_turtle.penup()
pen_turtle.goto(80,-210)
pen_turtle.pendown()

for i in range(5):
     pen_turtle.color("lightblue")
     pen_turtle.begin_fill()
     pen_turtle.circle(10,180)
     pen_turtle.right(108)
     pen_turtle.end_fill()


pen_turtle.penup()
pen_turtle.goto(180,-240)
pen_turtle.pendown()

for i in range(5):
     pen_turtle.color("lightgreen")
     pen_turtle.begin_fill()
     pen_turtle.circle(10,180)
     pen_turtle.right(108)
     pen_turtle.end_fill()
    

pen_turtle.penup()
pen_turtle.goto(280,-220)
pen_turtle.pendown()

for i in range(5):
     pen_turtle.color("lightblue")
     pen_turtle.begin_fill()
     pen_turtle.circle(10,180)
     pen_turtle.right(108)
     pen_turtle.end_fill()

turtle.done()
screen.exitonclick()
