import sys
from PySide2.QtWidgets import QDialog, QHBoxLayout
import src.ui.mainPanelUI as mainPanelUI


class Main(QDialog):

    def __init__(self, settings, parent=None):
        super(Main, self).__init__(parent)
        self.setWindowTitle("Mine Sweeper")
        self.load_main_panel(settings)

    def load_main_panel(self, settings):
        self.main_panel = mainPanelUI.MainPanel(settings)
        layout = QHBoxLayout()
        layout.addWidget(self.main_panel)
        self.setLayout(layout)
