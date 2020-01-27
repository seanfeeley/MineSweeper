import sys
from PySide2.QtWidgets import (QPushButton, QVBoxLayout)
from PySide2.QtGui import (QIcon)
from PySide2.QtCore import (SIGNAL, QObject, QSize)

LOST = 1
WON = 2
PRESSED = 3
PLAYING = 4


class ResetButton(QPushButton):

    def __init__(self, parent=None):
        super(ResetButton, self).__init__(parent)
        self.setStatePlaying()

    def setStatePlaying(self):
        self.setIcon(QIcon('images/smile.png'))
        self.setIconSize(QSize(50, 50))
