from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-280, 260)
        self.write(f'level {self.level}', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.level += 2
        self.write(f'level {self.level}', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game over', font=('Arial', 20, 'normal'))
