import fileinput
import sys

for line in fileinput.input("opentrons.rb", inplace=True):
    if "    url" in line:
        line = f'    url "{sys.argv[1]}"\n'
    sys.stdout.write(line)
