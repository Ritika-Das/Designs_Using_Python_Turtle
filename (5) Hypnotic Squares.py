from turtle import *
speed(4)    # comment this line if you want to see the turtle in action, but slower
pencolor(128,0,128)    # RGB coordinates of the color 'purple'
fd(175)
lt(90)
fd(175)
lt(90)
for i in range (170,0,-5):
  fd(i)
  lt(90)
  fd(i)
  lt(90)
