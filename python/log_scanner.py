import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--file", required=True)
parser.add_argument("--keyword", required=True)

args = parser.parse_args()

found = False
with open(args.file) as f:
    for line in f:
        if args.keyword.lower() in line.lower():
            print(line.strip())
            found = True

if found:
    sys.exit(1)
else:
    sys.exit(0)


