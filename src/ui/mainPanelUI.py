import sys
from PySide2.QtWidgets import (QWidget, QGridLayout, QApplication,
                               QLineEdit, QLayout, QLabel)
from PySide2.QtCore import Slot, Qt


class MainPanel(QWidget):

    def __init__(self, settings, parent=None):
        super(MainPanel, self).__init__(parent)
        self.settings = settings
