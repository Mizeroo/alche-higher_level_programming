#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            print("{}".format(chr(ord(i) - 32)), end="\n" if i == str[-1] else "")
        else:
            print("{}".format(i), end="\n" if i == str[-1] else "")
