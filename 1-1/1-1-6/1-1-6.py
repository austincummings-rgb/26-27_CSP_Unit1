#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
# Create spider body
painter.pensize(40)
painter.circle(20)
# configure spider legs
legs = 6
length_of_legs = 70
leg_angle = 360 / legs
painter.pensize(5)

#draw legs

n = 0
while (n < legs):
  painter.goto(0, 20)
  if n <=3:
    painter.setheading((leg_angle * n) -45)
  if n >3:
    painter.setheading(leg_angle * n + 45)
    painter.forward(length_of_legs)
  n = n + 1
  painter.forward(length_of_legs)
  n = n + 1

  # configure and draw eyes
  painter .pensize(6)
  painter.color("red")

  #Moveing to first eye
  painter.penup()
  painter.goto(-5, 50)
  painter.pendown()
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()