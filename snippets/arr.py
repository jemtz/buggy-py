"""
The purpose of this snippet is to test your knowledge of
default arguments for functions in python and how they
can be misused
"""


def arr(bar=[]):
    bar = ['foo']
    bar.append("baz")
    return bar
