from turtle import Turtle

current_player = -1
player_color = {
    0:"Green",
    1:"Yellow",
    2:"Blue",
    3:"Red",
}
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.handle_player_change()

    def handle_player_change(self):
        global current_player
        current_player = (current_player + 1) % 4
        self.clear()
        self.goto(-300,340)
        print(current_player)
        self.color("black")
        self.write(f"Player : ", font=("Arial", 24, "normal"))
        self.color(player_color[current_player])
        self.forward(120)
        self.write(f"{player_color[current_player]}", font=("Arial", 24, "normal"))

    