from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score



screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")




is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#Detect Collisions with Food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_size()
        score.increase_score()

# Detect Collisions with wall.
    if snake.head.xcor() >295 or snake.head.xcor() <-295 or snake.head.ycor() >295 or snake.head.ycor() <-280:
        score.reset()
        snake.reset()


# Detect collisions with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()




# Detect collisions with tail.
#     for segment in snake.segments:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 15:
#             is_game_on = False
#             score.game_over()





screen.exitonclick()