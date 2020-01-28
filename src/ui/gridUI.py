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
        self.is_game_over = False

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
        tile = tileUI.TileButton(row_index, column_index, parent=self)
        tile.clicked.connect(lambda: self.tile_clicked(row_index,
                                                       column_index))
        # tile.pressed.connect(lambda: self.tile_pressed(row_index,
        #                                                column_index))
        return tile

    def reset(self):
        self.is_game_over = False
        self.load_minefeild()
        self.run_function_on_all_tiles(self.reset_game_for_tile)

    def run_function_on_all_tiles(self, function):
        for row_index in range(0, len(self.tiles)):
            for column_index in range(0, len(self.tiles[row_index])):
                function(row_index, column_index)

    def reset_game_for_tile(self, row_index, column_index):
        tile = self.tiles[row_index][column_index]
        tile.set_state(states.HIDDEN)
        tile.setEnabled(True)

    def end_game_for_tile(self, row_index, column_index):
        tile = self.tiles[row_index][column_index]
        true_state = self.minefield[row_index][column_index]
        if (true_state == states.MINE and tile.state != states.DETONATED):
            tile.set_state(states.MINE)
        elif tile.state == states.HIDDEN:
            tile.setEnabled(False)

    def tile_clicked(self, row_index, column_index):
        tile = self.tiles[row_index][column_index]
        tile_state = self.minefield[row_index][column_index]
        if not self.is_game_over and tile.state != states.FLAGGED:
            if tile_state == states.MINE:
                tile.set_state(states.DETONATED)
                self.run_function_on_all_tiles(self.end_game_for_tile)
                self.parent().parent().set_game_status_lost()
            else:
                self.parent().parent().set_game_status_normal()
                tile.set_state(tile_state)
                if tile_state == states.BLANK:
                    self.reveal_attached_blanks(row_index, column_index)

    def reveal_attached_blanks(self, row_index, column_index):
        blank_mines = MineField.get_blank_area([[row_index,
                                               column_index]],
                                               self.minefield)
        for blank_mine in blank_mines:
            row_index = blank_mine[0]
            column_index = blank_mine[1]
            tile = self.tiles[row_index][column_index]
            if tile.state != states.FLAGGED:
                tile.set_state(self.minefield[row_index][column_index])
