import csv

def read_portfolio(filename='../../Data/portfolio.csv'):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            name = str(row[0])
            shares = int(row[1])
            price = float(row[2])
            record = Stock(name=name, shares=shares, price=price)
            records.append(record)
    return records

def print_portfolio(portfolio):
    assert isinstance(portfolio, list)
    for s in portfolio:
           assert isinstance(s, Stock)
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

class Stock:
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
            