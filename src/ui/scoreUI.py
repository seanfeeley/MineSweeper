import sys
from PySide2.QtWidgets import (QFrame, QVBoxLayout)


class ScoreFrame(QFrame):

    def __init__(self, parent=None):
        super(ScoreFrame, self).__init__(parent)
        self.load_layout()

    def load_layout(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
