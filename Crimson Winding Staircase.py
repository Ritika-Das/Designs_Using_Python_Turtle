from turtle import *
speed(0)           # fastest cursor speed of out Python Turtle

x = 1

while x < 200:
    r = 175
    g = 0
    b = 42
    pencolor(r,g,b)
    fd(50 + x)
    rt(90.911)
    x = x+1
