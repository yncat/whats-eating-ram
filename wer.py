import argparse
import csv
import platform
import subprocess
import sys

plat = platform.system()
if plat != 'Windows':
    sys.stderr.write(
        "Platform %s is not supported. This program works on Windows only.\n" % plat)
    sys.exit(1)

parser = argparse.ArgumentParser(
    description='Show processes eating ram the most')
parser.add_argument('--count', type=int,
                    help='Number of processes to show (default 5)', default=5)
args = parser.parse_args()

print("Top %d" % args.count)
proc = subprocess.run("tasklist /nh /fo csv", capture_output=True, text=True)
if proc.returncode != 0:
    sys.stderr.write(
        "tasklist command exited with return code %d\n" % proc.returncode)
    sys.exit(1)
# end error
processes = []
for line in csv.reader(proc.stdout.split("\n")):
    if len(line) < 4:
        continue
    # end avoid errors
    mem = int(line[4].rstrip(' K').replace(',', ''))
    processes.append((line[0], mem))
# end parse

processes.sort(key=lambda x: x[1], reverse=True)
print("\n".join(["%s: %sK" % (x[0], x[1]) for x in processes[0:args.count]]))
