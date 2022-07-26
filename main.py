from turtle import Turtle, Screen

toby = Turtle()
screen = Screen()

def move_forward():
    toby.fd(10)

def move_backwards():
    toby.bk(10)

def turn_right():
    new_heading = toby.heading() - 10
    toby.setheading(new_heading)

def turn_left():
    new_heading = toby.heading() + 10
    toby.setheading(new_heading)

def clear():
    toby.home()
    toby.clear()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
