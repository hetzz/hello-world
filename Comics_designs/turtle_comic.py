import random
import turtle
import time
a = turtle.Screen()
a.title('Stick Comic')
a.bgcolor("black")
a.setup(width=1750, height=850)
b = turtle.Turtle()
b.color('white')
b.pensize(5)
time.sleep(15)
def converse():
    c = turtle.Turtle()
    c.color('white')
    c.pensize(5)
    c.pu()
    c.goto(355, 200)
    c.pd()
    d = turtle.Turtle()
    d.color('white')
    d.pensize(5)
    d.pu()
    d.goto(-280, 205)
    d.pd()
    def man():
        b.penup()
        b.rt(180)
        b.fd(399)
        b.pendown()#    extention
        b.color('white')
        
        b.rt(90)
        b.fd(100)#      bodyline
        b.bk(100)
        
        b.lt(145)
        b.fd(75)#        left leg
        b.bk(75)
        
        b.lt(70)
        b.fd(75)#        right leg
        b.bk(75)
        b.rt(70)
        
        b.rt(145)#       body direction turn    
        
        b.fd(125)
        b.lt(120)#       left hand
        b.fd(75)
        b.bk(75)
        
        b.rt(240)
        b.fd(75)
        b.bk(75)#     right hand
        b.lt(120)
        
        b.fd(25)
        b.lt(90)#        neck
        
        b.circle(-25)#      face

        b.rt(90)
        b.penup()
        b.fd(15)
        b.pendown()
        b.color('white')   #   dialogue neck extension
        b.rt(70)
        b.fd(100)
        b.lt(100)

    man()
      
        
    def conversation():    
        b.penup()#           other man start
        b.home()
        
        b.fd(650)
        b.pendown()
        man()
        time.sleep(1)

        d.write('  Why are we stick figures?', False, font = ('Courier', 10, 'bold'))
       
        time.sleep(1)

        c.write('   Probably a Warli painting', font=('Courier', 10, 'bold'))
        
        time.sleep(2)
        d.clear()
        d.write("   The background is black", False, font = ('Courier', 10, 'bold'))
        time.sleep(2)
        a.bgcolor('#4f1e16')
        time.sleep(1)
        c.clear()
        c.write("    Looks like someone fixed it!!", False, font = ('Courier', 10, 'bold'))
        
        time.sleep(1)
        d.clear()
        d.write(" Lol Yeahhh!!", False, font = ('Courier', 10, 'bold'))
    
    conversation()

converse()
a.mainloop()