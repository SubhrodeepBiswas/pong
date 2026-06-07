import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from Menu import Menu
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Ultimate")
screen.tracer(0)

def draw_center_line():
    line = turtle.Turtle()
    line.color("white")
    line.penup()
    line.goto(0, 300)
    line.setheading(270)
    line.hideturtle()

    for _ in range(30):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)

draw_center_line()

# Objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
menu = Menu()

game_started = False

# MENU
menu.show()


# RESET FUNCTION
def reset_game():
    global game_started
    scoreboard.reset()
    ball.reset_position()
    game_started = False
    menu.show()


# START GAME
def start_game():
    global game_started
    menu.clear_menu()
    game_started = True


# KEY BINDINGS
screen.listen()

screen.onkey(start_game, "space")
screen.onkey(reset_game, "r")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")


# GAME LOOP
while True:
    time.sleep(0.01)
    screen.update()

    if not game_started:
        continue

    if scoreboard.game_over:
        continue

    ball.move()

    # Wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Score
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()