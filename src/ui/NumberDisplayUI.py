import sys
from PySide2.QtWidgets import (QLCDNumber, QVBoxLayout)
from PySide2.QtWidgets import (QLCDNumber, QVBoxLayout)


class NumberDisplay(QLCDNumber):

    def __init__(self, parent=None):
        super(NumberDisplay, self).__init__(parent)
        self.value = 0
        self.setSegmentStyle(QLCDNumber.Flat)
        self.setDigitCount(3)
        self.refresh_display()

    def reset(self):
        self.value = 0
        self.refresh_display()

    def refresh_display(self):
        self.display("%03d" % self.value)
