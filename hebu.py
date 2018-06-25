import turtle
import time
from turtle import *
pen=turtle.Turtle()
window=turtle.Turtle()
color=("violet","Indigo","blue","Green","yellow","orange","red")
turtle.speed(1000000)
turtle.setup(425,425,500,100)
pen.width(3)
for i in range(4):
    for j in range(360):
        pen.color(color[i%7])
        pen.right(1)
        pen.forward(1)

    pen.right(90)
    pen.forward(50)
    
bye()
