import unittest
from PySide2 import (QtCore, QtCore, QtWidgets, QtTest)
from src.ui.resetUI import ResetButton
import src.model.GameStateController as gsc
import src.model.GameStates as states
import UsesQApplication
import time


class TestResetUI(UsesQApplication.UsesQApplication):

    def setUp(self):
        super(TestResetUI, self).setUp()
        self.reset_button = ResetButton()
        self.game_state = gsc.GameStateController()

    def test_normal_state(self):
        self.game_state.set_game_normal.emit()
        self.assertEqual(self.reset_button.state, states.NORMAL)
        self.assertEqual(self.game_state.game_over, False)

    def test_wait_state(self):
        self.game_state.set_game_wait.emit()
        self.assertEqual(self.reset_button.state, states.WAIT)
        self.assertEqual(self.game_state.game_over, False)

    def test_not_wait_state(self):
        self.game_state.set_game_wait.emit()
        self.assertEqual(self.reset_button.state, states.WAIT)
        self.assertEqual(self.game_state.game_over, False)
        self.game_state.set_game_not_waiting.emit()
        self.assertEqual(self.reset_button.state, states.NORMAL)
        self.game_state.set_game_won.emit()
        self.assertEqual(self.reset_button.state, states.WON)
        self.game_state.set_game_not_waiting.emit()
        self.assertEqual(self.reset_button.state, states.WON)

    def test_win_state(self):
        self.game_state.set_game_won.emit()
        self.assertEqual(self.reset_button.state, states.WON)
        self.assertEqual(self.game_state.game_over, True)

    def test_lost_state(self):
        self.game_state.set_game_lost.emit()
        self.assertEqual(self.reset_button.state, states.LOST)
        self.assertEqual(self.game_state.game_over, True)

    def test_reset_click(self):
        self.game_state.set_game_won.emit()
        self.assertEqual(self.reset_button.state, states.WON)
        self.assertEqual(self.game_state.game_over, True)
        QtTest.QTest.mouseClick(self.reset_button, QtCore.Qt.LeftButton)
        self.assertEqual(self.reset_button.state, states.NORMAL)
        self.assertEqual(self.game_state.game_over, False)


if __name__ == '__main__':
    unittest.main()
