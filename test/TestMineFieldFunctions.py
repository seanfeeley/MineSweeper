import unittest
from PySide2 import (QtCore, QtCore, QtWidgets, QtTest)
from src.ui.resetUI import ResetButton
import src.model.GameStateController as gsc
import src.model.MineFieldFunctions as mff
import src.model.GameStates as states
import UsesQApplication
import time
import copy

EMPTY_3X3 = [[states.BLANK, states.BLANK, states.BLANK],
             [states.BLANK, states.BLANK, states.BLANK],
             [states.BLANK, states.BLANK, states.BLANK]]

MINE1_3X3 = [[states.HINT1, states.MINE, states.HINT1],
             [states.HINT1, states.HINT1, states.HINT1],
             [states.BLANK, states.BLANK, states.BLANK]]

MINE2_3X3 = [[states.HINT1, states.MINE, states.HINT1],
             [states.HINT2, states.HINT2, states.HINT2],
             [states.HINT1, states.MINE, states.HINT1]]

MINE3_3X3 = [[states.MINE, states.MINE, states.HINT1],
             [states.HINT3, states.HINT3, states.HINT2],
             [states.HINT1, states.MINE, states.HINT1]]

MINE4_3X3 = [[states.MINE, states.MINE, states.MINE],
             [states.HINT3, states.HINT4, states.HINT3],
             [states.HINT1, states.MINE, states.HINT1]]

MINE5_3X3 = [[states.MINE, states.MINE, states.MINE],
             [states.HINT4, states.HINT5, states.HINT3],
             [states.MINE, states.MINE, states.HINT1]]

MINE6_3X3 = [[states.MINE, states.MINE, states.MINE],
             [states.HINT4, states.HINT6, states.HINT4],
             [states.MINE, states.MINE, states.MINE]]

MINE7_3X3 = [[states.MINE, states.MINE, states.MINE],
             [states.MINE, states.HINT7, states.HINT4],
             [states.MINE, states.MINE, states.MINE]]

MINE8_3X3 = [[states.MINE, states.MINE, states.MINE],
             [states.MINE, states.HINT8, states.MINE],
             [states.MINE, states.MINE, states.MINE]]

MINE9_3X3 = [[states.MINE, states.MINE, states.MINE],
             [states.MINE, states.MINE, states.MINE],
             [states.MINE, states.MINE, states.MINE]]

EMPTY_3X2 = [[states.BLANK, states.BLANK],
             [states.BLANK, states.BLANK],
             [states.BLANK, states.BLANK]]

EMPTY_2X3 = [[states.BLANK, states.BLANK, states.BLANK],
             [states.BLANK, states.BLANK, states.BLANK]]

CONNECTED_4X4 = [[states.BLANK, states.BLANK, states.HINT1, states.MINE],
                 [states.BLANK, states.BLANK, states.HINT1, states.HINT1],
                 [states.HINT1, states.HINT1, states.BLANK, states.BLANK],
                 [states.MINE, states.HINT1, states.BLANK, states.BLANK]]

CONNECTED_4X4_BLANK_AREA = [[0, 0],
                            [0, 1],
                            [0, 2],
                            [1, 0],
                            [1, 1],
                            [1, 2],
                            [1, 3],
                            [2, 0],
                            [2, 1],
                            [2, 2],
                            [2, 3],
                            [3, 1],
                            [3, 2],
                            [3, 3]]

DISCONNECTED_4X4 = [[states.BLANK, states.BLANK, states.HINT1, states.HINT1],
                    [states.BLANK, states.BLANK, states.HINT1, states.MINE],
                    [states.HINT1, states.HINT1, states.HINT1, states.HINT1],
                    [states.MINE, states.HINT1, states.BLANK, states.BLANK]]

DISCONNECTED_4X4_BLANK_AREA_1 = [[0, 0],
                                 [0, 1],
                                 [0, 2],
                                 [1, 0],
                                 [1, 1],
                                 [1, 2],
                                 [2, 0],
                                 [2, 1],
                                 [2, 2]]

DISCONNECTED_4X4_BLANK_AREA_2 = [[2, 1],
                                 [2, 2],
                                 [2, 3],
                                 [3, 1],
                                 [3, 2],
                                 [3, 3]]


ATTACHED_CORDS_3x3_1x1 = [[0, 0],
                          [0, 1],
                          [0, 2],
                          [1, 0],
                          [1, 2],
                          [2, 0],
                          [2, 1],
                          [2, 2]]

ATTACHED_CORDS_3x3_0x1 = [[0, 0],
                          [0, 2],
                          [1, 0],
                          [1, 1],
                          [1, 2]]

ATTACHED_CORDS_3x3_0x0 = [[0, 1],
                          [1, 1],
                          [1, 0]]

