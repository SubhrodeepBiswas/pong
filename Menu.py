from turtle import Turtle

class Menu(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()

    def show(self):
        self.goto(0, 100)
        self.write("PONG GAME", align="center", font=("Courier", 40, "bold"))

        self.goto(0, 20)
        self.write("Press SPACE to Start", align="center", font=("Courier", 20, "normal"))

        self.goto(0, -40)
        self.write("W/S = Left Paddle | ↑/↓ = Right Paddle",
                   align="center", font=("Courier", 14, "normal"))

    def clear_menu(self):
        self.clear()