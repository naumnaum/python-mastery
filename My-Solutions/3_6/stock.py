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
        if not value >= 0:
            raise ValueError("Price must be >= 0")
        self._price = value

    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1]}")
        if not value >= 0:
            raise ValueError("Shares must be >= 0")
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price
    
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
    def sell(self, nshares):
        assert isinstance(nshares, int)
        assert nshares < self.shares
        self.shares = self.shares - nshares

    def __repr__(self):
        return f"Stock('{self.name}', {self._shares}, {self._price})"
    
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == 
                                             (other.name, other.shares, other.price))


def print_portfolio(portfolio):
    assert isinstance(portfolio, list)
    for s in portfolio:
           assert isinstance(s, Stock)
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))