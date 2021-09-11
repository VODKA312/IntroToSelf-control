# rainbow.py

from turtle import *
from random import *


def HSB2RGB(hues):
    hues = hues * 3.59  # 100转成359范围
    rgb = [0.0, 0.0, 0.0]
    i = int(hues / 60) % 6
    f = hues / 60 - i
    if i == 0:
        rgb[0] = 1;
        rgb[1] = f;
        rgb[2] = 0
    elif i == 1:
        rgb[0] = 1 - f;
        rgb[1] = 1;
        rgb[2] = 0
    elif i == 2:
        rgb[0] = 0;
        rgb[1] = 1;
        rgb[2] = f
    elif i == 3:
        rgb[0] = 0;
        rgb[1] = 1 - f;
        rgb[2] = 1
    elif i == 4:
        rgb[0] = f;
        rgb[1] = 0;
        rgb[2] = 1
    elif i == 5:
        rgb[0] = 1;
        rgb[1] = 0;
        rgb[2] = 1 - f
    return rgb


def rainbow():
    hues = 0.0
    color(1, 0, 0)
    # 绘制彩虹
    hideturtle()
    speed(100)
    pensize(3)
    penup()
    goto(-400, -300)
    pendown()
    right(110)
    for i in range(100):
        circle(1000)
        right(0.13)
        hues = hues + 1
        rgb = HSB2RGB(hues)
        color(rgb[0], rgb[1], rgb[2])
    penup()


def main():
    setup(800, 600, 0, 0)
    bgcolor((0.5, 0.8, 1.0))
    tracer(False)
    rainbow()
    # 输出文字
    goto(100, -100)
    pendown()
    color("red")
    write("Rainbow", align="center", font=("Script MT Bold", 80, "bold"))
    tracer(True)
    mainloop()


if __name__ == '__main__':
    main()