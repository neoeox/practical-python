# test_stock.py

import unittest
import Work.stock3 as stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        self.assertEqual(s.cost, 49010.0)
        s.sell(50)
        self.assertEqual(s.shares, 100-50)
        # s.shares = 10.0
        # self.assertEqual(s.shares, 10)

if __name__ == '__main__':
    unittest.main()











