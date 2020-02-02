#!/bin/bash
TEST_DIRECTORY=$(cd `dirname $0` && pwd)
export PYTHONPATH=$PYTHONPATH:$TEST_DIRECTORY/../

# python3 TestScoreUI.py
# python3 TestResetUI.py
# python3 TestTimerUI.py
# python3 TestTileUI.py

python3 TestGridUI.py

# python3 TestMineFieldFunctions.py
