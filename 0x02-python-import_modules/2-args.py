#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 0:
        print("{:d} argument.".format(len(sys.argv) - 1))
    if len(sys.argv) == 1:
        print("{:d} argument:".format(len(sys.argv) - 1))
    if len(sys.argv) > 1:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    for argv, argc in zip(sys.argv[1:], range(1, len(sys.argv))):
        print("{1}: {0}".format(argv, argc))
