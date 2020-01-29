import sys
from PySide2.QtWidgets import (QPushButton, QVBoxLayout)
from PySide2.QtGui import (QIcon)
from PySide2.QtCore import (QSize)
import src.model.GameStates as states
import src.model.GameStateController as gsc

class ResetButton(QPushButton):

    def __init__(self, parent=None):
        super(ResetButton, self).__init__(parent)
        self.set_state(states.NORMAL)
        self.game_state = gsc.GameStateController()
        self.game_state.set_game_lost.connect(self.game_lost)
        self.game_state.set_game_won.connect(self.game_won)
        self.game_state.set_game_reset.connect(self.game_reset)
        self.game_state.set_game_wait.connect(self.game_wait)
        self.game_state.set_game_normal.connect(self.game_normal)

    def mouseClickEvent(self, QMouseEvent):
        super(ResetButton, self).mouseClickEvent(QMouseEvent)
        self.game_reset.emit()

    def game_lost(self):
        self.game_state.game_over = True
        self.set_state(states.LOST)

    def game_won(self):
        self.set_state(states.WON)

    def game_reset(self):
        self.game_state.game_over = False
        self.set_state(states.NORMAL)

    def game_wait(self):
        self.set_state(states.WAIT)

    def game_normal(self):
        self.set_state(states.NORMAL)

    def set_state(self, state):
        self.state = state
        self.set_icon()
        self.refresh_stylesheet()

    def reset(self):
        self.set_state(states.NORMAL)

    def set_icon(self):
        self.setIcon(QIcon('images/%s.png' % self.state))
        self.setIconSize(QSize(50, 50))

    def refresh_stylesheet(self):
        self.style().unpolish(self)
        self.style().polish(self)
