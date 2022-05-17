import os
import sys

# Print sys.argv
print(sys.argv)
path = sys.argv[1]

flist = os.listdir(path)

# This is a for loop
for f in flist:
    print(f)
print("Conflict?")
