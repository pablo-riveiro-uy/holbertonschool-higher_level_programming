#!/usr/bin/python3
if __name__ == "__main__":
    decode = dir("./hidden_4")
    i = 0
    while decode[i]:
        if decode[i][0] != '_':
            print("{}".format(decode[i]))
        i += 1
