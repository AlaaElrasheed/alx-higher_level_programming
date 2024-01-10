#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = set(my_list)
    result = 0
    for i in add:
        result += i
    return result
