from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1
STARTING_X_POSITION = 320
CHANCE_OF_CAR_SPAWNING = 0.035


class CarManager(Turtle):

    def __init__(self):
        self.cars = []
        self.traffic_speed = STARTING_MOVE_DISTANCE
        self.spawn_chance = CHANCE_OF_CAR_SPAWNING
        self.generate_car()

    def generate_car(self):

        print(f"{self.spawn_chance * 100}%")

        # Randomize if a car will spawn or not.
        if random.random() < self.spawn_chance:

            # Create turtle.
            new_car = Turtle()
            new_car.penup()
            new_car.setheading(180)
            new_car.setx(STARTING_X_POSITION)
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))

            # Randomize y-position (rounded to the nearest 20s)
            random_y = round(random.randint(-250, 280) / 20.0) * 20
            new_car.sety(random_y)

            # Append new car to list of cars.
            self.cars.append(new_car)

    def speed_up(self):
        self.traffic_speed += MOVE_INCREMENT
        self.spawn_chance += 0.0175

    def update_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.hideturtle()
            else:
                car.forward(self.traffic_speed)


