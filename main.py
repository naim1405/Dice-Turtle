import turtle
from board import Board
from piece import Piece
from turtle import Screen

from piece_path import *

game_is_on = True

board = Board() 
p1 = Piece(1,path_1, inactive_pos_1[0], active_pos_1[0])
p2 = Piece(2,path_2, inactive_pos_2[0], active_pos_2[0])
p3 = Piece(3,path_3, inactive_pos_3[0], active_pos_3[0])
p4 = Piece(4,path_4, inactive_pos_4[0], active_pos_4[0])

# test
# p1 = Piece(1,path_1, inactive_pos_1[0])
# p2 = Piece(2,path_2, inactive_pos_1[1])
# p3 = Piece(3,path_3, inactive_pos_1[2])
# p4 = Piece(4,path_4, inactive_pos_1[3])

screen = Screen()
screen.setup(width=800, height=800)
screen.listen()
# debug
screen.onkeypress(lambda: p1.move(1), "Left")
screen.onkeypress(lambda: p2.move(1), "Up")
screen.onkeypress(lambda: p3.move(1), "Right")
screen.onkeypress(lambda: p4.move(1), "Down")



while game_is_on:
    screen.update()
