import turtle
# create a turtle obj
amy = turtle.Turtle()
amy.width(5)
# Move back without drawing anything
amy.penup()
amy.back(250)
amy.pendown()
# for loop start
for pretty_color in ["red", "yellow", "blue"]:
    amy.color(pretty_color)
    # nesting loop start
    sides = [1, 2, 3, 4]
    for side in sides:
        amy.forward(100)
        amy.right(90)
    # nesting loop end
    amy.penup()
    amy.forward(200)
    amy.pendown()
# for loop end
