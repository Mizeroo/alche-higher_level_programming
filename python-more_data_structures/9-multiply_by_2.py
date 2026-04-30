#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i in a_dictionary:
        new_dictionary.append(map(lambda x: x*2, a_dictionary))
    return(new_dictionary)
