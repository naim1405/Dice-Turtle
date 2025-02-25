from turtle import Turtle
from dice import Dice
from player import p
from action import action_writer

from player import Player


class Piece(Turtle):
    allow_moving = False
    piece_status = {
        0: {"available": 4, "active": 0},
        1: {"available": 4, "active": 0},
        2: {"available": 4, "active": 0},
        3: {"available": 4, "active": 0},
    }
    next_player = True

    def __init__(self, player, path, inactive_pos, active_pos):
        super().__init__()
        self.shape("circle")
        self.pensize(15)
        self.pencolor("black")
        self.speed(0)
        self.player = player
        self.path = path
        self.inactive_pos = inactive_pos
        self.active_pos = active_pos
        self.box_size = 41
        self.current_pos = -1
        self.is_active = False
        self.penup()
        self.path_len = 56
        self.is_finished = False
        if player == 0:
            self.fillcolor("green")
        if player == 1:
            self.fillcolor("yellow")
        if player == 2:
            self.fillcolor("blue")
        if player == 3:
            self.fillcolor("red")

        self.goto(inactive_pos)
        self.speed(6)
        self.onclick(fun=self.handle_click)

    def handle_click(self, x, y):
        self.move()

    def move(self):
        if self.is_active:
            if Player.current_player == self.player and Piece.allow_moving:
                next_idx = self.current_pos + Dice.current_value
                if next_idx <= self.path_len:
                    self.goto(self.path[next_idx])
                    self.current_pos = next_idx
                    check_overlap(self)
                    if Dice.current_value != 6:
                        Piece.next_player = True
                    else:
                        Piece.next_player = False
                else:
                    if Piece.piece_status[self.player]["available"] > 1:
                        Piece.next_player = True
                        return
                    Piece.next_player = False

                if next_idx == self.path_len:
                    self.is_finished = True
                    Piece.piece_status[self.player]["available"] = (
                        Piece.piece_status[self.player]["available"] - 1
                    )

                Piece.allow_moving = False
                Dice.allow_rolling = True
                if self.is_finished:
                    Piece.allow_moving = True
            if Piece.next_player:
                if Dice.current_value != 6:
                    p.handle_player_change()
                action_writer.update_action(0)
                Piece.next_player = False

        elif self.player == Player.current_player and (
            not self.is_active and Dice.current_value == 6
        ):
            self.is_active = True
            self.goto(self.active_pos)
            Dice.allow_rolling = True
            action_writer.update_action(0)
            Piece.piece_status[self.player]["active"] += 1

        elif self.player == Player.current_player and not self.is_active:
            if Piece.piece_status[self.player]["active"] == 0:
                p.handle_player_change()
                Dice.allow_rolling = True
                action_writer.update_action(0)


    def set_inactive(self):
        self.is_active = False
        self.goto(self.inactive_pos)
        
    
    
from piece_path import *

players = {
    0:[],
    1:[],
    2:[],
    3:[],
}


for i in range(4):
    from piece import Piece
    for j in range(4):
        if i == 0:
            _ = Piece(i,path_1, inactive_pos_1[j], active_pos_1[j])
            players[0].append(_)
        elif i == 1:
            _ = Piece(i,path_2, inactive_pos_2[j], active_pos_2[j])
            players[1].append(_)
        elif i == 2:
            _ = Piece(i,path_3, inactive_pos_3[j], active_pos_3[j])
            players[2].append(_)
        elif i == 3 :
            _ = Piece(i,path_4, inactive_pos_4[j], active_pos_4[j])
            players[3].append(_)
    
def check_overlap(moved_piece):
    for (idx, pieces) in players.items():
        if idx != Player.current_player:
            for item in pieces:
                if moved_piece.pos() == item.pos():
                    item.set_inactive()
