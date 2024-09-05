import turtle
# from board import Board
from piece import Piece
from turtle import Screen
from dice import Dice
from player import p
from action import action_writer

game_is_on = True

screen = Screen()
screen.setup(width=750, height=750)
screen.title("Dice")
screen.listen()
screen._root.iconbitmap("./resources/Dice.ico")
# screen.bgpic("./resources/dice_bg.gif")
screen.bgpic("./resources/bg_color.gif")
screen.addshape("./resources/dice_2.gif")
screen.addshape("./resources/dice_1.gif")
screen.addshape("./resources/dice_3.gif")
screen.addshape("./resources/dice_4.gif")
screen.addshape("./resources/dice_5.gif")
screen.addshape("./resources/dice_6.gif")
screen.addshape("./resources/dice_blank.gif")

#Board
# board = Board() 


# Dice
dice = Dice()

def handle_dice_roll():
    if not Dice.allow_rolling:
        # Piece.allow_moving = False
        return
    Dice.allow_rolling = False
    dice.roll()
    Piece.allow_moving = True
    action_writer.update_action(1)
    if Dice.current_value != 6:
        p.handle_player_change

    
screen.onkeypress(handle_dice_roll, " ")

# test
# p1 = Piece(1,path_1, inactive_pos_1[0])
# p2 = Piece(2,path_2, inactive_pos_1[1])
# p3 = Piece(3,path_3, inactive_pos_1[2])
# p4 = Piece(4,path_4, inactive_pos_1[3])

# debug
def handle_click(x,y):
    print(x,y)
# screen.onclick(handle_click)
# screen.onkeypress(lambda: p1.move(1), "Left")
# screen.onkeypress(lambda: p2.move(1), "Up")
# screen.onkeypress(lambda: p3.move(1), "Right")
# screen.onkeypress(lambda: p4.move(1), "Down")

turtle.mainloop()
