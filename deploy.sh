#!/bin/bash

SCRIPT="manage.py"
python $SCRIPT assets clean
python $SCRIPT assets build
python $SCRIPT collectstatic --noinput
python $SCRIPT syncmedia

echo "Done."

