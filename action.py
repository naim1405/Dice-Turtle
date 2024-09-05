from turtle import Turtle, mainloop
from player import Player

class Action(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.current_action = 0
        self.write_action()

    def write_action(self):
        self.clear()
        self.goto(120,320)
        self.color("black")
        self.write(f"Do: ", font=("Arial", 24, "normal"))
        self.forward(60)
        self.color(Player.player_color[Player.current_player])
        if self.current_action == 0:
            # self.color("Red")
            self.write(f"Roll Dice", font=("Arial", 24, "normal"))
            
        if self.current_action == 1:
            # self.color("Green")
            self.write(f"Move Piece", font=("Arial", 24, "normal"))
    def update_action(self, value):
        self.current_action = value
        self.write_action()


action_writer = Action()