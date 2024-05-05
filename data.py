import pandas as pd


class Data:

    def __init__(self):
        self.df = pd.read_csv("50_states.csv")
        self.states = self.df["state"].tolist()
        self.remaining_states = len(self.states)

    def check_answer(self, state):
        if self.states.__contains__(state):
            self.remaining_states -= 1
            return True
        else:
            return False

    def get_state_cor(self, state):
        correct_state = self.df[self.df["state"] == state]
        x_cor = int(correct_state.x.iloc[0])
        y_cor = int(correct_state.y.iloc[0])
        return x_cor, y_cor
