# sample.py

from validate import PositiveInteger, Integer, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: PositiveInteger) -> Integer:
    return x ** y