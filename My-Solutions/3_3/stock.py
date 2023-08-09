import csv
from decimal import Decimal

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        assert isinstance(nshares, int)
        assert nshares < self.shares
        self.shares = self.shares - nshares
    
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)


def print_portfolio(portfolio):
    assert isinstance(portfolio, list)
    for s in portfolio:
           assert isinstance(s, Stock)
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))