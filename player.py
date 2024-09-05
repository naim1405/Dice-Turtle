from turtle import Turtle

class Player(Turtle):
    current_player = -1
    player_color = {
        -1:"White",
        0:"Green",
        1:"Yellow",
        2:"Blue",
        3:"Red",
    }
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.handle_player_change()

    def handle_player_change(self):
        Player.current_player = (Player.current_player + 1) % 4
        self.clear()
        self.goto(-300,320)
        self.color("black")
        self.write(f"Player : ", font=("Arial", 24, "normal"))
        self.color(Player.player_color[Player.current_player])
        self.forward(120)
        self.write(f"{Player.player_color[Player.current_player]}", font=("Arial", 24, "normal"))

    

p = Player()