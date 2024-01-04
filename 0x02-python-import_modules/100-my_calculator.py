#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operators = {'+': add, '-': sub, '*': mul, '/': div}
        if sys.argv[2] in operators:
            operator_symbol = sys.argv[2]
            result = operators[operator_symbol](a, b)
            print("{} {} {} = {}".format(a, operator_symbol, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
