import sys
from PySide2.QtWidgets import (QPushButton)
from PySide2.QtCore import (QSize, Qt)
from PySide2.QtGui import (QIcon, QMouseEvent)
import src.model.GameStates as states
import src.model.GameStateController as gsc
import random


class TileButton(QPushButton):

    tileWidth = 40
    iconWidth = 30

    def __init__(self, row, column, true_state, parent=None):
        super(TileButton, self).__init__(parent)
        self.game_state = gsc.GameStateController()
        self.game_state.set_game_lost.connect(self.game_lost)
        self.game_state.set_game_won.connect(self.game_won)
        self.row = row
        self.column = column
        self.set_state(states.HIDDEN)
        self.set_true_state(true_state)
        size = QSize(self.tileWidth, self.tileWidth)
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.clicked.connect(self.tile_clicked)

    def reset(self, state):
        self.true_state = state
        self.setEnabled(True)
        self.set_state(states.HIDDEN)

    def is_in_win_state(self):
        win_state = True
        if self.state in [states.MINE, states.DETONATED]:
            win_state = False
        elif self.state in [states.HIDDEN, states.FLAGGED]:
            win_state = self.true_state == states.MINE
        return win_state

    def set_true_state(self, true_state):
        self.true_state = true_state

    def set_state(self, state):
        self.state = state
        # self.clear_button()
        if self.state == states.MINE:
            self.show_mine()
        elif self.state == states.DETONATED:
            self.show_detonated()
            self.game_state.set_game_lost.emit()
        elif self.state == states.FLAGGED:
            self.show_flagged()
        elif self.state == states.HIDDEN:
            self.show_hidden()
        elif self.state == states.BLANK:
            self.show_blank()
        elif self.state >= states.HINT1:
            self.show_hint(self.state)
        self.refresh_stylesheet()

    def game_lost(self):
        self.setEnabled(False)
        if (self.true_state == states.MINE
           and self.state != states.DETONATED):
            self.show_mine()

    def game_won(self):
        self.setEnabled(False)
        if (self.true_state == states.MINE
           and self.state != states.FLAGGED):
            self.set_state(states.FLAGGED)
            self.game_state.add_flag.emit()

    def refresh_stylesheet(self):
        self.style().unpolish(self)
        self.style().polish(self)

    def clear_button(self):
        self.setIcon(QIcon())
        self.setText('')

    def show_mine(self):
        self.setObjectName("Mine")
        self.setIcon(QIcon('images/mine.png'))
        self.setIconSize(QSize(self.iconWidth, self.iconWidth))

    def show_detonated(self):
        self.setObjectName("Mine")
        self.setIcon(QIcon('images/detonatedMine.png'))
        self.setIconSize(QSize(self.iconWidth, self.iconWidth))

    def show_flagged(self):
        self.setObjectName("Flagged")
        self.setIcon(QIcon('images/flag.png'))
        self.setIconSize(QSize(self.iconWidth, self.iconWidth))

    def show_hidden(self):
        self.setObjectName("Hidden")
        self.clear_button()
        self.setIconSize(QSize(self.iconWidth, self.iconWidth))

    def show_blank(self):
        self.setObjectName("Blank")
        self.clear_button()
        self.setIconSize(QSize(self.iconWidth, self.iconWidth))

    def show_hint(self, state):
        self.setObjectName("Hint%d" % state)
        self.setText(str(state))

    def mousePressEvent(self, QMouseEvent):
        super(TileButton, self).mousePressEvent(QMouseEvent)
        if QMouseEvent.button() == Qt.RightButton:
            if self.state in [states.HIDDEN, states.FLAGGED]:
                self.toggle_flag()
        elif QMouseEvent.button() == Qt.LeftButton:
            if self.state == states.HIDDEN:
                self.game_state.set_game_wait.emit()

    def mouseReleaseEvent(self, QMouseEvent):
        super(TileButton, self).mouseReleaseEvent(QMouseEvent)
        if QMouseEvent.button() == Qt.LeftButton:
            self.game_state.set_game_not_waiting.emit()

    def toggle_flag(self):
        if self.state == states.FLAGGED:
            self.set_state(states.HIDDEN)
            self.game_state.remove_flag.emit()
        elif self.state == states.HIDDEN:
            self.set_state(states.FLAGGED)
            self.game_state.add_flag.emit()

    def tile_clicked(self):
        if self.state != states.FLAGGED:
            if self.true_state == states.MINE:
                self.set_state(states.DETONATED)
            elif self.true_state == states.BLANK:
                self.game_state.reveal_blanks.emit(self.row, self.column)
            else:
                self.set_state(self.true_state)

        self.game_state.check_for_game_won.emit()
