import turtle
from turtle import*
import time
tess=Turtle()
tess.color("purple")
tess.pendown()
size=0
for i in range(50):
    tess.right(30)
    size=size+5
    tess.forward(size)
    tess.right(30)
    tess.backward(size)
bye()       
