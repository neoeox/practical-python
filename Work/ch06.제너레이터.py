"""
ch06.제너레이터
"""

#
a = 'hello'
for c in a:
    print(c)

b = {
    'name': 'Dave',
    'password': 'foo',
}
print(type(b))
print(b)
for i, item in enumerate(b.items()):
    print(i, item)
for i, item in enumerate(b.items()):
    print(i, item[0], item[1])

c = list(range(1, 5))
print(c)
for i in c:
    print(i)

f = open('Work/Data/portfolio.csv')
for x in f:
    print(x, end='')
f.close()

obj = {
    'name': 'Dave',
    'password': 'foo',
}
for x in obj:
    print(x)

_iter = obj.__iter__()
print(_iter)
while True:
    try:
        x = _iter.__next__()
    except StopIteration:
        break

x = [1, 2, 3]
it = x.__iter__()
print(it)
print(it.__next__())

class Portfolio:
    def __init__(self):
        self.holdings = []
    def __iter__(self):
        return self.holdings.__iter__()

port = Portfolio()
for s in port:
    print(s)
print(port.__dict__)

a = [1, 9, 4, 25, 16]
i = a.__iter__()
i.__next__()
i.__next__()
i.__next__()
i.__next__()
i.__next__()
i.__next__()

#
# import Work.fileparse as fileparse
# from Work.stock import Stock
# from Work.portfolio import Portfolio

#
import Work.report4 as report
# portfolio = report.read_portfolio('Work/Data/portfolio.csv')
# prices = report.read_prices('Work/Data/prices.csv')
# report = report.make_report_data(portfolio, prices)
report.portfolio_report('Work/Data/portfolio.csv', 'Work/Data/prices.csv')

import Work.pcost as pcost
pcost.portfolio_cost('Work/Data/portfolio.csv')

import Work.report4 as report
portfolio = report.read_portfolio('Work/Data/portfolio.csv')
print(len(portfolio))
print(portfolio[0])
print(portfolio[1])
print(portfolio[:3])
print('IBM' in portfolio)
print('AAPL' in portfolio)

def countdown(n):
    return list(range(10, 0, -1))
for x in countdown(10):
    print(x, end=' ')
print()
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for x in countdown(10):
    print(x, end=' ')

def countdown(n):
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1
x = countdown(10)
print(x)
print(x.__next__())

#
def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line
for line in open('Work/Data/portfolio.csv'):
    print(line, end='')
for line in filematch('Work/Data/portfolio.csv', 'IBM'):
    print(line, end='')

#
from Work.follow import follow
def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
lines = follow('Work/Data/stocklog.csv')
ibm = filematch(lines, 'IBM')
for line in ibm:
    print(line)


#
from Work.follow import follow
import csv
lines = follow('Work/Data/stocklog.csv')
rows = csv.reader(lines)
for row in rows:
    print(row)


from Work.ticker import ticker
ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')

a = [1, 2, 3, 4]
b = (2 * x for x in a)
print(b)
for i in b:
    print(i, end=' ')

a = [1, 2, 3, 4]
b = (x * x for x in a)
c = (-x for x in a)
for i in b:
    print(i, end=' ')
print()
for i in c:
    print(i, end=' ')

#
import itertools
"""
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1, ... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1, ... , sN)
"""

nums = [1, 2, 3, 4, 5]
squares = (x * x for x in nums)
print(squares)
print(type(squares))
for n in squares:
    print(n)

nums = [1,2,3,4,5]
sum([x*x for x in nums])    # 리스트 컴프리헨션
sum(x*x for x in nums)      # 제너레이터 표현식


def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

rows = (row for row in rows if row['name'] in names)















































