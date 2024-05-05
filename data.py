import pandas as pd


class Data:

    def __init__(self):
        self.df = pd.read_csv("50_states.csv")
        self.states = self.df["state"].tolist()

    def check_answer(self, state):
        if self.states.__contains__(state):
            return True
        else:
            return False

