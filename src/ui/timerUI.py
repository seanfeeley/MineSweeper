import sys
from src.ui.NumberDisplayUI import NumberDisplay
from PySide2.QtCore import QTimer
import src.model.GameStateController as gsc


class TimerFrame(NumberDisplay):
    ONE_SECOND = 1000

    def __init__(self, parent=None):
        super(TimerFrame, self).__init__(parent)
        self.create_timer()
        self.game_state = gsc.GameStateController()
        self.game_state.set_game_lost.connect(self.pause_timer)
        self.game_state.set_game_won.connect(self.pause_timer)
        self.game_state.set_game_normal.connect(self.start_timer)
        self.game_state.set_game_reset.connect(self.stop_timer)

    def create_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.one_second_passed)

    def restart_timer(self):
        self.value = 0
        self.timer.start(self.ONE_SECOND)

    def one_second_passed(self):
        self.increment_timer()
        self.refresh_display()

    def increment_timer(self):
        if self.value == self.MAX_VALUE:
            self.game_state.set_game_lost.emit()
        else:
            self.value += 1


    def pause_timer(self):
        self.timer.stop()

    def stop_timer(self):
        self.timer.stop()
        self.value = 0
        self.refresh_display()

    def start_timer(self):
        if self.value == 0 and not self.timer.isActive():
            self.restart_timer()
