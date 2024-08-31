import turtle
from PIL import Image
t = turtle.Turtle()
t.penup()
t.goto(-300,300)
t.pendown()
t.speed(0)

class Board:
    def __init__(self):
        self.board_size = 15
        self.box_size = 41
        self.path = [[[0,0]]] * 8
        self.final_path = [0] * 4
        self.piece_path = []
        self.create_board()

    def create_box(self,size, direction):
        t.pendown()
        for _ in range(4):
            t.forward(size)
            t.right(90 * direction)

    def create_left_path(self, direction, l, m , r):
        left = []
        right = []
        middle = []
        for i in range(3):
            for j in range(6):
                self.create_box(self.box_size,direction)
                coor = [t.xcor() - 21, t.ycor() + 21]
                if i == 0:
                    left.append(coor)
                elif i == 2:
                    right.insert(0,coor)
                elif i == 1:
                    middle.append(coor)
                if i == 1 and j == 5:
                    left.append(coor)
                t.forward(self.box_size)
            t.backward(6 * self.box_size)
            t.right(90 * direction)
            t.forward(self.box_size)
            t.left(90 * direction)
        self.path[l] = left
        self.path[r] = right
        middle.reverse()
        middle.append([-300 + 21 + (7 * self.box_size), 300 - 21 - (7 * self.box_size)])
        self.final_path[m] = middle

    def create_right_path(self, direction, l, m , r):
        left = []
        right = []
        middle = []
        for i in range(3):
            for j in range(6):
                self.create_box(self.box_size,direction)
                coor = [t.xcor() + 21, t.ycor() - 21]
                if i == 0:
                    left.append(coor)
                elif i == 2:
                    right.insert(0,coor)
                elif i == 1:
                    middle.append(coor)
                if i == 1 and j== 5:
                    left.append(coor)
                t.forward(self.box_size)
            t.backward(6 * self.box_size)
            t.right(90 * direction)
            t.forward(self.box_size)
            t.left(90 * direction)
        self.path[l] = left
        self.path[r] = right
        middle.reverse()
        middle.append([-300 + 21 + (7 * self.box_size), 300 - 21 - (7 * self.box_size)])
        self.final_path[m] = middle
    
    def create_top_path(self, direction, l, m, r):
        left = []
        middle = []
        right = []
        for i in range(6):
            for j in range(3):
                self.create_box(self.box_size, direction)
                coor = [t.xcor() + 21, t.ycor() - 21]
                if j == 0:
                    left.insert(0, coor)
                elif j == 2:
                    right.append(coor)
                elif j == 1 and i != 0:
                    middle.append(coor)
                if j == 1 and i == 0:
                    right.append(coor)
                t.forward(self.box_size)
            t.backward(3 * self.box_size)
            t.right(90 * direction)
            t.forward(self.box_size)
            t.left(90 * direction)
        

        self.path[l] = left
        self.path[r] = right
        middle.append([-300 + 21 + (7 * self.box_size), 300 - 21 - (7 * self.box_size)])
        self.final_path[m] = middle
    def create_bottom_path(self, direction, l, m, r):
        left = []
        middle = []
        right = []
        for i in range(6):
            for j in range(3):
                self.create_box(self.box_size, direction)
                coor = [t.xcor() - 21, t.ycor() - 21]
                if j == 0:
                    left.append(coor)
                elif j == 2:
                    right.insert(0,coor)
                elif j == 1:
                    middle.append(coor)
                if j == 1 and i == 5:
                    left.append(coor)
                t.forward(self.box_size)
            t.backward(3 * self.box_size)
            t.right(90 * direction)
            t.forward(self.box_size)
            t.left(90 * direction)
        

        self.path[l] = left
        self.path[r] = right
        middle.reverse()
        middle.append([-300 + 21 + (7 * self.box_size), 300 - 21 - (7 * self.box_size)])
        self.final_path[m] = middle

    def create_path(self):
        for j in self.path:
            for i in j:
                self.piece_path.append(i)

    def create_board(self):
        self.create_box(self.board_size * self.box_size, 1)
        t.forward(6 * self.box_size)
        self.create_top_path(1, 7,0,0)
        t.forward(3 * self.box_size)
        self.create_right_path(1, 1 ,1, 2)
        t.right(180)
        self.create_bottom_path(-1, 3, 2, 4)
        t.forward(3 * self.box_size)
        t.right(90)
        t.forward(6 * self.box_size)
        t.left(90)
        self.create_left_path(1,5,3,6)
        self.create_path()

if __name__ == "__main__":
    b = Board()
    turtle.done()
