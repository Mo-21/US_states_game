import turtle
from data import Data

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = Data()

answer = screen.textinput(title="Guess The States", prompt="What is the state's name?")
data.check_answer(answer)

screen.exitonclick()
