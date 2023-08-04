"""
2. 데이터로 작업하기
https://wikidocs.net/84358
"""

# None
email_address = None
print(email_address)

def send_email(email_address, msg):
    print(email_address, msg)

email_address = 'abc@keco.go.kr'
msg = 'Hello jon'
if email_address:
    send_email(email_address, msg)


# tuple
s = ('GOOG', 100, 490.1)
print(s, type(s))
s = 'GOOG', 100, 490.1
print(s, type(s))

t = ()  # 빈 튜플
w = ('GOOG',)
print(t, type(t))
print(w, type(w))

s = ('GOOG', 100, 490.1)
name, shares, price = s
print(name, shares, price)
print('Cost=', shares * price)

record = ('GOOG', 100, 490.1)
symbols = ['GOOG', 'AAPL', 'IBM']

# 딕셔너리
s = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1,
}
print(s, type(s))
print(s['name'], s['shares'], s['price'])
s['shares'] = 75
s['date'] = '2023/08/02'
del s['date']

print(s['price'])
print(s[2])  # KeyError: 2


#
import csv
f = open('./Work/Data/portfolio.csv')
rows = csv.reader(f)
print(next(rows))
row = next(rows)
print(row)
f.close()

t = (row[0], int(row[1]), float(row[2]))
print(t)
cost = t[1] * t[2]
print(cost)
t[1] = 75  # TypeError: 'tuple' object does not support item assignment  튜플은 읽기 전용
t = ([t[1], 75, t[2]])  # 튜플의 내용을 바꿀 수는 없지만, 항상 완전히 새로운 튜플을 생성해 기존 것을 대신할 수 있다.

#
d = {
    'name': row[0],
    'shares': int(row[1]),
    'price': float(row[2]),
}
print('d=', d)
print('cost=', d['shares'] * d['price'])
d['shares'] = 75
d['date'] = (6, 11, 2007)
d['account'] = 12345
print('d=', d)

print(list(d))

for k in d:
    print('k=', k, ', v=', d[k])

keys = d.keys()
print(keys)
del d['account']
print(keys)

items = d.items()
print(items)
for k, v in d.items():
    print(k, '=', v)

print(items, type(items))
d = dict(items)
print(d, type(d))

'''
리스트(list): 순서가 유지되는(ordered) 데이터.
딕셔너리(dict): 순서가 없는(unordered) 데이터.
세트(set): 고유한 항목의 집합이며 순서가 없음.
'''
# list
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]
print(portfolio, type(portfolio))
print(portfolio[0], type(portfolio[0]))

records = []
records.append(('GOOG', 100, 490.1))
records.append(('IBM', 50, 91.3))
print(records)

records = []
with open('Work/Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        line = line.replace('\n', '')
        row = line.split(',')
        records.append((row[0], row[1], row[2]))
print(records)


#
prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}
print(prices)
print(prices['GOOG'])

prices = {}
prices['GOOG'] = 513.25
prices['CAT'] = 93.37
prices['IBM'] = 87.22
print(prices)

prices = {} # 빈 딕셔너리로 초기화
with open('Work/Data/prices.csv', 'rt') as f:
    for line in f:
        if line.strip():  # 빈줄 확인
            row = line.split(',')
            # print(row[0], float(row[1]))
            prices[row[0]] = float(row[1])
print(prices)

key = 'aaaa'
key = 'name'
if key in d:
    print('YES')
else:
    print('NO')

name = d.get(key, 'jonsoft')
print(name)

holidays = {
    (1, 1): 'New Years',
    (3, 14): 'Pi day',
    (9, 13): "Programmer's day",
}
print(holidays)
print(holidays[3, 14])
print(holidays[(3, 14)])

# set
tech_stocks = {'IBM', "AAPL", 'MSFT'}
print(tech_stocks)
tech_stocks = set(['IBM', "AAPL", 'MSFT'])
print(tech_stocks)

names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']
unique = set(names)
print(names)
print(unique)
unique.add('CAT')
unique.remove('YHOO')


#
name = 'IBM'
shares = 100
price = 91.1
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')

s = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}
print(f'{name:>10s} {shares:>10d} {price:>10.2f}'.format_map(s))

print(f'{name:>10s} {shares:>10d} {price:>10.2f}'.format(name='IBM', shares=100, price=91.1))

