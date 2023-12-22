from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISHING_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.penup()
        self.shape('turtle')
        self.color('red')
        self.go_to_start_position()
        self.left(90)

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def player_crossed(self):
        if self.ycor() > 280:
            return True
        else:
            return False
    def go_to_start_position(self):
        self.goto(STARTING_POSITION)