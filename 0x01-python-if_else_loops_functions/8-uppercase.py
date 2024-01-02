#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i.isalpha() and i.islower():
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
