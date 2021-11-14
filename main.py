import turtle
from Obdlznik import Rectangle
from Trojuholnik import Triangle
from Kruh import Circle

vajco = turtle.Turtle()
vajco.speed(9)

circle = Circle(-269,50,169)
circle.setColor("purple")
circle.draw(vajco)

triangle = Triangle(169,69,269)
triangle.setColor("brown")
triangle.draw(vajco)

rectangle = Rectangle(-169,-69,369,169)
rectangle.setColor("black")
rectangle.draw(vajco)
print("funny number 69 XD")
turtle.exitonclick()