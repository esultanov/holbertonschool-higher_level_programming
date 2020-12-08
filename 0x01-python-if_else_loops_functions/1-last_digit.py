#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
t = number % 10 if number > 0 else int(repr(number)[-1]) * -1
if t == 0:
    print("Last digit of {} is 0 and is 0".format(number))
elif t < 6:
    print("Last digit of {} is {} and is less than \
6 and not 0".format(number, t))
else:
    print("Last digit of {} is {} and is greater than 5".format(number, t))
