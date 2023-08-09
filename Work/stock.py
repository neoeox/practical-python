# stock.py

class Stock:
    """
     An instance of a stock holding consisting of name, shares, and price.
    """
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def __repr__(self):
        # return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
        # return f'Stock({self.name!s}, {self.shares!s}, {self.price!s})'
        return f'Stock({self.name!a}, {self.shares!a}, {self.price!a})'
    def cost(self):
        return self.shares * self.price
    def sell(self, nshares):
        self.shares -= nshares


class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor

    def panic(self):
        self.sell(self.shares)

    def cost(self):
        actual_cost = super().cost()
        return self.factor * actual_cost








