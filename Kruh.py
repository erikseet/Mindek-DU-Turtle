from Tvar import Tvar
class Circle(Tvar):
    def __init__(self, pos_x, pos_y, side_adam):
        super().__init__(pos_x, pos_y)
        self.adam = side_adam

    def draw(self, turtle):
        super().draw(turtle)
        if self.color != None:
            turtle.pencolor(self.color)
        turtle.circle(self.adam)