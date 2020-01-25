import sys
from PySide2.QtWidgets import (QPushButton)

HIDDEN = 1
FLAGDED = 2
HINT = 3
MINE = 4


class TileButton(QPushButton):

    def __init__(self, row, column, has_mine, parent=None):
        super(TileButton, self).__init__(parent)
        self.has_mine = has_mine
        self.row = row
        self.column = column
        self.state = HIDDEN
        self.load_layout()

    def load_layout(self):
        pass
