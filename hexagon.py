import turtle

# Number of Sides 	Polygon name 	Exterior Angle
# 5 	Pentagon 	72
# 6 	Hexagon 	60
# 7 	Heptagon 	51.42
# 8 	Octagon 	45
# 9 	Nanogon 	40
# 10 	Decagon 	36

screen = turtle.Screen()

mathTurtle = turtle.Turtle()

for i in range(6):
    # Move forward by 90 units
    mathTurtle.forward(90)

    # Turn left the turtle by 300 degrees
    mathTurtle.left(300)

mathTurtle.penup()
mathTurtle.goto(50, 250)
mathTurtle.pendown()

for i in range(5):
    mathTurtle.forward(100)  # Assuming the side of a pentagon is 100 units
    mathTurtle.right(72)  # Turning the turtle by 72 degree

mathTurtle.penup()
mathTurtle.goto(260, 250)
mathTurtle.pendown()

for i in range(8):
    mathTurtle.forward(100)  # Assuming the side of a pentagon is 100 units
    mathTurtle.right(45)  # Turning the turtle by 72 degree

screen.mainloop()
