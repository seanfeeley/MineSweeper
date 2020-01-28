import sys
from PySide2.QtWidgets import (QPushButton)
from PySide2.QtCore import (QSize)
from PySide2.QtGui import (QIcon)
import src.model.MineFieldStates as states
import random


class TileButton(QPushButton):

    def __init__(self, row, column, parent=None):
        super(TileButton, self).__init__(parent)
        self.row = row
        self.column = column
        self.set_state(states.HIDDEN)

    def set_state(self, state):
        self.state = state
        self.reset_button()
        if self.state == states.MINE:
            self.show_mine()
        elif self.state == states.FLAGGED:
            self.show_flagged()
        elif self.state == states.HIDDEN:
            self.show_hidden()
        elif self.state == states.BLANK:
            self.show_blank()
        elif self.state >= states.HINT1:
            self.show_hint(self.state)
        self.refresh_stylesheet()

    def refresh_stylesheet(self):
        self.style().unpolish(self)
        self.style().polish(self)

    def reset_button(self):
        self.setObjectName("")
        self.setIcon(QIcon())
        self.setText('')

    def show_mine(self):
        self.setObjectName("Mine")
        self.setIcon(QIcon('images/mine.png'))
        self.setIconSize(QSize(20, 20))

    def show_flagged(self):
        self.setObjectName("Flagged")
        self.setIcon(QIcon('images/flag.png'))
        self.setIconSize(QSize(20, 20))

    def show_hidden(self):
        self.setObjectName("Hidden")

    def show_blank(self):
        self.setObjectName("Blank")

    def show_hint(self, state):
        self.setObjectName("Hint%d" % state)
        self.setText(str(state))
