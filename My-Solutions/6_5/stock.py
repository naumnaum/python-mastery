from structure import Structure
from validate import ValidatedFunction, Integer

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        print("inside def sell: ", nshares)
        self.shares -= nshares
    # sell = ValidatedFunction(sell) 

Stock.create_init()