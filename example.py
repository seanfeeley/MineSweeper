import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)


        self.button = QtWidgets.QPushButton("Click me!")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)


    def magic(self):
        self.button.setText(str(random.random()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
