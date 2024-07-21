from sys import argv
from os import listdir
from os.path import isdir

def help():
    print("Usage: findme <file_name>...")

def find(path, target):
    found = False
    dirs = []
    for file in listdir(path):
        if file == target:
            found = True
            print(path+"/"+file)
        if isdir(path+"/"+file):
            dirs.append(file)
    for directory in dirs:
        found = find(path+"/"+directory, target) or found
    return found

def main():
    if len(argv) == 1:
        help()
    else:
        for file_name in argv[1:]:
            print(f"\033[94;1m{file_name}:\033[0m")
            if not find(".", file_name):
                print(f"'{file_name}' is not found.")

if __name__ == "__main__":
    main()