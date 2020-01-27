import sys, os
import json
import src.app as app
from PySide2.QtWidgets import (QApplication)
from PySide2.QtCore import (QFile, QTextStream)
import StyleSheets

SETTINGS = "easy"  # custom/easy/normal/hard


def load_settings():
    settings = {}
    directory = os.path.dirname(os.path.realpath(__file__))
    with open("%s/settings/%s.json" % (directory, SETTINGS)) as json_file:
        settings = json.load(json_file)
    return settings


def loadStyleSheet(app):
    directory = os.path.dirname(os.path.realpath(__file__))
    sshFile = "%s/StyleSheets/weird.qss" % (directory)
    with open(sshFile, "r") as fh:
        app.setStyleSheet(fh.read())


if __name__ == '__main__':
    application = QApplication(sys.argv)
    settings = load_settings()
    loadStyleSheet(application)
    Main = app.Main(settings)
    Main.show()
    sys.exit(application.exec_())
