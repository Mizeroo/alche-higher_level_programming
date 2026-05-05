#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError("")
    except NameError as ne:
        print(ne)
