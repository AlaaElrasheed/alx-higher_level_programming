#!/usr/bin/python3
def no_c(my_string):
    copy = list(my_string)
    for i in range(len(copy)):
        if copy[i] == 'c' or copy[i] == 'C':
            copy[i] = ''
    return ''.join(copy)
