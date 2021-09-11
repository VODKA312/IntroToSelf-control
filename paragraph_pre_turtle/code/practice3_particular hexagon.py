import turtle
amy = turtle.Turtle()
amy.width(5)
amy.color("purple")
lists = [1,2,3,4,5,6]
sides = [1,2,3,4,5,6]
for list in lists:
    for side in sides:
        amy.right(60)
        amy.forward(50)
    amy.penup()
    amy.left(60)
    amy.forward(20)
    amy.pendown()
