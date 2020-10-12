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
    # move_length = (radius*2)*i/(sides/2) if (i<=sides/2) else (radius*2)*(sides-i)/(sides/2)
    move_length = radius*2
    t.left(6)
    t.left(turn_angle)
    t.forward(move_length)
    t.penup()
    t.backward(move_length)
    t.pendown()
    t.right(turn_angle)
    t.forward(side_length)
    i += 1
