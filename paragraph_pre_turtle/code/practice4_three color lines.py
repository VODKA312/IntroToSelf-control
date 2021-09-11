import turtle
amy = turtle.Turtle()
amy.width(5)
# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()
for prettycolor in ["red","yellow","blue"]:
    amy.color(prettycolor)
    amy.forward(100)
    if prettycolor != "blue":
        amy.penup() #expect blue to control the white area
        amy.forward(50)
    amy.pendown()

