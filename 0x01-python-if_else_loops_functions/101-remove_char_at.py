#!/usr/bin/python3
def remove_char_at(str, n):
    copy = str[0:n] + str[n+1:]
    if n >= 0:
        return copy
    else:
        return str
