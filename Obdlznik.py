from Tvar import Tvar
class Rectangle(Tvar):
    def __init__(self, pos_x, pos_y, side_adam, side_marek):
        super().__init__(pos_x,pos_y)
        self.s = side_adam
        self.c = side_marek
    def draw(self, turtle):
        super().draw(turtle)
        if self.color != None:
            turtle.pencolor(self.color)
        for i in range(0,2):
            turtle.fd(self.s)
            turtle.right(90)
            turtle.fd(self.c)
            turtle.right(90)