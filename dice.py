from turtle import Turtle, mainloop
from random import randint
import time

class Dice(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(8,360)
        self.showturtle()
        self.shape(f"./resources/dice_5.gif")
        self.prev_value = 0
        self.current_value = 0
        self.consecutive_six = 0
    def roll(self):
        random_dice = randint(1,6)
        print(random_dice)
        if random_dice == 6:
            self.consecutive_six += 1
        else:
            self.consecutive_six = 0
        if self.consecutive_six == 3:
            self.consecutive_six -= 1
            self.roll()
            return
        self.prev_value = self.current_value
        self.current_value = random_dice
        self.shape(f"./resources/dice_{self.current_value}.gif")

    def get_dice_value(self):
        return self.current_value

        

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

        
