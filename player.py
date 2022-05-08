from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def detect_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False

    def detect_collision(self, cars):
        for c in cars:
            if self.distance(c) < 30:
                return True
        return False
