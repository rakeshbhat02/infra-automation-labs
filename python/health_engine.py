import subprocess
import shutil
from pathlib import Path

STATE_FILE = Path.home() / ".disk_prev"
GROWTH_THRESHOLD = 5

total, used, free = shutil.disk_usage("/")
current = int((used / total) * 100)

if STATE_FILE.exists():
    previous = int(STATE_FILE.read_text().strip())
else:
    previous = current

growth = current - previous

STATE_FILE.write_text(str(current))

print(f"Disk growth: {growth}%")

if growth < GROWTH_THRESHOLD:
    print("System healthy")
    exit(0)

print("Disk growth abnormal, scanning logs...")

cmd = ["journalctl","-p","err","--since","1 hour ago"]
result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

output = result.stdout.strip()
if not output or output == "--No entries--":
    print("No errors found")
    exit(0)
else:
    print(output)
    exit(1)



