from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, number_player):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if number_player == 1:
            self.goto(x=350, y=0)
        else:
            self.goto(x=-350, y=0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)