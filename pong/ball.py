from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.ball_speed = 0.09

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.95

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 15, "normal"))

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.ball_speed = 0.09