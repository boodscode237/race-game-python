from turtle import Turtle, Screen

tort = Turtle()
screen = Screen()


def move_forwards():
    tort.forward(10)


def move_backwards():
    tort.backward(10)


def turn_left():
    new_heading = tort.heading() + 10
    tort.setheading(new_heading)


def turn_right():
    tort.right(10)


def clear():
    tort.clear()
    tort.penup()
    tort.home()
    tort.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(clear, "c")

screen.exitonclick()
