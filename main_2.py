import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-80, -40, 0, 40, 80, 120]
all_turtles = []

for turtle_index in range(0, 6):
    new_tort = Turtle(shape="turtle")
    new_tort.color(colors[turtle_index])
    new_tort.penup()
    new_tort.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_tort)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_input:
                print(f"You won! The {winner} turtle is the winner!")
            else:
                print(f"You lost! The race {winner} is the winner turtle")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
