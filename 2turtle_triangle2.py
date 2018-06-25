#import the module
from turtle import *

wn = Screen()

#adding background color
wn.bgcolor("light blue")

#setting background image
#wn.setup(500,500)
#wn.bgpic("im1.gif")

#setting title
wn.title("Drawing Triangle")

#marker for drawing
pen = Turtle()

#changing pen color
pen.color("red")

#changing pen width
pen.width(4)

#setting pen speed
pen.speed(1)

#some other methods 
#pen.up()
#pen.goto(-100,0)
#pen.down()

#Drawing an euilateral triangle
for i in range(3):
    pen.forward(100) #move marker forward
    pen.left(120)    #tilt it to 120 degree

#shut the turtle graphics screen
bye()
