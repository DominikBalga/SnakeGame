import turtle as t
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

class Snake():
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in starting_positions:
            self.add_part(position)

    def move(self):
        for part in range(len(self.snake) - 1, 0, -1):
            x = self.snake[part - 1].position()
            self.snake[part].goto(x)
        self.snake[0].fd(20)

    def right(self):
        head = self.snake[0].heading()
        if head != 0:
            self.snake[0].setheading(180)
        else:
            pass
    def left(self):
        head = self.snake[0].heading()
        if head != 180:
            self.snake[0].setheading(0)
        else:
            pass
    def up(self):
        head = self.snake[0].heading()
        if head!=270:
            self.snake[0].setheading(90)
        else:
            pass
    def down(self):
        head=self.snake[0].heading()
        if head!=90:
            self.snake[0].setheading(270)
        else:
            pass
    def add_part(self,position):
        self.part = t.Turtle("square")
        self.part.color("black")
        self.part.pencolor("red")
        self.part.penup()
        self.part.goto(position)
        self.snake.append(self.part)
    def extend(self):
        self.add_part(self.snake[-1].position())

    def reset(self):
        for snake in self.snake:
            snake.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
