import unittest
from datetime import datetime as datetime_, timedelta
from PySide2 import QtCore, QtCore, QtWidgets, QtTest
_instance = None


class UsesQApplication(unittest.TestCase):
    '''Helper class to provide QApplication instances'''

    qapplication = True

    def setUp(self):
        '''Creates the QApplication instance'''

        # Simple way of making instance a singleton
        super(UsesQApplication, self).setUp()
        global _instance
        if _instance is None:
            _instance = QtWidgets.QApplication([])

        self.app = _instance

    def tearDown(self):
        '''Deletes the reference owned by self'''
        del self.app
        super(UsesQApplication, self).tearDown()


@staticmethod
def qWait(t):
    end = datetime_.now() + timedelta(milliseconds=t)
    while datetime_.now() < end:
        QtWidgets.QApplication.processEvents()


QtTest.QTest.qWait = qWait
