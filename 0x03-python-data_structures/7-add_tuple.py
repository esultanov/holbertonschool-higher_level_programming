#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a) + [0] * 2
    list_b = list(tuple_b) + [0] * 2
    list_c = []
    for x, y in zip(list_a, list_b):
        list_c.append(x + y)
    return tuple(list_c[0:2])