print('The value is %d' % 3)
print('%5d %-5d %10d' % (3, 4, 5))
print('%0.2f' % (3.1415926,))


value = 42868.1
print(value)
print(f'{value:0.4f}')
print(f'{value:16.2f}')
print(f'{value:*>16,.2f}')

f = '%0.4f' % value
print(f, type(f))


a = 'Hello'
b = [1, 4, 5]
c = ('GOOG', 100, 490.1)
print(a[0])
print(b[-1])
print(c[1])
print(len(a))
print(len(b))
print(len(c))
print(a * 3)
print(b * 2)
print(c * 2)

a = (1, 2, 3)
b = (4, 5)
print(a + b)
c = [1, 5]
print(a + c)  # TypeError: can only concatenate tuple (not "list") to tuple

a = list(range(0, 9))
print(a)
print(a[2:5])
print(a[-5])
print(a[:3])
a[2:4] = [10, 11, 12]
print(a)

s = [1, 2, 3, 4, 5]
print(s)
print(sum(s))
print(max(s))
t = ['Hello', 'World']
print(max(t))

s = [1, 4, 9, 16]
for i in s:
    print(i)
print(i)

filename = "Work/Data/prices.csv"
with open(filename, 'rt') as f:
    lines = f.readlines()
    for line in lines:
        if line == '\n':
            continue
        print(line, end='')

for i in range(100):
    print(i)
for j in range(10, 20):
    print(j)
for k in range(10, 50, 2):
    print(k)

names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    print(i, name)

filename = "Work/Data/prices.csv"
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
        print(lineno, line, end='')

points = [
    (1, 4), (10, 40), (23, 14), (5, 6), (7, 8)
]
for x, y in points:
    print(x, y)
for i, point in enumerate(points):
    # print(i, point)
    print(i, point[0], point[1])

columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1]
pairs = zip(columns, values)
for column, value in pairs:
    print(column, '=', value)

pairs = zip(columns, values)
for pair in pairs:  # 작동 안됨 왜 -> 소비되면 값을 지움
    print(pair)

d = dict(zip(columns, values))
print(d)
for k, v in d.items():
    print(k, v)

for n in range(10):
    print(n, end=' ')

for n in range(10, 0, -1):
    print(n, end=' ')

for n in range(0, 10, 2):
    print(n, end=' ')

data = [4, 9, 1, 25, 16, 100, 49]
print(min(data))
print(max(data))
print(sum(data))

for x in data:
    print(x)

for n, x in enumerate(data):
    print(n, x)


prices = {
    'GOOG': 490.1,
    'AA': 23.45,
    'IBM': 91.1,
    'MSFT': 34.23
}
print(prices.items())
pricelist = list(zip(prices.values(), prices.keys()))
print(pricelist)
print(min(pricelist))
print(max(pricelist))
print(sorted(pricelist))

a = [5, 1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6, 0.8]
print(list(zip(a, b, c)))


portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]
from collections import Counter
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares
print(total_shares['IBM'])
print(total_shares)
print(total_shares.most_common(3))

from collections import defaultdict
holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares, price))
print(holdings['IBM'])
print(holdings)


from collections import deque
history = deque(maxlen=10)
filename = "Work/Data/portfolio.csv"
with open(filename) as f:
    for line in f:
        history.append(line)
print(history)


#
import csv
def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # holding = (row[0], int(row[1]), float(row[2]))
            # stock = {
            #     'name': row[0],
            #     'shares': int(row[1]),
            #     'price': float(row[2]),
            # }
            stock = {
                headers[0]: row[0],
                headers[1]: int(row[1]),
                headers[2]: float(row[2]),
            }
            portfolio.append(stock)
    return portfolio
portfolio = read_portfolio('Work/Data/portfolio.csv')
from collections import Counter
holdings = Counter()
for s in portfolio:
    holdings[s['name']] += s['shares']
print(holdings)
print(holdings['IBM'])
print(holdings['MSFT'])
print(holdings.most_common(3))


portfolio2 = read_portfolio('Work/Data/portfolio2.csv')
holdings2 = Counter()
for s in portfolio2:
    holdings2[s['name']] += s['shares']
print(holdings2)

print(holdings)
print(holdings2)
combined = holdings + holdings2
print(combined)






























































