#!/usr/bin/python3
import hidden_4
hide = dir(hidden_4)
if __name__ == "__main__":
    for i in range(len(hide)):
        if hide[i][0] != '_':
            print(hide[i])
