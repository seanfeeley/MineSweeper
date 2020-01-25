import sys
from PySide2.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout
from src.ui.scoreUI import ScoreFrame
from src.ui.resetUI import ResetFrame
from src.ui.timerUI import TimerFrame
from src.ui.gridUI import GridFrame


class MainPanel(QFrame):

    def __init__(self, settings, parent=None):
        super(MainPanel, self).__init__(parent)
        self.settings = settings
        self.load_layout()

    def load_layout(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.top_widget = QFrame()
        self.top_layout = QHBoxLayout()
        self.top_widget.setLayout(self.top_layout)
        self.score_widget = ScoreFrame()
        self.top_layout.addWidget(self.score_widget)
        self.reset_widget = ResetFrame()
        self.top_layout.addWidget(self.reset_widget)
        self.timer_widget = TimerFrame()
        self.top_layout.addWidget(self.timer_widget)

        self.bottom_widget = QFrame()
        self.bottom_layout = QHBoxLayout()
        self.bottom_widget.setLayout(self.bottom_layout)
        self.grid_widget = GridFrame(self.settings)
        self.bottom_layout.addWidget(self.grid_widget)

        self.main_layout.addWidget(self.top_widget)
        self.main_layout.addWidget(self.bottom_widget)
