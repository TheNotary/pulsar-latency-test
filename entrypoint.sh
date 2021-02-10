#!/bin/bash
set -e

# This entry point runs two processes, a continuous java api build and a continuous serve of a springboot application
#cd /home/gradle/src
cd /app

# Spawn bash if we're booting in console mode
if [ "$1" = 'bash' ]; then
    /bin/bash
    exit
fi

if [ "$1" = 'consume' ]; then
  python consume.py
fi

if [ "$1" = 'produce' ]; then
  sleep 1
  echo "Executing produce.py"
  python produce.py
fi
