import sys
from PySide2.QtWidgets import (QLCDNumber, QVBoxLayout)
from PySide2.QtWidgets import (QLCDNumber, QVBoxLayout)


class NumberDisplay(QLCDNumber):

    def __init__(self, parent=None):
        super(NumberDisplay, self).__init__(parent)
        self.reset()
        self.setSegmentStyle(QLCDNumber.Flat)

    def reset(self):
        import random
        self.score = 0
        self.reset_display()

    def reset_display(self):
        self.display("%03d" % self.score)
        self.setDigitCount(3)
        self.repaint()
