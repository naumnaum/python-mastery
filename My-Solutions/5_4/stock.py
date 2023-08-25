import csv
from decimal import Decimal
# from validate import PositiveInteger, PositiveFloat, String
from typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
    
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
    def sell(self, nshares):
        if not isinstance(nshares, int):
            raise TypeError(f"Expected nshares to be {int.__name__}")
        if nshares > self.shares:
            raise ValueError("nshares to be sold must be less than "
                            "current number of shares")
        else:
            self.shares = self.shares - nshares

    def __repr__(self):
        return f"{type(self).__name__}('{self.name}', {self.shares}, {self.price})"
    
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == 
                                             (other.name, other.shares, other.price))


def print_portfolio(portfolio):
    for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))