from turtle import Turtle
ALIGN="center"
FONT=("Times",20,"normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,290)
        self.color("black")
        with open("data.txt", mode="r") as data:
            self.hs = int(data.read())
        self.hideturtle()
        self.hideturtle()
        self.count = 0
        print(self.hs)

    def new_score(self):
        self.clear()
        self.count += 1
        self.write(arg=f"Sneki Snek Score: {self.count} High score: {self.hs}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.write(arg=f"GAME OVER. Your final score is {self.count}",align=ALIGN,font=("Times",20,"bold"))

    def high_score(self):
       if self.count>self.hs:
           with open("data.txt", mode="w") as data:
            data.write(str(self.count))
           self.hs = self.count
       self.count=0
       self.clear()
       self.write(arg=f"Sneki Snek Score: {self.count} High score: {self.hs}", align=ALIGN, font=FONT)

