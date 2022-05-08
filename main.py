import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    if player.detect_finish_line():
        scoreboard.update_level()
        car_manager.speed_up()

    car_manager.update_cars()
    car_manager.generate_car()



screen.exitonclick()