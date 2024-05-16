import turtle
import colorsys

turtle.bgcolor("#043c4d")

keith = turtle.Turtle()
keith.color("#7df582")
keith.width(2)
keith.speed(0)

Point = tuple[int, int]


def triangle(p1: Point, p2: Point, p3: Point, depth=0):
    if depth >= 6:
        return
    keith.color("white")
    keith.penup()
    keith.goto(p1)
    keith.pendown()
    keith.goto(p2)
    keith.goto(p3)
    keith.goto(p1)
    p4 = ((p2[0] + p1[0]) // 2, (p2[1] + p1[1]) // 2)
    p5 = ((p3[0] + p2[0]) // 2, (p3[1] + p2[1]) // 2)
    p6 = ((p3[0] + p1[0]) // 2, (p3[1] + p1[1]) // 2)
    triangle(p1, p4, p6, depth + 1)
    triangle(p4, p2, p5, depth + 1)
    triangle(p6, p5, p3, depth + 1)
    keith.color(colorsys.hls_to_rgb(depth / 6, 0.7, 0.7))
    keith.penup()
    keith.goto(p1)
    keith.pendown()
    keith.goto(p2)
    keith.goto(p3)
    keith.goto(p1)


triangle((-384, -384), (0, 384), (384, -384))

turtle.done()
