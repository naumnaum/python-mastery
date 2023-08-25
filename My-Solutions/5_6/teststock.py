import unittest
import stock
from stock import Stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
    
    def test_create_keyargs(self):
        s = Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)        
    
    def test_sell(self):
        nshares_init = 100
        nshares_tosell = 10
        s = Stock('GOOG', nshares_init, 490.1)
        s.sell(nshares_tosell)
        self.assertEqual(s.shares, nshares_init - nshares_tosell)

    def test_cost(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, s.shares * s.price)

    def test_from_row(self):
        row = ['GOOG', '100', '490.1']
        s = Stock.from_row(row)
        self.assertEqual(s.name, str(row[0]))
        self.assertEqual(s.shares, int(row[1]))
        self.assertEqual(s.price, float(row[2]))

    def test_repr(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(str(s), f"{type(s).__name__}('{s.name}', {s.shares}, {s.price})")

    def test_eq(self):
        s1 = Stock('GOOG', 100, 490.1)
        s2 = Stock('GOOG', 100, 490.1)
        s3 = Stock('AAPL', 50, 231.1)
        self.assertEqual(s1==s2, True)
        self.assertEqual(s1==s3, False)

    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
             s.shares = '50'

    def test_negative_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
             s.shares = -50

    def test_bad_price(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
             s.price = '50.1'

    def test_negative_price(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
             s.price = -490.1

    def test_non_exist_attr(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
             s.share = 'spaam'

if __name__ == '__main__':
    unittest.main()
