import os
import sys

# Print sys.argv
print(sys.argv)
path = sys.argv[1]

flist = os.listdir(path)

print('\n'.join(flist))
