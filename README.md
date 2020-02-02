# Mine Sweeper

Simple Mine Sweeper game

## Getting Started

This python application has been developed in **Mac0SX Catalina (10.15.1)**

### Prerequisites

The following are required to run the application

```
Python 3.8.1
PySide 5.14.0
```

### Running the app

You can run the app from the terminal
```
> python3.8 MineSweeper.py
```

You can change the minefield size and number of mines in two ways. By passing arguments to the script:

```
> python3.8 MineSweeper.py --rows 9 --columns 9 --mines 10
```
OR you can default file here: **settings/defaults.json**
```
{"rows":9,"columns":9,"mines":10}
```

Rows must be between 3 and 20 inclusive.
Columns must be between 8 and 80 inclusive.
Mines must be below 300 or less than rows * columns.

## Running the tests

Tests can be run via from the terminal

```
> cd test/
> ./run.sh
```

## Authors

* **Sean Feeley**

## Acknowledgments

* Stylesheet https://github.com/Alexhuszagh/BreezeStyleSheets
* QtTesting Help https://stackoverflow.com/a/34745326/396772
