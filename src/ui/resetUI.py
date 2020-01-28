import sys
from PySide2.QtWidgets import (QPushButton, QVBoxLayout)
from PySide2.QtGui import (QIcon)
from PySide2.QtCore import (SIGNAL, QObject, QSize)


DEFAULT = 'smile'
PRESSED = 'wait'
LOST = 'fail'
WIN = 'win'


class ResetButton(QPushButton):

    def __init__(self, parent=None):
        super(ResetButton, self).__init__(parent)
        self.set_state(DEFAULT)

    def set_state(self, state):
        self.state = state
        self.set_icon()
        self.refresh_stylesheet()

    def reset(self):
        self.set_state(DEFAULT)

    def set_icon(self):
        self.setIcon(QIcon('images/%s.png' % self.state))
        self.setIconSize(QSize(50, 50))

    def refresh_stylesheet(self):
        self.style().unpolish(self)
        self.style().polish(self)
