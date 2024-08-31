from turtle import Turtle, Screen
screen = Screen()

class Piece(Turtle):
    def __init__(self,player, path):
        super().__init__()
        self.shape("circle")
        self.pensize(15)
        self.pencolor("white")
        self.player = player
        self.path = path
        self.origin = []
        self.box_size = 41
        self.start = 0
        self.current_pos  = 0
        self.penup()
        if player == 1:
            self.origin = [-300 + (3 * self.box_size), 300 - (3 * self.box_size)]
            self.fillcolor("green")
        if player == 2:
            self.origin = [-300 + (12 * self.box_size), 300 - (3 * self.box_size)] 
            self.fillcolor("yellow")
        if player == 3:
            self.origin = [-300 + (12 * self.box_size), 300 - (12 * self.box_size)]
            self.fillcolor("blue")
        if player == 4:
            self.origin = [-300 + (3 * self.box_size), 300 - (12 * self.box_size)]
            self.fillcolor("red")

        # self.goto(self.origin)
        self.goto(self.path[self.current_pos])

    def move(self, step):
        self.current_pos = self.current_pos + step
        self.goto(self.path[self.current_pos])
        screen.update()