class TestMineFieldFunctions(UsesQApplication.UsesQApplication):

    def setUp(self):
        super(TestMineFieldFunctions, self).setUp()

    def test_generate_empty_minefield(self):
        self.assertEqual(mff.generate_empty_minefield(3, 3), EMPTY_3X3)
        self.assertEqual(mff.generate_empty_minefield(3, 2), EMPTY_3X2)
        self.assertEqual(mff.generate_empty_minefield(2, 3), EMPTY_2X3)

    def test_add_mines_to_minefield(self):
        minefield = mff.generate_empty_minefield(3, 3)
        self.assertEqual(mff.add_mines_to_minefield(9, minefield), MINE9_3X3)
        minefield = mff.generate_empty_minefield(1, 10)
        minefield = mff.add_mines_to_minefield(1, minefield)

        # Asset that in the 1 row there is one MINE and at least one HINT1
        minefield[0].sort()
        self.assertEqual(minefield[0][0], states.MINE)
        self.assertEqual(minefield[0][1], states.BLANK)
        self.assertEqual(minefield[0][-1], states.HINT1)

    def test_generate_minefield(self):
        for rows, columns in [[3, 3], [3, 2], [2, 3]]:
            minefield = mff.generate_empty_minefield(rows, columns)
            self.assertEqual(len(minefield), rows)
            for row in minefield:
                self.assertEqual(len(row), columns)

    def test_add_mine_to_minefield(self):
        minefield = mff.generate_empty_minefield(3, 3)
        mff.add_mine_to_minefield(0, 1, minefield)
        self.assertEqual(minefield, MINE1_3X3)
        mff.add_mine_to_minefield(2, 1, minefield)
        self.assertEqual(minefield, MINE2_3X3)
        mff.add_mine_to_minefield(0, 0, minefield)
        self.assertEqual(minefield, MINE3_3X3)
        mff.add_mine_to_minefield(0, 2, minefield)
        self.assertEqual(minefield, MINE4_3X3)
        mff.add_mine_to_minefield(2, 0, minefield)
        self.assertEqual(minefield, MINE5_3X3)
        mff.add_mine_to_minefield(2, 2, minefield)
        self.assertEqual(minefield, MINE6_3X3)
        mff.add_mine_to_minefield(1, 0, minefield)
        self.assertEqual(minefield, MINE7_3X3)
        mff.add_mine_to_minefield(1, 2, minefield)
        self.assertEqual(minefield, MINE8_3X3)
        mff.add_mine_to_minefield(1, 1, minefield)
        self.assertEqual(minefield, MINE9_3X3)

    def test_increase_hint(self):
        minefield = mff.generate_empty_minefield(3, 3)
        minefield[1][1] = states.BLANK
        mff.increase_hint(1, 1, minefield)
        self.assertEqual(minefield[1][1], states.HINT1)
        mff.increase_hint(1, 1, minefield)
        self.assertEqual(minefield[1][1], states.HINT2)
        mff.increase_hint(1, 1, minefield)
        self.assertEqual(minefield[1][1], states.HINT3)
        mff.increase_hint(1, 1, minefield)
        self.assertEqual(minefield[1][1], states.HINT4)
        mff.increase_hint(1, 1, minefield)
        self.assertEqual(minefield[1][1], states.HINT5)
        mff.increase_hint(1, 1, minefield)
        self.assertEqual(minefield[1][1], states.HINT6)
        mff.increase_hint(1, 1, minefield)
        self.assertEqual(minefield[1][1], states.HINT7)
        mff.increase_hint(1, 1, minefield)
        self.assertEqual(minefield[1][1], states.HINT8)

    def test_get_blank_area(self):
        CONNECTED_4X4_BLANK_AREA.sort()
        blank_area = mff.get_blank_area([[0, 0]], CONNECTED_4X4)
        blank_area.sort()
        self.assertEqual(blank_area, CONNECTED_4X4_BLANK_AREA)
        blank_area = mff.get_blank_area([[3, 3]], CONNECTED_4X4)
        blank_area.sort()
        self.assertEqual(blank_area, CONNECTED_4X4_BLANK_AREA)

        DISCONNECTED_4X4_BLANK_AREA_1.sort()
        DISCONNECTED_4X4_BLANK_AREA_2.sort()
        blank_area = mff.get_blank_area([[0, 0]], DISCONNECTED_4X4)
        blank_area.sort()
        self.assertEqual(blank_area, DISCONNECTED_4X4_BLANK_AREA_1)
        blank_area = mff.get_blank_area([[3, 3]], DISCONNECTED_4X4)
        blank_area.sort()
        self.assertEqual(blank_area, DISCONNECTED_4X4_BLANK_AREA_2)

    def test_get_attached_coords(self):
        self.assertEqual(sorted(mff.get_attached_coords(0, 0, EMPTY_3X3)),
                         sorted(ATTACHED_CORDS_3x3_0x0))
        self.assertEqual(sorted(mff.get_attached_coords(1, 1, EMPTY_3X3)),
                         sorted(ATTACHED_CORDS_3x3_1x1))
        self.assertEqual(sorted(mff.get_attached_coords(0, 1, EMPTY_3X3)),
                         sorted(ATTACHED_CORDS_3x3_0x1))


if __name__ == '__main__':
    unittest.main()
