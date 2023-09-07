#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    # Get the number of arguments
    num_args = len(argv) - 1  

    if num_args == 0:
        print("0 argument.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    # Print the arguments
    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i]))
