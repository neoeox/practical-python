"""
5. 파이썬 객체의 내부 작동
https://wikidocs.net/84361
"""

stock = {
    'name' : 'GOOG',
    'shares' : 100,
    'price' : 490.1
}
print(type(stock), "\n", stock)

from Work.stock import Stock
s = Stock('GOOG', 100, 490.1)
s
print(s)
s.__dict__
print(s.__dict__)
s.__class__
print(s.__class__)
s.shares = 50
s.date = '2023/08/09'
print(s.__dict__)
del s.shares
print(s.__dict__)

#
class Dog:
    def noise(self):
        return 'Bark'
    def chase(self):
        return 'Chasing!'
class LoudDog(Dog):
    def noise(self):
        return super().noise().upper()

#
class Bike:
    def noise(self):
        return 'On Your Left'
    def pedal(self):
        return 'Pedaling!'
class LoudBike(Bike):
    def noise(self):
        return super().noise().upper()


#
from Work.stock import Stock
goog = Stock('GOOG', 100, 490.10)
ibm = Stock('IBM', 50, 91.23)

print(goog.__dict__)
print(ibm.__dict__)
goog.date = '6/11/2007'
print(goog.__dict__)
print(ibm.__dict__)
goog.__dict__['time'] = '9:45am'
print(goog.__dict__)
print(ibm.__dict__)
print(goog.cost())
print(ibm.cost())

print(Stock.__dict__['cost'])
print(Stock.__dict__['cost'](goog))
print(Stock.__dict__['cost'](ibm))
Stock.foo = 42
print(goog.foo)
print(ibm.foo)


class Foo(object):
    a = 13  # 클래스 변수
    def __init__(self, b):
        self.b = b  # 인스턴스 변수

f = Foo(10)
g = Foo(20)
print(f.a)
print(g.a)
print(f.b)
print(g.b)
Foo.a = 42
print(f.a)
print(g.a)


from Work.stock import Stock
goog = Stock('GOOG', 100, 490.10)
s = goog.sell
print(s)
s(25)
print(goog.shares)

print(s.__func__)
print(Stock.__dict__['sell'])
print(s.__self__)
s.__func__(s.__self__, 25)
print(goog.shares)

class Person(object):
    def __init__(self, name):
        self._name = 0
p = Person('Guido')
print(p._name)
p._name = 'Dave'
print(p._name)


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    def get_shares(self):
        return self._shares
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
s = Stock('GOOG', 100, 490.10)
print(s)
print(s.name, s._shares, s.price)
print(s.name, s.get_shares(), s.price)




class Stock:
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
    @property
    def cost(self):
        return self.shares * self.price
s = Stock('GOOG', 100, 490.10)
print(s)
print(s.name, s.shares, s._shares)
# s.shares = '100'  # TypeError: Expected an int
print(s.name, s.shares, s.price, s.cost)

s = Stock('IBM', 100, 385.15)
a = s.cost
print(s.cost)
print(s.shares)
print(s.name, s.shares, s.price, s.cost)
print(s.prices)


#
from Work.stock import Stock
s = Stock('GOOG', 100, 490.1)
print(s.shares, s.price, s.cost())

#
from Work.stock2 import Stock
s = Stock('GOOG', 100, 490.1)
print(s.shares, s._shares, s.price, s.cost)
# print(s.shares, s.price, s.cost())  # TypeError: 'float' object is not callable
s.shares = 50
print(s.shares, s.price, s.cost)
# s.shares = 'a lot'  # TypeError: Must be integer
print(s.name)
# s.blah = 42  # AttributeError: 'Stock' object has no attribute 'blah'

print(s.__dict__)  # AttributeError: 'Stock' object has no attribute '__dict__'. Did you mean: '__dir__'?









