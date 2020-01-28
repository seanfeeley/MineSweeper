import sys
from src.ui.NumberDisplayUI import NumberDisplay


class ScoreFrame(NumberDisplay):

    def __init__(self, mines, parent=None):
        super(ScoreFrame, self).__init__(parent)
        self.mines = mines
        self.flags = 0
        self.set_the_score()

    def set_the_score(self):
        self.value = self.mines - self.flags
        self.refresh_display()

    def add_flag(self):
        self.flags += 1
        self.set_the_score()

    def remove_flag(self):
        self.flags -= 1
        self.set_the_score()
