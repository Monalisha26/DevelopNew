import turtle
from turtle import *
import time


wn = turtle.Screen()
wn.bgcolor("blue")
tess = Turtle()
tess.shape("turtle")
tess.color("yellow")

#tess.pendown()
size = 0
for i in range(50):
   tess.stamp()             # Leave an impression on the canvas
   size = size + 3          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.left(28)           #  ...  and turn her
time.sleep(2)
turtle.bye()

#time.sleep(2)

