#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = a / b
    try:
        print("{} / {} = {}".format(a,b, quotient))
    except ValueError:
        pass
    finally:
        return quotient
