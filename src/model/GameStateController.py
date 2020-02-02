from PySide2.QtCore import QObject, Signal, Slot


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class GameStateController(QObject):
    game_over = False
    add_flag = Signal()
    remove_flag = Signal()
    set_game_lost = Signal()
    set_game_won = Signal()
    set_game_reset = Signal()
    set_game_wait = Signal()
    set_game_not_waiting = Signal()
    set_game_normal = Signal()
    check_for_game_won = Signal()
    reveal_blanks = Signal(int, int)
