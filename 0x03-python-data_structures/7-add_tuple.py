#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    return (tuple_a[0] + tuple_b[0] if len(tuple_a) >= 1 and len(tuple_b) >= 1 else 0,
            tuple_a[1] + tuple_b[1] if len(tuple_a) >= 2 and len(tuple_b) >= 2 else 0)

