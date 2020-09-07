import turtle

t = turtle.Turtle()

for c in ['purple']:
  for i in range(5,20):
    t.color(c)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(75-i)
