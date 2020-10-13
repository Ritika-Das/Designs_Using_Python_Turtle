import turtle
import math

ts = turtle.getscreen()
ts.colormode(255)

t = turtle.Turtle()
t.speed(0.5)
i = 1 #iterator
flag = "running"

side_length = 10
circle_angle = 360
sides = 60


# calculating the number of angles in a polygon with 60 sides , value of angle between each adjacent sides, then finding the angles of the diagonals
number_of_angles = (sides-2)*180
each_angle = number_of_angles/sides

per_turn = each_angle/sides

radius = (side_length*60)/(math.pi*2)
move_length = side_length



while flag!="end":
    if i == 61:
        flag = "end"
    turn_angle = i*(per_turn)
    t.pencolor(0,255,255) if (i<=sides/2) else t.pencolor(255,105,180)

    # Could'nt find the perfect length of each diagonal, but all these values look good

    move_length = (radius*2)*i/(sides/2)*1.6 if (i<=sides/2) else (radius*2)*(sides-i)/(sides/2)*1.6
    # move_length = radius*2
    # move_length = side_length*(0.7*i)
    # move_length = i*(1.6) if (i<=sides/2) else (sides - i)*1.6                               #value of phi(golden ratio) gave some weird lines but it kinda makes sense?
    # move_length = (radius*2*(i/sides/2)) if (i<=sides/2) else (radius*2*((sides-i)/sides/2))  # the ratio of radius and the diagonal count gives the golden ratio too!

    t.left(6)
    t.left(turn_angle)
    t.forward(move_length)
    t.penup()
    t.backward(move_length)
    t.pendown()
    t.right(turn_angle)
    t.forward(side_length)
    i += 1
