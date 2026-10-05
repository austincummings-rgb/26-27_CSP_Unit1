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
  painter.setheading(leg_angle * n)
  painter.forward(length_of_legs)
  n = n + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()