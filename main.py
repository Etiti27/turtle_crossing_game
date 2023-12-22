from turtle import Screen
import time
from player import Player
from cars import Cars
from scoreboard import ScoreBoard

screen = Screen()
car = Cars()
screen.tracer(0)
player = Player()
score = ScoreBoard()

is_game_on = True
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.listen()
while is_game_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move_player, 'Up')
    car.create_car()
    car.moving_cars()
    for cars in car.all_car:
        if cars.distance(player) < 20:
            time.sleep(1)
            score.game_over()
            player.go_to_start_position()
            is_game_on = False


    if player.player_crossed():
        player.go_to_start_position()
        car.speed_up()
        score.update_score()

screen.exitonclick()
