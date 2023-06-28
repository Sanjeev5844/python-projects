# importing turtle for graphics
import turtle

# Forming the window screen
tut = turtle.Screen()

# background color green
tut.bgcolor("black")

# object
pen = turtle.Turtle()

#speed of pen
pen.speed(25)

# object color
pen.color("red")

# object width
pen.width(30)
tut = turtle.Screen()


# Code for symbol
# backward C
for x in range(200):
    pen.forward(2)
    pen.right(2)

# up
pen.right(100)
pen.forward(60)

# right
pen.right(90)
pen.forward(130)

# down
pen.right(90)
pen.forward(50)
pen.left(90)

# forward C
for x in range(180):
    pen.backward(3)
    pen.right(3)

turtle.done()
