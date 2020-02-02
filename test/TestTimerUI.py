'''Tests for TimerUI'''
import unittest
from PySide2 import QtCore, QtCore, QtWidgets, QtTest
from src.ui.timerUI import TimerFrame
import src.model.GameStateController as gsc
import UsesQApplication
import time


class TestTimerUI(UsesQApplication.UsesQApplication):
    def setUp(self):
        super(TestTimerUI, self).setUp()
        self.timer_frame = TimerFrame()
        self.game_state = gsc.GameStateController()

    def tearDown(self):
        super(TestTimerUI, self).tearDown()

    def test_timer_starts_at_0(self):
        value = self.timer_frame.value
        self.assertEqual(self.timer_frame.value, 0)

    def test_timer_starts_when_game_does(self):
        self.assertEqual(self.timer_frame.timer.isActive(), False)
        self.game_state.set_game_normal.emit()
        self.assertEqual(self.timer_frame.timer.isActive(), True)

    def test_timer_freezes_when_game_won(self):
        self.assertEqual(self.timer_frame.timer.isActive(), False)
        self.game_state.set_game_normal.emit()
        self.assertEqual(self.timer_frame.timer.isActive(), True)
        test_timer_value = 10
        self.timer_frame.value = test_timer_value
        self.game_state.set_game_won.emit()
        self.assertEqual(self.timer_frame.timer.isActive(), False)
        self.assertEqual(self.timer_frame.value, test_timer_value)

    def test_timer_freezes_when_game_lost(self):
        self.assertEqual(self.timer_frame.timer.isActive(), False)
        self.game_state.set_game_normal.emit()
        self.assertEqual(self.timer_frame.timer.isActive(), True)
        test_timer_value = 10
        self.timer_frame.value = test_timer_value
        self.game_state.set_game_lost.emit()
        self.assertEqual(self.timer_frame.timer.isActive(), False)
        self.assertEqual(self.timer_frame.value, test_timer_value)

    def test_timer_resets_when_game_restarts(self):
        self.assertEqual(self.timer_frame.timer.isActive(), False)
        self.game_state.set_game_normal.emit()
        self.assertEqual(self.timer_frame.timer.isActive(), True)
        test_timer_value = 10
        self.timer_frame.value = test_timer_value
        self.game_state.set_game_won.emit()
        self.assertEqual(self.timer_frame.timer.isActive(), False)
        self.game_state.set_game_reset.emit()
        self.assertEqual(self.timer_frame.timer.isActive(), False)
        self.assertEqual(self.timer_frame.value, 0)

    def test_value_increments_each_second(self):
        value = 10
        self.game_state.set_game_normal.emit()
        self.assertEqual(self.timer_frame.timer.isActive(), True)
        self.timer_frame.value = value
        QtTest.QTest.qWait(1100)
        self.assertEqual(self.timer_frame.value, value+1)
        QtTest.QTest.qWait(1100)
        self.assertEqual(self.timer_frame.value, value+2)
        QtTest.QTest.qWait(1100)
        self.assertEqual(self.timer_frame.value, value+3)

    def test_timer_stops_at_max_value(self):
        value = self.timer_frame.MAX_VALUE
        self.game_state.set_game_normal.emit()
        self.assertEqual(self.timer_frame.timer.isActive(), True)
        self.timer_frame.value = value - 3
        QtTest.QTest.qWait(1100)
        self.assertEqual(self.timer_frame.value, value - 2)
        QtTest.QTest.qWait(1100)
        self.assertEqual(self.timer_frame.value, value - 1)
        QtTest.QTest.qWait(1100)
        self.assertEqual(self.timer_frame.value, value)
        QtTest.QTest.qWait(1100)
        self.assertEqual(self.timer_frame.value, value)
        self.assertEqual(self.timer_frame.timer.isActive(), False)


if __name__ == '__main__':
    unittest.main()
