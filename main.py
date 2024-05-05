import turtle
from turtle import Screen

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = screen.textinput(title="Guess The States", prompt="What is the state's name?")
print(answer)

screen.exitonclick()