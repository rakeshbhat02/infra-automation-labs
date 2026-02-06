#!/bin/bash

echo "Running Disk Check..."
USAGE=$(df / | tail -1 | awk '{print $5}' | tr -d '%')

echo "Disk Usage: $USAGE%"

if [ $USAGE -gt 80 ]; then
	echo ""
	echo "High disk usage detected. Scanning logs..."

	python3 log_scanner.py --file /var/log/messages --keyword error

	if [ $? -ne 0 ]; then
		echo ""
		echo "SYSTEM STATUS: ATTENTION REQUIRED"
	else
		echo ""
		echo "SYSTEM STATUS: DISK HIGH BUT NO ERRORS"
	fi
else
	echo ""
	echo "SYSTEM STATUS: HEALTHY"
fi


