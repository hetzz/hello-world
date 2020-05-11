import turtle
from turtle import *
from random import randint 

b = turtle.Screen()
d = turtle.Turtle()
d.speed(0)

b.bgcolor('black')

x = 1

while x < 400:

    r = randint(0,255) 
    g = randint(0,255)
    b = randint(0,255) 

    colormode(255)


    d.pencolor(r,g,b) 
    d.fd(60 + x)
    d.rt(120.8) # Change the degree for different shapes


    x = x+1 

b.exitonclick() 