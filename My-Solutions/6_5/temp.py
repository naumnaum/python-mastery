import inspect
from validate import Integer, ValidatedFunction
from stock import Stock

def add(x: Integer, y:Integer):
        return x + y

s = Stock('GOOG', 100, 490.1)
sell = Stock.sell()
print(add)
print(sell)
print(add)