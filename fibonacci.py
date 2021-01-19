#!/usr/bin/env python3

def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """
    """Use modulo operator to work with last 8 digits
    """
    if some_int > 100000000:
        return some_int % 100000000
    else:
        return some_int
    # raise NotImplementedError()


def optimized_fibonacci(f):
    if f == 0:
        return 0
    previous, current = (0, 1)
    for i in range(2, f+1):
        previous, current = (current, previous + current)
    return current
    # raise NotImplementedError()


class SummableSequence(object):
    fib_sequence = 0

    def __init__(self, *initial):
        fib_sequence = sum(initial)
        # raise NotImplementedError()

    def __call__(self, i):
        return optimized_fibonacci(i)
        # raise NotImplementedError()


if __name__ == "__main__":
    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))
