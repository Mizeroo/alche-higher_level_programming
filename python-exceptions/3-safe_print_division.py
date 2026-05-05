#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = none
    try:
        quotient = a / b
        print("Inside result: {}".format( quotient))
    except ZeroDivisionError:
        print("Inside result: None")
    finally:
        return quotient
