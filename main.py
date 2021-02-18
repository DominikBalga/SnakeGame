import time
import turtle as t
from snakefood import Food
import snake
import scoreboard

screen = t.Screen()
screen.tracer(0)
screen.screensize(600, 610, "yellow")
boa = snake.Snake()
food = Food()
score = scoreboard.Scoreboard()
score.clear()
score.write(arg=f"Sneki Snek Score: {score.count} High score: {score.hs}", align="center", font=("Times",20,"normal"))
screen.update()
screen.listen()
screen.onkeypress(boa.left, "d")
screen.onkeypress(boa.right, "a")
screen.onkeypress(boa.up, "w")
screen.onkeypress(boa.down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    boa.move()

    if boa.snake[0].distance(food) < 15:
        food.refresh()
        score.new_score()
        boa.extend()

    if boa.snake[0].xcor() >= 380 or boa.snake[0].xcor() <= -380 or boa.snake[0].ycor() >= 340 or boa.snake[
        0].ycor() <= -320:
        score.high_score()
        boa.reset()

    for part in boa.snake[1:len(boa.snake)]:
        if boa.snake[0].distance(part) < 10:
            score.high_score()
            boa.reset()
screen.exitonclick()
