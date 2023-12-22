from turtle import Turtle
import random

CAR_COLOR = ['red', 'blue', 'black', 'green', 'grey']
SPEED = 10


class Cars:
    def __init__(self):
        self.speed = SPEED
        self.all_car = []

    def create_car(self):
        rand_time = random.randint(1, 6)
        if rand_time == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(CAR_COLOR))
            random_number_y = random.randint(-220, 220)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(260, random_number_y)
            self.all_car.append(new_car)

    def moving_cars(self):
        for car in self.all_car:
            car.setheading(180)
            car.forward(self.speed)

    def speed_up(self):
        self.speed += SPEED
