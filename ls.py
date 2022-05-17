import os
import sys

# Print sys.argv
print(sys.argv)
path = sys.argv[1]

flist = os.listdir(path)

for f in flist:
    print(f)
