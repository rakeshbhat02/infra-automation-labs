import shutil
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--path", default='/', help="Path to check disk usage")
args = parser.parse_args()

THRESHOLD=80    

total, used, free = shutil.disk_usage(args.path)

usage = int((used/total) * 100)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if usage > THRESHOLD:
    print(f"[{now}] WARNING: {args.path} usage crossed {THRESHOLD}%: {usage}%")
else:
    print(f"[{now}] {args.path} usage OK: {usage}%")

