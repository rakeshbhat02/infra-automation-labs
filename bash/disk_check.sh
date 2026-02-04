#!/bin/bash

THRESHOLD=80
USAGE=$(df / | tail -1 | awk '{print $5}' | tr -d "%")

if [ $USAGE -gt $THRESHOLD ]; then
   echo "WARNING: disk usage is above $THRESHOLD%"
else
   echo "Disk usage is OK: $USAGE%"
fi
