import sys, os
import json
import src.app as app
from PySide2.QtWidgets import (QApplication)

SETTINGS = "custom"  # custom/easy/normal/hard


def load_settings():
    settings = {}
    directory = os.path.dirname(os.path.realpath(__file__))
    with open("%s/settings/%s.json" % (directory, SETTINGS)) as json_file:
        setting = json.load(json_file)
    return settings


if __name__ == '__main__':
    application = QApplication(sys.argv)
    settings = load_settings()
    Main = app.Main(settings)
    Main.show()
    sys.exit(application.exec_())
