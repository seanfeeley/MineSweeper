import sys
from PySide2.QtWidgets import QWidget, QHBoxLayout
import src.ui.mainPanelUI as mainPanelUI


class Main(QWidget):

    def __init__(self, settings, parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle("Mine Sweeper")
        self.load_main_panel(settings)

    def load_main_panel(self, settings):
        self.main_panel = mainPanelUI.MainPanel(settings)
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setMargin(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.main_panel)
        self.setLayout(layout)
