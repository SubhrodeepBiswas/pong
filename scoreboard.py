from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 36, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.l_score = 0
        self.r_score = 0

        self.game_over = False
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align=ALIGN, font=FONT)

        self.goto(100, 250)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        if not self.game_over:
            self.l_score += 1
            self.animate_score()
            self.check_win()

    def r_point(self):
        if not self.game_over:
            self.r_score += 1
            self.animate_score()
            self.check_win()

    def animate_score(self):
        # simple animation effect
        self.update_score()
        self.shapesize(1.2)
        self.getscreen().ontimer(lambda: self.shapesize(1), 100)

    def check_win(self):
        if self.l_score >= 10:
            self.game_over = True
            self.show_winner("LEFT PLAYER WINS!")

        elif self.r_score >= 10:
            self.game_over = True
            self.show_winner("RIGHT PLAYER WINS!")

    def show_winner(self, text):
        self.goto(0, 0)
        self.write(text, align=ALIGN, font=("Courier", 28, "bold"))
        self.goto(0, -40)
        self.write("Press R to Restart", align=ALIGN, font=("Courier", 18, "normal"))

    def reset(self):
        self.l_score = 0
        self.r_score = 0
        self.game_over = False
        self.clear()
        self.update_score()