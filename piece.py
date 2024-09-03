from turtle import Turtle

class Piece(Turtle):
    def __init__(self,player, path, inactive_pos, active_pos):
        super().__init__()
        self.shape("circle")
        self.pensize(15)
        self.pencolor("white")
        self.speed(0)
        self.player = player
        self.path = path
        self.inactive_pos = inactive_pos
        self.active_pos = active_pos
        self.box_size = 41
        self.current_pos = -1
        self.is_active = True
        self.penup()
        if player == 1:
            self.fillcolor("green")
        if player == 2:
            self.fillcolor("yellow")
        if player == 3:
            self.fillcolor("blue")
        if player == 4:
            self.fillcolor("red")

        # self.goto(self.path[self.current_pos])
        self.goto(inactive_pos)
        self.onclick(fun=self.handle_click)

    def handle_click(self,x,y):
        self.move(1)
        
    def move(self, step):
        self.current_pos = self.current_pos + step
        self.goto(self.path[self.current_pos])

