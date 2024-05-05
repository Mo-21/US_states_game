import turtle
from data import Data
from turtle_states import State

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = Data()
state = State()

while data.remaining_states > 0:
    answer = screen.textinput(title="Guess The States", prompt="What is the state's name?")

    if data.check_answer(answer):
        x_cor, y_cor = data.get_state_cor(answer)
        state.write_state(x_cor=x_cor, y_cor=y_cor, state_name=answer)

screen.exitonclick()
