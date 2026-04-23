#!/usr/bin/python3
def uppercase(str):
    for i in str:
        end = "\n" if i == str[-1] else ""
        if ord('a') <= ord(i) <= ord('z'):
            print("{}".format(chr(ord(i) - 32)), end=end)
        else:
            print("{}".format(i), end=end)
