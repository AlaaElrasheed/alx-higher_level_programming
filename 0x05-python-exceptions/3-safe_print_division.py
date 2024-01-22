#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if b == 0:
            print("Inside result: {}".format(result))
            return None
        else:
            print("Inside result: {}".format(div))
            return div
