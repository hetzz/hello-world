import random
import turtle
import time
a = turtle.Screen()
a.title('design')
a.bgcolor("black")
a.setup(width=700, height=700)
b = turtle.Turtle()
b.color('white')
b.pensize(5)
b.speed(6)
def hexagon():
    for _ in range(6):
        b.fd(100)
        b.lt(60)

def octagon():
    for _ in range(8):
        b.fd(50)
        b.lt(45)
def decagon():
    for _ in range(10):
        b.fd(50)
        b.lt(36)
def triangle():
    for _ in range(3):
        b.fd(150)
        b.lt(120)
def square():
    for _ in range(4):
        b.fd(150)
        b.lt(90)
def design_hexagon():
    b.pu()
    b.goto(0, 150 )
    b.pd()
    for _ in range(18):
            hexagon()
            b.fd(20)
            b.rt(20)

def design_octagon():
    b.pu()
    b.goto(0, 150 )
    b.pd()
    for _ in range(18):
            octagon()
            b.fd(20)
            b.rt(20)

def design_decagon():
    b.pu()
    b.goto(0, 150 )
    b.pd()
    for _ in range(18):
            decagon()
            b.fd(20)
            b.rt(20)

def design_circle():

    print('best 1 is 20,60' )
    x = int(input('Note:  (no. should be between 10 and 27) and (27 is smallest and 10 is the biggest)\nEnter the size of the inner ring:  '))
    y = int(input('Note:  (no. should be between 10 and 75) and (10 is smallest and 75 is the biggest)\nEnter the size of the circle:  '))    
    b.pu()
    b.goto(0, 175 )
    b.pd()
    if (x <= 27 and x >= 10) and (y <= 75 and y >= 10):
        for _ in range(360//x):
            b.circle(y)
            b.fd(20)
            b.rt(x)
    else:
       print('Invalid no. in either or both inputs\nRun the code again' )

def design_square():
    b.pu()
    b.goto(0, 150 )
    b.pd()
    for _ in range(18):
            square()
            b.fd(20)
            b.rt(20)

design_circle()