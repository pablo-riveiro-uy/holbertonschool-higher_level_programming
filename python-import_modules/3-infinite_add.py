#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    for i in range(1, len(sys.argv)):
        if int(sys.argv[i]) < 0:
            res = res - int(sys.argv[i]) * -1
        else:
            res += int(sys.argv[i])
    print(res)
