"""
ch07.고급주제
"""
import time


#
def avg(x, *more):
    return float(x + sum(more)) / (1 + len(more))
print(avg(10, 11))
print(avg(3, 4, 5))
print(avg(1, 2, 3, 4, 5, 6))

data = ('GOOG', 100, 490.1)
from Work.stock2 import Stock
# s = Stock(data)  # TypeError: Stock.__init__() missing 2 required positional arguments: 'shares' and 'price'
s = Stock(*data)
print(s)
data = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
s = Stock(**data)
print(s)


s = [10, 1, 7, 3]
s.sort()
print(s)
s.sort(reverse=True)
print(s)

def add(x, y):
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
a = add(3, 4)
print(a)
print(a())


import time
def after(seconds, func):
    time.sleep(seconds)
    func()
def greeting():
    print('Hello Guido')
after(3, greeting)


def add(x, y):
    def do_add():
        print(f'Adding {x} + {y} -> {x + y}')
    return do_add

def after(seconds, func):
    time.sleep(seconds)
    func()

after(3, add(2, 3))


from Work.typedproperty import typedproperty
class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stock('IBM', 50, 91.1)
print(s.name)
print(s.shares)
# s.shares = '100'  # TypeError: Expected <class 'int'>

#
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

logged_add = logged(add)
logged_sub = logged(sub)
print(logged_add(3, 4))
print(logged_sub(3, 4))

#
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
@logged
def add(x, y):
    return x + y
@logged
def sub(x, y):
    return x - y

logged_add = logged(add)
logged_sub = logged(sub)
print(logged_add(3, 4))
print(logged_sub(3, 4))

def add(x, y):
    return x + y
print(add.__name__)
print(add.__module__)






























































