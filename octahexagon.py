import colorsys
import turtle

turtle.bgcolor("#2C2C32")

octa = turtle.Turtle()
octa.width(5)
octa.color("white")
octa.penup()
octa.goto((-500, 300))
octa.pendown()

hexa = turtle.Turtle()
hexa.width(5)
hexa.color("white")
hexa.penup()
hexa.goto((280, 300))
hexa.pendown()

for i in range(8):
    octa.color(colorsys.hsv_to_rgb(i / 8 % 1, 0.5, 0.7))
    octa.forward(200)
    octa.right(45)

for i in range(6):
    hexa.color(colorsys.hsv_to_rgb(i / 6 % 1, 0.5, 0.7))
    hexa.forward(280)
    hexa.right(60)

turtle.done()
