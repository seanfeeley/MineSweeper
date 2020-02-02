#!/bin/bash

copy_required_modules_here () {
  # echo "copy_required_modules_here"
  mkdir tcl
  mkdir tk
  cp -R /Library/Frameworks/Python.framework/Versions/3.8/lib/tcl* tcl/.
  cp -R /Library/Frameworks/Python.framework/Versions/3.8/lib/tk* tk/.
  cp -R /Library/Frameworks/Python.framework/Versions/3.8/lib/Tk* tk/.
  cp -R /Library/Frameworks/Python.framework/Versions/3.8/lib/Tk* tk/.
  cp -R $DIRECTORY/stylesheets .
  cp -R $DIRECTORY/images .
  cp -R $DIRECTORY/settings .
}

pyinstaller --windowed MineSweeper.py --icon=images/icon.icns
DIRECTORY=$(cd `dirname $0` && pwd)
cd $DIRECTORY/dist/MineSweeper
copy_required_modules_here
cd $DIRECTORY/dist/MineSweeper.app/Contents/MacOs
copy_required_modules_here

echo ''
echo 'Build Complete'
