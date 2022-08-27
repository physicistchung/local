
import os
import argparse
from pydoc import describe

parser = argparse.ArgumentParser(description='Replace file names')
parser.add_argument('arg1', help='Location of the directory')

args = parser.parse_args()
input_path = args.arg1

for file in os.listdir(input_path):
    nfilename = file.replace("strings-to-be-replaced", "")
    print(nfilename)
    os.rename(os.path.join(input_path, file), os.path.join(input_path, nfilename))

