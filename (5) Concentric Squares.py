import turtle
from turtle import *
speed(0)
t = turtle.Turtle()

for c in ['purple']:
  t.color(c)
  t.forward(175)
  t.left(90)
  t.forward(175)
  t.left(90)
  for i in range (170,0,-5):
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.left(90)
