# sample.py

from validate import PositiveInteger, Integer, validated, enforce
from logcall import logformat, logged

@enforce(x=Integer, y=Integer, return_=Integer)
def mul(x, y):
    return x*y

# @validated
# def add(x: Integer, y: Integer) -> Integer:
#     return x + y

# @validated
# def pow(x: Integer, y: PositiveInteger) -> Integer:
#     return x ** y

# @logformat('{func.__code__.co_filename}:{func.__name__}')
# def mul(x,y):
#     return x*y