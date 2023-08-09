"""
4. 클래스와 객체
https://wikidocs.net/84360
"""

nums = [1, 2, 3]
nums.append(4)
print(nums)
nums.insert(1, 10)
print(nums)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def damage(self, pts):
        self.health -= pts

a = Player(2, 3)
b = Player(10, 20)
print(a.x)
print(b.x)
a.move(1, 2)
print(a.x, a.y)

s = ('GOOG', 100, 490.10)
print(s, type(s))
s = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.10
}
print(s, type(s))

def cost(s):
    return s['shares'] * s['price']
print(cost(s))


import Work.stock as stock
a = stock.Stock('GOOG', 100, 490.10)
print(a.name, a.shares, a.price)
b = stock.Stock('AAPL', 50, 122.34)
c = stock.Stock('IBM', 75, 91.75)
print(b.shares * b.price)
print(c.shares * c.price)
print(b.cost())

stocks = [a, b, c]
print(stocks, type(s))
for s in stocks:
    print(s)

for s in stocks:
    print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')


# 연습문제 메서드를 추가하기
# import Work.stock as stock
from Work import stock
s = stock.Stock('GOOG', 100, 490.10)
print(s.cost())
print(s.shares)
s.sell(25)
print(s.shares)
print(s.cost())

# 인스턴스의 리스트를 생성하기
import Work.fileparse as fileparse
with open('Work/Data/portfolio.csv') as lines:
    portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
print(portdicts)
portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
print(portfolio)
print(type(portfolio))
print(sum(s.cost() for s in portfolio))

# 클래스를 사용하기
from Work import pcost
pcost.portfolio_cost('Work/Data/portfolio.csv')
from Work import report3
report3.portfolio_report('Work/Data/portfolio.csv', 'Work/Data/prices.csv')


from Work.stock import MyStock
s = MyStock('GOOG', 100, 490.1)
print(s.cost())
print(s.name, s.shares, s.price)
s.sell(25)
print(s.name, s.shares, s.price)
s.panic()
print(s.name, s.shares, s.price)

from Work.stock import Stock, MyStock
s1 = Stock('GOOG', 100, 490.1)
print(s1.cost())
print(s1.cost() * 1.1)
s2 = MyStock('GOOG', 100, 490.1, 1.1)
print(s2.cost())

import Work.report4 as report
report.portfolio_report('Work/Data/portfolio.csv', 'Work/Data/prices.csv', fmt='txt')
report.portfolio_report('Work/Data/portfolio.csv', 'Work/Data/prices.csv', fmt='csv')
report.portfolio_report('Work/Data/portfolio.csv', 'Work/Data/prices.csv', fmt='html')



#
from datetime import date
d = date(2012, 12, 21)
print(d)
d
print(str(d))
str(d)

repr(d)

#
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'
    def __repr__(self):
        return f'Date({self.year}, {self.month}, {self.day})'

d = Date(2012, 12, 21)
d
print(d)
str(d)
print(str(d))
repr(d)
print(repr(d))

"""
a + b       a.__add__(b)
a - b       a.__sub__(b)
a * b       a.__mul__(b)
a / b       a.__truediv__(b)
a // b      a.__floordiv__(b)
a % b       a.__mod__(b)
a << b      a.__lshift__(b)
a >> b      a.__rshift__(b)
a & b       a.__and__(b)
a | b       a.__or__(b)
a ^ b       a.__xor__(b)
a ** b      a.__pow__(b)
-a          a.__neg__()
~a          a.__invert__()
abs(a)      a.__abs__()
"""
a = 2
b = 3
a.__add__(b)
a
~a
abs(~a)

x = 'abc'
len(x)
x.__len__()


#
class Sequence:
    def __len__(self):
        pass
    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        pass
    def __delitem__(self, key):
        pass

from Work.stock import Stock
s = Stock('GOOG', 100, 490.10)
c = s.cost
c
c()
print('Cost : %0.2f' % s.cost())
print('Cost : %0.2f' % s.cost)  # TypeError: must be real number, not method

#
from Work.stock import Stock
obj = ('GOOG', 100, 490.10, 'x')
if hasattr(obj, 'x'):
    x = getattr(obj, 'x')
else:
    x = None
print(x)
x = getattr(obj, 'x', None)
print(x)

#
from Work.stock import Stock
goog = Stock('GOOG', 100, 490.1)
print(goog)


"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first
name = 'jon'
print(f"Harold's a clever {name!s}")        # Calls str() on the argument first
print(f"Bring out the holy {name!r}")    # Calls repr() on the argument first
print(f"More {name!a}")                      # Calls ascii() on the argument first


import Work.report4 as report
portfolio = report.read_portfolio('Work/Data/portfolio.csv')
print(portfolio)

import Work.stock as stock
s = stock.Stock('GOOG', 100, 490.1)
columns = ['name', 'shares']
for colname in columns:
    print(colname, '=', getattr(s, colname))


import Work.report4 as report
portfolio = report.read_portfolio('Work/Data/portfolio.csv')
print(portfolio)
from Work.tableformat import create_formatter, print_table
formatter = create_formatter('txt')
print_table(objects=portfolio, columns=['name', 'shares'], formatter=formatter)
print_table(portfolio, ['name', 'shares', 'price'], formatter)


from Work.tableformat import create_formatter
formatter = create_formatter('xls')

















