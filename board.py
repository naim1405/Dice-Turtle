import turtle
from PIL import Image

class Board:
    def __init__(self):

        self.t = turtle.Turtle()
        self.t.penup()
        self.t.goto(-300,300)
        self.t.pendown()
        self.t.speed(0)
        self.board_size = 15
        self.box_size = 41
        self.path = [[[0,0]]] * 8
        self.final_path = [0] * 4
        self.piece_path = []
        self.create_board()

    def create_box(self,size, direction):
        self.t.pendown()
        for _ in range(4):
            self.t.forward(size)
            self.t.right(90 * direction)
    def create_inactive_zone(self):
        self.t.penup()
        self.t.pencolor("red")
        self.t.goto(-300,300)
        self.t.right(180)
        self.t.forward(self.box_size)
        self.t.right(90)
        self.t.forward(self.box_size)
        # 1
        self.t.pencolor("green")
        for _ in range(4):
            self.create_box(self.box_size, 1)
            self.t.forward(self.box_size)
        self.t.penup()
        self.t.forward(5 * self.box_size)
        # 4
        self.t.pencolor("red")
        for _ in range(4):
            self.create_box(self.box_size, 1)
            self.t.forward(self.box_size)
        self.t.penup()
        self.t.goto((-300 + (15* self.box_size)),300 )
        self.t.forward(self.box_size)
        # 2
        self.t.pencolor("yellow")
        for _ in range(4):
            self.create_box(self.box_size, 1)
            self.t.forward(self.box_size)
        self.t.penup()
        self.t.forward(5 * self.box_size)
        # 3
        self.t.pencolor("blue")
        for _ in range(4):
            self.create_box(self.box_size, 1)
            self.t.forward(self.box_size)
        self.t.penup()

    def create_left_path(self, direction, l, m , r):
        for i in range(3):
            for j in range(6):
                self.create_box(self.box_size,direction)
                self.t.forward(self.box_size)
            self.t.backward(6 * self.box_size)
            self.t.right(90 * direction)
            self.t.forward(self.box_size)
            self.t.left(90 * direction)

    def create_right_path(self, direction, l, m , r):
        for i in range(3):
            for j in range(6):
                self.create_box(self.box_size,direction)
                self.t.forward(self.box_size)
            self.t.backward(6 * self.box_size)
            self.t.right(90 * direction)
            self.t.forward(self.box_size)
            self.t.left(90 * direction)
    
    def create_top_path(self, direction, l, m, r):
        for i in range(6):
            for j in range(3):
                self.create_box(self.box_size, direction)
                self.t.forward(self.box_size)
            self.t.backward(3 * self.box_size)
            self.t.right(90 * direction)
            self.t.forward(self.box_size)
            self.t.left(90 * direction)
        
    def create_bottom_path(self, direction, l, m, r):
        for i in range(6):
            for j in range(3):
                self.create_box(self.box_size, direction)
                self.t.forward(self.box_size)
            self.t.backward(3 * self.box_size)
            self.t.right(90 * direction)
            self.t.forward(self.box_size)
            self.t.left(90 * direction)

    def create_board(self):
        self.create_box(self.board_size * self.box_size, 1)
        self.t.forward(6 * self.box_size)
        self.create_top_path(1, 7,0,0)
        self.t.forward(3 * self.box_size)
        self.create_right_path(1, 1 ,1, 2)
        self.t.right(180)
        self.create_bottom_path(-1, 3, 2, 4)
        self.t.forward(3 * self.box_size)
        self.t.right(90)
        self.t.forward(6 * self.box_size)
        self.t.left(90)
        self.create_left_path(1,5,3,6)
        self.create_inactive_zone()
        self.t.hideturtle()

if __name__ == "__main__":
    b = Board()
    turtle.done()
