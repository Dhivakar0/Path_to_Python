import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

score = Scoreboard()
cars = CarManager()
screen.listen()
screen.onkeypress(fun=player.move,key="Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()

    # Detect when car hits player.
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_finish()

    #  Detect successful crossing and level up.
    if player.ycor() > 280:
        score.increase_level()
        player.restart()
        cars.increase_speed()


screen.exitonclick()


