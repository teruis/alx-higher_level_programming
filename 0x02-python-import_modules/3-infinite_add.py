#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    # Skip the first element (script name) and convert arguments to integers while summing them
    result = sum(int(arg) for arg in argv[1:])
    print(result)

