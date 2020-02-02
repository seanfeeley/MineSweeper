import unittest
from PySide2 import QtCore, QtCore, QtWidgets, QtTest
from src.ui.ScoreUI import ScoreFrame
import src.model.GameStateController as gsc
import UsesQApplication
import time


class TestScoreUI(UsesQApplication.UsesQApplication):
    MINES = 10

    def setUp(self):
        super(TestScoreUI, self).setUp()
        self.score_frame = ScoreFrame(self.MINES)
        self.game_state = gsc.GameStateController()

    def test_add_flag(self):
        self.assertEqual(self.score_frame.value, self.MINES)
        self.score_frame.flag_added()
        self.assertEqual(self.score_frame.value, self.MINES-1)

    def test_remove_flag(self):
        self.assertEqual(self.score_frame.value, self.MINES)
        self.score_frame.flag_removed()
        self.assertEqual(self.score_frame.value, self.MINES+1)

    def test_clear_flags(self):
        self.assertEqual(self.score_frame.value, self.MINES)
        self.score_frame.flag_removed()
        self.assertEqual(self.score_frame.value, self.MINES+1)
        self.score_frame.clear_flags()
        self.assertEqual(self.score_frame.value, self.MINES)


if __name__ == '__main__':
    unittest.main()
