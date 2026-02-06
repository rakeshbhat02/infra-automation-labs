#!/bin/bash

echo "Running Disk Check..."
python3 disk_check.py --path /

echo ""
echo "Scanning logs..."


python3 log_scanner.py --file sample.log --keyword error

if [ $? -ne 0 ]; then
	echo ""
	echo "SYSTEM STATUS: ATTENTION REQUIRED"	
else
	echo ""
	echo "SYSTEM STATUS: HEALTHY"
fi


