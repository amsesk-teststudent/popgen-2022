import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", store = "action", default = ".", help = "The path you would like to list.")
parser.parse_args()

path = args.path

flist = os.listdir(path)

# This is a for loop
for f in flist:
    print(f)

    x=1
