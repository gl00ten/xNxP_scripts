#!/bin/bash
# click_spam_mouse.sh
# ARCHIVED: Perfectly dumb.
# Hardcoded screen coordinates + xdotool loop to click 3000 times.
# No arguments, no purpose beyond "spam click here". Zero reusability.
# Originally: scripts/clickABunchOfTimes.bash

for i in {1..3000}; do
  xdotool mousemove 918 584 click 1 &
  sleep 0.1
done


