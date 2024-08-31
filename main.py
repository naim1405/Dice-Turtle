import turtle
from board import Board
from piece import Piece
from turtle import Screen

from piece_path import *

game_is_on = True

board = Board() 
p1 = Piece(1,path_1)
p2 = Piece(2,path_2)
p3 = Piece(3,path_3)
p4 = Piece(4,path_4)

screen = Screen()
screen.setup(width=800, height=800)
screen.listen()
screen.onkeypress(lambda: p1.move(1), "Left")
screen.onkeypress(lambda: p2.move(1), "Up")
screen.onkeypress(lambda: p3.move(1), "Right")
screen.onkeypress(lambda: p4.move(1), "Down")



while game_is_on:
    screen.update()
