import sys
import os
import json
import src.app as app
from PySide2.QtWidgets import (QApplication)
from PySide2.QtCore import (QFile, QTextStream)
import StyleSheets

# SETTINGS = "hard"  # custom/easy/normal/hard
STYLESHEETS = ["light", "MineSweeper"]


def load_settings(level):
    settings = {}
    directory = os.path.dirname(os.path.realpath(__file__))
    with open("%s/settings/%s.json" % (directory, level)) as json_file:
        settings = json.load(json_file)
    return settings


def loadStyleSheet(app):
    directory = os.path.dirname(os.path.realpath(__file__))
    stylesheet_data = ""
    for stylesheet in STYLESHEETS:
        sshFile = "%s/StyleSheets/%s.qss" % (directory, stylesheet)
        with open(sshFile, "r") as fh:
            stylesheet_data += fh.read()
    app.setStyleSheet(stylesheet_data)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    settings = load_settings(sys.argv[1])
    loadStyleSheet(application)
    Main = app.Main(settings)
    Main.show()
    Main.setFixedSize(Main.size())
    sys.exit(application.exec_())
