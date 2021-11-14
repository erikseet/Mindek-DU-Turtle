class Tvar:
    def __init__(self,pos_a, pos_b):
        self.xd = pos_a
        self.y = pos_b
        self.color = None
    def setColor(self, color):
        self.color = color
    def draw(self, turtle):
        turtle.penup()
        turtle.setpos(self.xd, self.y)
        turtle.pendown()