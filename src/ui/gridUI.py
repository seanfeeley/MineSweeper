import sys
from PySide2.QtWidgets import (QFrame, QHBoxLayout)
from src.ui.tileUI import TileButton


class GridFrame(QFrame):

    def __init__(self, settings, parent=None):
        super(GridFrame, self).__init__(parent)
        self.settings = settings
        print(self.settings)
        self.tiles = []
        self.load_layout()

    def load_layout(self):
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        self.load_tiles()

    def load_tiles(self):
        for row_index in range(0, self.settings['rows']):
            self.make_row(row_index)

    def make_row(self, row_index):
        row_widget = QFrame()
        row_layout = QHBoxLayout()
        row_widget.setLayout(row_layout)
        for column_index in range(0, self.settings['columns']):
            tile = self.make_tile(row_index, column_index)
            row_layout.addWidget(tile)
        self.main_layout.addWidget(row_widget)

    def make_tile(self, row, column):
        has_mine = self.is_there_a_mine(row, column)
        tile = TileButton(row, column, has_mine)
        return tile

    def is_there_a_mine(self, row, column):
        return False
