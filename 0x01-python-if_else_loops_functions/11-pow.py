#!/usr/bin/python3
def pow(a, b):
    c = 1
    d = b
    if b < 0:
        b *= -1
    for i in range(b):
        c *= a
    if d < 0:
        return float(1 / c)
    return c
