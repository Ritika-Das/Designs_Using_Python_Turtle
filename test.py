import turtle
import math


t = turtle.Turtle()
i = 1
flag = "running"
side_length = 10
circle_angle = 360
sides = 60

number_of_angles = (sides-2)*180
each_angle = number_of_angles/sides

per_turn = each_angle/sides

radius = (side_length*60)/(math.pi*2)

t.forward(side_length)

while flag!="end":
    if i == 61:
        flag = "end"
    turn_angle = i*(per_turn)
    t.left(6)
    t.left(turn_angle)
    t.forward(5)
    t.penup()
    t.backward(5)
    t.pendown()
    t.right(turn_angle)
    t.forward(side_length)
    i += 1
