import sys
from PySide2.QtWidgets import (QFrame, QHBoxLayout, QVBoxLayout, QPushButton)
import src.model.GameStates as states
import src.model.MineFieldFunctions as MineField
import src.ui.tileUI as tileUI
import random
import src.model.GameStateController as gsc


class GridFrame(QFrame):

    def __init__(self, settings, parent=None):
        super(GridFrame, self).__init__(parent)
        self.settings = settings
        self.game_state = gsc.GameStateController()
        self.game_state.reveal_blanks.connect(self.reveal_blanks)
        self.game_state.set_game_reset.connect(self.reset)
        self.game_state.check_for_game_won.connect(self.check_for_win_state)

        self.tiles = []
        self.load_minefeild()
        self.load_layout()


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
        tile = tileUI.TileButton(row_index,
                                 column_index,
                                 self.minefield[row_index][column_index])
        return tile

    def reset(self):
        self.load_minefeild()

    def check_for_win_state(self):
        self.game_state.set_game_normal.emit()

    def reveal_blanks(self, row_index, column_index):
        blank_mines = MineField.get_blank_area([[row_index,
                                               column_index]],
                                               self.minefield)
        for blank_mine in blank_mines:
            row_index = blank_mine[0]
            column_index = blank_mine[1]
            tile = self.tiles[row_index][column_index]
            if tile.state != states.FLAGGED:
                tile.set_state(self.minefield[row_index][column_index])
