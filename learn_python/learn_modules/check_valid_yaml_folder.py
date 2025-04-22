from validate_yaml_file import check_valid_yaml_file
import sys
import os

path = os.path.abspath(sys.argv[1])
# print(path)

# os.walk() returns three different values, root(current directory path), _(the list of subdirectories, we don't need this), files(the list of files in our path)
for root, _, files in os.walk(path):
    for file in files:
        if file.endswith(".pyc"):
            break
        check_valid_yaml_file(file)