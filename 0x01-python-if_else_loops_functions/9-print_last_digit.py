#!/usr/bin/python3
def print_last_digit(number):
    last = repr(int(number))[-1]
    print("{}".format(last), end="")
    return last
