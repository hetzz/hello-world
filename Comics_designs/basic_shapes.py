import turtle
import time
a = turtle.Screen()
a.title('Shapes')
a.bgcolor("black")
a.setup(width=1000, height=1000)
b = turtle.Turtle()
b.color('white')
b.pensize(5)

def circle():
    b.circle(50)

def pentagon():
    for _ in range(5):
        b.fd(100)
        b.lt(72)
def hexagon():
    for _ in range(6):
        b.fd(100)
        b.lt(60)
def parallelogram():
    b.fd(200)
    b.lt(45)
    b.fd(100)
    b.lt(135)
    b.fd(200)
    b.lt(45)
    b.fd(100)

def my_name():
    b.write('Hetal',False,'center',('algerian', 100, 'bold'))

time.sleep(10)
b.penup()
b.fd(-500)
b.pendown()
circle()
b.penup()
b.fd(200)
b.pendown()
pentagon()
hexagon()
b.penup()
b.fd(200)
b.pendown()
parallelogram()
b.penup()
b.lt(50)
b.fd(500)
b.pendown()
my_name()
a.mainloop()
