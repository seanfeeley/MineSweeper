import sys
from PySide2.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout
from PySide2.QtWidgets import (QPushButton, QSpacerItem, QSizePolicy)
from src.ui.scoreUI import ScoreFrame
import src.ui.resetUI as resetUI
from src.ui.timerUI import TimerFrame
from src.ui.gridUI import GridFrame


class MainPanel(QFrame):

    def __init__(self, settings, parent=None):
        super(MainPanel, self).__init__(parent)
        self.settings = settings
        self.reset_layout()

    def reset_layout(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.top_widget = QFrame()
        self.top_widget.setObjectName("top_widget")
        self.top_layout = QHBoxLayout()
        self.top_layout.setSpacing(0)
        self.top_layout.setMargin(0)
        self.top_layout.setContentsMargins(0, 0, 0, 0)
        self.top_widget.setLayout(self.top_layout)
        self.score_widget = ScoreFrame(self.settings['mines'])
        self.top_layout.addWidget(self.score_widget)
        self.top_layout.addStretch()

        self.reset_button = resetUI.ResetButton()
        self.top_layout.addWidget(self.reset_button)
        self.top_layout.addStretch()

        self.timer_widget = TimerFrame()
        self.top_layout.addWidget(self.timer_widget)

        self.bottom_widget = QFrame()
        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setSpacing(0)
        self.bottom_layout.setMargin(0)
        self.bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_widget.setLayout(self.bottom_layout)
        self.grid_widget = GridFrame(self.settings, parent=self)
        self.bottom_layout.addWidget(self.grid_widget)

        self.main_layout.addWidget(self.top_widget)
        self.main_layout.addWidget(self.bottom_widget)
