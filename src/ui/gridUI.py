import sys
from PySide2.QtWidgets import (QFrame, QHBoxLayout, QVBoxLayout, QPushButton)
import src.model.MineFieldStates as states
import src.model.MineField as MineField
import src.ui.tileUI as tileUI
import random


class GridFrame(QFrame):

    def __init__(self, settings, parent=None):
        super(GridFrame, self).__init__(parent)
        self.settings = settings
        self.tiles = []
        self.load_layout()
        self.load_minefeild()

    def load_minefeild(self):
        self.minefield = MineField.generate_minefield(self.settings['rows'],
                                                      self.settings['columns'],
                                                      self.settings['mines'])


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
            tile = self.make_tile(row_index, column_index)
            self.tiles[row_index].append(tile)
            row_layout.addWidget(tile)
        self.main_layout.addWidget(row_widget)

    def make_tile(self, row_index, column_index):
        tile = tileUI.TileButton(row_index, column_index)
        tile.clicked.connect(lambda: self.tile_clicked(row_index,
                                                       column_index))
        tile.pressed.connect(lambda: self.tile_pressed(row_index,
                                                       column_index))
        return tile

    def reset(self):
        self.load_minefeild()
        self.set_all_tiles_hidden()

    def set_all_tiles_hidden(self):
        for row_index in range(0, len(self.tiles)):
            for column_index in range(0, len(self.tiles[row_index])):
                tile = self.tiles[row_index][column_index]
                tile.set_state(states.HIDDEN)
                tile.setEnabled(True)

    def disable_all_tiles(self):
        for row_index in range(0, len(self.tiles)):
            for column_index in range(0, len(self.tiles[row_index])):
                tile = self.tiles[row_index][column_index]
                tile.setEnabled(False)

    def tile_clicked(self, row_index, column_index):
        tile = self.tiles[row_index][column_index]
        tile_state = self.minefield[row_index][column_index]
        if tile_state == states.MINE:
            self.parent().parent().set_game_lost()
            self.disable_all_tiles()
        else:
            self.parent().parent().set_game_normal()
            tile.set_state(tile_state)
            if tile_state == states.BLANK:
                self.reveal_attached_blanks(row_index, column_index)
            self.check_if_game_won()

    def tile_pressed(self, row_index, column_index):
        tile = self.tiles[row_index][column_index]
        # tile_state = self.minefield[row_index][column_index]
        if tile.state == states.HIDDEN:
            self.parent().parent().tile_pressed()

    def reveal_mines(self):
        pass

    def reveal_attached_blanks(self, row_index, column_index):
        non_mines = MineField.get_attached_non_mines([[row_index,
                                                       column_index]],
                                                     self.minefield)
        for non_mine in non_mines:
            row_index = non_mine[0]
            column_index = non_mine[1]
            tile = self.tiles[row_index][column_index]
            tile.set_state(self.minefield[row_index][column_index])

    def check_if_game_won(self):
        pass
