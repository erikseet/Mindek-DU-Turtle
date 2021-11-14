from Tvar import Tvar
class Triangle(Tvar):
    def __init__(self, pos_a, pos_b, side_adam):
        super().__init__(pos_a, pos_b)
        self.adam = side_adam
    def draw(self, turtle):
        super().draw(turtle)
        if self.color != None:
            turtle.pencolor(self.color)
        turtle.fd(self.adam)
        turtle.left(120)
        turtle.fd(self.adam)
        turtle.left(120)
        turtle.fd(self.adam)
        turtle.left(120)