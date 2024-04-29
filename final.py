import colorsys
import turtle

turtle.bgcolor("#2C2C32")

houda = turtle.Turtle()
houda.speed(0)

houda.penup()
houda.goto(-50, 50)
houda.pendown()

for i in range(720):
    color = colorsys.hsv_to_rgb(i / 360 % 1, 0.5, 0.7)
    houda.color(color)
    houda.forward(100 + i)
    houda.right(89)

turtle.done()
