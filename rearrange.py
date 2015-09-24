import sys


def systemRearrange() -> str:
    newSet = set(sys.argv[1:])
    string = ' '.join(item for item in newSet)
    return string

if __name__ == "__main__":
    print(systemRearrange())
