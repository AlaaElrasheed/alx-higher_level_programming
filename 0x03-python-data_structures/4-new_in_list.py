#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx >= len(copy) or idx < 0:
        return copy
    else:
        copy[idx] = element
        return copy
