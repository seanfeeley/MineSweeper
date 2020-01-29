import sys
from src.ui.NumberDisplayUI import NumberDisplay
import src.model.GameStateController as gsc


class ScoreFrame(NumberDisplay):

    def __init__(self, mines, parent=None):
        super(ScoreFrame, self).__init__(parent)
        self.mines = mines
        self.flags = 0
        self.game_state = gsc.GameStateController()
        self.game_state.add_flag.connect(self.flag_added)
        self.game_state.remove_flag.connect(self.flag_removed)
        self.set_the_score()

    def set_the_score(self):
        self.value = self.mines - self.flags
        self.refresh_display()

    def flag_added(self):
        self.flags += 1
        self.set_the_score()

    def flag_removed(self):
        self.flags -= 1
        self.set_the_score()
