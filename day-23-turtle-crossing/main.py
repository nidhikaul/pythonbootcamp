import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect Collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 10:
            game_is_on = False
            scoreboard.game_over()

    #Detect when the player has crossed the road
    if player.ycor() > 260:
        player.next_level()
        car_manager.level_up()
        scoreboard.player_point()





screen.exitonclick()
