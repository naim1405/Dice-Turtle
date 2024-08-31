from turtle import Turtle, Screen, done


class Piece(Turtle):
    def __init__(self,player, path, final_path):
        super().__init__()
        self.player = player
        self.path = path
        self.final_path = final_path
        self.origin = []
        self.box_size = 41
        self.start = 0
        if player == 1:
            self.origin = [-300 + (12 * self.box_size), 300 - (3 * self.box_size)] 
        if player == 2:
            self.origin = [-300 + (12 * self.box_size), 300 - (12 * self.box_size)]
        if player == 3:
            self.origin = [-300 + (3 * self.box_size), 300 - (12 * self.box_size)]
        if player == 4:
            self.origin = [-300 + (3 * self.box_size), 300 - (3 * self.box_size)]

        self.goto(self.origin)

#    def move(self, step):
#        for i in range(step):

