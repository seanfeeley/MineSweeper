
import unittest
from PySide2 import QtCore, QtCore, QtWidgets, QtTest
from src.ui.TileUI import TileButton
import src.model.GameStateController as gsc
import src.model.GameStates as states
import UsesQApplication
import time


class TestTileUI(UsesQApplication.UsesQApplication):
    def setUp(self):
        super(TestTileUI, self).setUp()
        self.tile = TileButton(0, 0, states.BLANK)
        self.game_state = gsc.GameStateController()

    def test_reset(self):
        for state in [states.BLANK, states.MINE, states.HINT1]:
            self.tile.reset(state)
            self.assertEqual(self.tile.true_state, state)
            self.assertEqual(self.tile.state, states.HIDDEN)

    def test_in_win_state(self):
        self.tile.reset(states.BLANK)
        self.assertEqual(self.tile.is_in_win_state(), False)

        self.tile.reset(states.MINE)
        self.assertEqual(self.tile.is_in_win_state(), True)

        self.tile.reset(states.MINE)
        self.tile.set_state(states.MINE)
        self.assertEqual(self.tile.is_in_win_state(), False)

        self.tile.reset(states.MINE)
        self.tile.set_state(states.DETONATED)
        self.assertEqual(self.tile.is_in_win_state(), False)

        self.tile.reset(states.HINT1)
        self.assertEqual(self.tile.is_in_win_state(), False)

        self.tile.reset(states.MINE)
        self.tile.set_state(states.HINT1)
        self.assertEqual(self.tile.is_in_win_state(), True)

    def test_set_true_state(self):
        self.tile.set_true_state(states.HINT3)
        self.assertEqual(self.tile.true_state, states.HINT3)

    def test_game_lost(self):
        self.tile.reset(states.BLANK)
        self.assertEqual(self.tile.isEnabled(), True)
        self.game_state.set_game_lost.emit()
        self.assertEqual(self.tile.state, states.HIDDEN)
        self.assertEqual(self.tile.isEnabled(), False)

        self.tile.reset(states.MINE)
        self.assertEqual(self.tile.isEnabled(), True)
        self.game_state.set_game_lost.emit()
        self.assertEqual(self.tile.state, states.MINE)
        self.assertEqual(self.tile.isEnabled(), False)

        self.tile.reset(states.HINT1)
        self.assertEqual(self.tile.isEnabled(), True)
        self.game_state.set_game_lost.emit()
        self.assertEqual(self.tile.state, states.HIDDEN)
        self.assertEqual(self.tile.isEnabled(), False)

    def test_game_won(self):
        self.tile.reset(states.BLANK)
        self.assertEqual(self.tile.isEnabled(), True)
        self.game_state.set_game_won.emit()
        self.assertEqual(self.tile.state, states.HIDDEN)
        self.assertEqual(self.tile.isEnabled(), False)

        self.tile.reset(states.MINE)
        self.assertEqual(self.tile.isEnabled(), True)
        self.game_state.set_game_won.emit()
        self.assertEqual(self.tile.state, states.FLAGGED)
        self.assertEqual(self.tile.isEnabled(), False)

        self.tile.reset(states.HINT1)
        self.assertEqual(self.tile.isEnabled(), True)
        self.game_state.set_game_won.emit()
        self.assertEqual(self.tile.state, states.HIDDEN)
        self.assertEqual(self.tile.isEnabled(), False)

    def test_show_hint_and_clear_button(self):
        self.tile.reset(states.HINT5)
        self.tile.set_state(states.HINT5)
        self.assertEqual("5", self.tile.text())
        self.tile.clear_button()
        self.assertEqual("", self.tile.text())

    def test_toggle_flag(self):
        self.tile.set_state(states.HIDDEN)
        self.tile.toggle_flag()
        self.assertEqual(self.tile.state, states.FLAGGED)
        self.tile.toggle_flag()
        self.assertEqual(self.tile.state, states.HIDDEN)

    def test_tile_left_mouse_press(self):
        self.tile.reset(states.BLANK)
        QtTest.QTest.mousePress(self.tile, QtCore.Qt.LeftButton)
        self.assertEqual(self.tile.state, states.HIDDEN)

    def test_tile_right_mouse_press(self):
        self.tile.reset(states.BLANK)
        QtTest.QTest.mousePress(self.tile, QtCore.Qt.RightButton)
        self.assertEqual(self.tile.state, states.FLAGGED)
        QtTest.QTest.mousePress(self.tile, QtCore.Qt.RightButton)
        self.assertEqual(self.tile.state, states.HIDDEN)

    def test_tile_click(self):
        self.tile.reset(states.BLANK)
        QtTest.QTest.mouseClick(self.tile, QtCore.Qt.LeftButton)
        self.assertEqual(self.tile.state, states.BLANK)

        self.tile.reset(states.HINT1)
        QtTest.QTest.mouseClick(self.tile, QtCore.Qt.LeftButton)
        self.assertEqual(self.tile.state, states.HINT1)

        self.tile.reset(states.MINE)
        QtTest.QTest.mouseClick(self.tile, QtCore.Qt.LeftButton)
        self.assertEqual(self.tile.state, states.DETONATED)


if __name__ == '__main__':
    unittest.main()
