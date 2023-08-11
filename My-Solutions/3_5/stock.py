import csv
from decimal import Decimal

class Stock:
    _types = (str, int, float)
    __slots__ = ('name', '_shares', '_price')
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        print(self._types)
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2]}")
        if value < 0:
            raise ValueError("Price must be >= 0")
        else: 
            self._price = value

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1]}")
        if value < 0:
            raise ValueError("Shares must be >= 0")
        else:
            self._shares = value
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


def print_portfolio(portfolio):
    for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))