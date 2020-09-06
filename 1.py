import turtle

t = turtle.Turtle()

for c in ['red', 'green', 'blue', 'purple']:
  for i in range (1,7):
    t.color(c)
    t.forward(75)
    t.left(90)
    t.left(15)
