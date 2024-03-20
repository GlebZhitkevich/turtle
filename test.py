from turtle import *
from time import sleep

t = Turtle()
t.color('blue')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(10)

def draw(x,y):
    t.goto(x,y)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def stepUp():
    t.goto(t.xcor(), t.ycor()+5)

def stepDown():
    t.goto(t.xcor(), t.ycor()-5)

def stepLeft():
    t.goto(t.xcor()-5, t.ycor())

def stepRight():
    t.goto(t.xcor()+5, t.ycor())

def setRed():
    t.color('red')
def setOrange():
    t.color('orange')
def setGreen():
    t.color('green')

def rand():
    while True:
        for i in ['red', 'orange',  'blue', 'green', 'yellow',  'darkviolet']:
            t.color(i)
            sleep(0.3)
t.ondrag(draw)
scr = t.getscreen()
scr.onscreenclick(move)
scr.listen()
scr.onkey(stepUp, 'Up')
scr.onkey(stepDown, 'Down')
scr.onkey(stepLeft, 'Left')
scr.onkey(stepRight, 'Right')
scr.onkey(setRed, 'r')
scr.onkey(setOrange, 'o')
scr.onkey(setGreen, 'g')
scr.onkey(rand, '1')
mainloop()