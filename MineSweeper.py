import sys
import os
import json
import src.app as app
import src.model.ResourceLoader as ResourceLoader
from PySide2.QtWidgets import (QApplication)
from PySide2.QtCore import (QFile, QTextStream)
import pprint
import argparse

STYLESHEETS = ["light", "MineSweeper"]

MIN_ROWS = 3
MAX_ROWS = 20

MIN_COLUMNS = 8
MAX_COLUMNS = 30

MIN_MINES = 1
MAX_MINES = 300


def load_defaults():
    settings = {}
    directory = os.path.dirname(os.path.realpath(__file__))
    defaults_json = ResourceLoader.resource_path("settings/default.json")
    with open(defaults_json) as json_file:
        settings = json.load(json_file)
    return settings


def get_valid_settings_str(settings):
    valid_str = ""
    if settings['rows'] < MIN_ROWS:
        valid_str += "\nrows must be over or equal to %s" % MIN_ROWS
    if settings['rows'] > MAX_ROWS:
        valid_str += "\nrows must be unde or equal to %s" % MAX_ROWS
    if settings['columns'] < MIN_COLUMNS:
        valid_str += "\ncolumns must be over or equal to %s" % MIN_COLUMNS
    if settings['columns'] > MAX_COLUMNS:
        valid_str += "\ncolumns must be under or equal to %s" % MAX_COLUMNS
    if settings['mines'] < MIN_MINES:
        valid_str += "\nmines must be over or equal to %s" % MIN_MINES
    if settings['mines'] > MAX_MINES:
        valid_str += "\nmines must be under or equal to %s" % MAX_MINES
    if settings['mines'] > settings['rows'] * settings['columns']:
        valid_str += "\nToo many mines for the grid size"
    return valid_str


def loadStyleSheet(app):
    directory = os.path.dirname(os.path.realpath(__file__))
    stylesheet_data = ""
    for stylesheet in STYLESHEETS:
        sshFile = ResourceLoader.resource_path("stylesheets/%s.qss" % (stylesheet))
        with open(sshFile, "r") as fh:
            stylesheet_data += fh.read()
    app.setStyleSheet(stylesheet_data)

def main(settings):
    application = QApplication(sys.argv)
    # settings = load_settings(settings)
    valid_str = get_valid_settings_str(settings)
    if valid_str != "":
        print("Invalid Settings:")
        pprint.pprint(settings)
        print(valid_str)
    else:
        loadStyleSheet(application)
        Main = app.Main(settings)
        Main.show()
        Main.setFixedSize(Main.size())
        sys.exit(application.exec_())


if __name__ == '__main__':
    defaults = load_defaults()
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows",
                        "-r",
                        default=defaults['rows'],
                        type=int)
    parser.add_argument("--columns",
                        "-c",
                        default=defaults['columns'],
                        type=int)
    parser.add_argument("--mines",
                        "-m",
                        default=defaults['mines'],
                        type=int)
    args = parser.parse_args()
    main({'rows': args.rows,
          'columns': args.columns,
          'mines': args.mines})
