import subprocess

cmd = ["journalctl","-p","err","--since","1 hour ago"]

result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

output = result.stdout.strip()
if not output or output == "-- No entries --":
    print("No recent errors found")
    exit(0)
else:
    print(output)
    exit(1)

    
