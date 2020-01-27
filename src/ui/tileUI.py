import sys
from PySide2.QtWidgets import (QPushButton)
from PySide2.QtCore import (QSize)
from PySide2.QtGui import (QIcon)

import random

MINE = -3
FLAGGED = -2
HIDDEN = -1
BLANK = 0
HINT1 = 1
HINT2 = 2
HINT3 = 3
HINT4 = 4
HINT5 = 6
HINT6 = 7
HINT7 = 7
HINT8 = 8


class TileButton(QPushButton):

    def __init__(self, parent=None):
        super(TileButton, self).__init__(parent)
        self.state = HIDDEN
        self.set_state(random.randint(-3, 8))

    def set_state(self, state):
        self.reset_button()
        if state == MINE:
            self.show_mine()
        elif state == FLAGGED:
            self.show_flagged()
        elif state == HIDDEN:
            self.show_hidden()
        elif state == BLANK:
            self.show_blank()
        elif state >= HINT1:
            self.show_hint(state)
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
        self.reset_button()
        self.setObjectName("Flagged")
        self.setIcon(QIcon('images/flag.png'))
        self.setIconSize(QSize(20, 20))

    def show_hidden(self):
        self.reset_button()
        self.setObjectName("Hidden")

    def show_blank(self):
        self.reset_button()
        self.setObjectName("Blank")

    def show_hint(self, state):
        self.reset_button()
        self.setObjectName("Hint%d" % state)
        self.setText(str(state))
