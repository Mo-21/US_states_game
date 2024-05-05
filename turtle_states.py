from turtle import Turtle


class State(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.cor = (0, 0)

    def write_state(self, x_cor, y_cor, state_name):
        self.cor = (x_cor, y_cor)
        self.goto(self.cor)
        self.write(state_name)
