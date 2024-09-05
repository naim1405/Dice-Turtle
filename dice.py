from turtle import Turtle, mainloop
from random import randint

class Dice(Turtle):
    prev_value = 0
    current_value = 0
    consecutive_six = 0
    allow_rolling = True
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(8,335)
        self.showturtle()
        self.shape(f"./resources/dice_blank.gif")
    def roll(self):
        random_dice = randint(1,6)
        if random_dice == 6:
            Dice.consecutive_six += 1
        else:
            Dice.consecutive_six = 0
        if Dice.consecutive_six == 3:
            Dice.consecutive_six -= 1
            self.roll()
            return
        Dice.prev_value = Dice.current_value
        Dice.current_value = random_dice
        self.shape(f"./resources/dice_{self.current_value}.gif")


if __name__ == "__main__":
    from turtle import Screen
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.addshape("./resources/dice_1.gif")
    screen.addshape("./resources/dice_2.gif")
    screen.addshape("./resources/dice_3.gif")
    screen.addshape("./resources/dice_4.gif")
    screen.addshape("./resources/dice_5.gif")
    screen.addshape("./resources/dice_6.gif")
    d = Dice()
    screen.listen()
    screen.onkeypress(d.roll, " ")

    mainloop()