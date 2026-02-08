import shutil
from pathlib import Path

STATE_FILE = Path.home() / ".disk_prev"

total,used,free = shutil.disk_usage("/")

current = int((used/total)*100)

if STATE_FILE.exists():
    previous = int(STATE_FILE.read_text().strip())
else: 
    previous = current


growth = current - previous

print(f"Previous: {previous:.2f}%")
print(f"Current: {current:.2f}%")
print(f"Growth: {growth:.2f}%")

STATE_FILE.write_text(str(current))


if growth >= 5:
    print("Abnormal disk growth detected")
    exit(1)
else:
    print("Disk growth normal")
    exit(0)





