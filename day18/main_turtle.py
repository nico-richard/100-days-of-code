from turtle import Turtle, Screen


turtle1 = Turtle()
screen1 = Screen()

turtle1.shape('turtle')
turtle1.penup()
turtle1.speed(0)
turtle1.width(1)
turtle1.setpos((-220, 220))

turtle1.pendown()
for i in range(2000):
    turtle1.forward(500)
    turtle1.right(91)
    i += 1

screen1.exitonclick()
