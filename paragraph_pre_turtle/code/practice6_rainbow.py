import turtle
# create a turtle obj
rainbow = turtle.Turtle()
rainbow.width(5)
# Move back without drawing anything
rainbow.penup()
rainbow.back(250)
rainbow.pendown()
# Create a specific color list
colors = ["red","orange","yellow","green","blue","purple"]
for pretty_color in colors:
    rainbow.color(pretty_color)
    # Nesting loop start
    for side in [1,2,3]:
        if side == 1:
            rainbow.left(60)
        rainbow.right(30)
        rainbow.forward(20)
    # Nesting loop end
    rainbow.left(30)
# for loop end
rainbow.hideturtle()