import sys
from PySide2.QtWidgets import (QFrame, QHBoxLayout, QVBoxLayout, QPushButton)
import src.ui.tileUI as tileUI
import random

class GridFrame(QFrame):

    def __init__(self, settings, parent=None):
        super(GridFrame, self).__init__(parent)
        self.settings = settings
        self.tiles = []
        self.load_layout()

    def load_layout(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setMargin(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)
        self.load_tiles()

    def load_tiles(self):
        for row_index in range(0, self.settings['rows']):
            self.tiles.append([])
            self.make_row(row_index)

    def make_row(self, row_index):
        row_widget = QFrame()
        row_layout = QHBoxLayout()
        row_layout.setSpacing(0)
        row_layout.setMargin(0)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_widget.setLayout(row_layout)
        for column_index in range(0, self.settings['columns']):
            t = tileUI.TileButton("")
            self.tiles[row_index].append(t)
            row_layout.addWidget(t)
        self.main_layout.addWidget(row_widget)

    def reset(self):
        for tile_row in self.tiles:
            for tile in tile_row:
                tile.set_state(tileUI.HIDDEN)
