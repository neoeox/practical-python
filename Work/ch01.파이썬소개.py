# ch01.파이썬소개.py

print('hello world')

name = 'Jake'
print('My name is', name)

print('Hello', end=' ')
print('My name is', 'Jake')

c = 4 + True
print(c)
d = False
if d == 0:
    print('d is False')

a = 2.1 + 4.2
print(a, a == 6.3)

a = 10
b = 20
c = 30
if b >= a and b <= c:
    print('b is between a and c')
if not (b < a or b > c):
    print('b is still between a and c')

a = 3.14159
print(int(a))

b = '3.14159'
print(float(b))

print(False)
print(int(False))
print(int(True))
print(bool("False"))
print(bool("True"))
print(bool(0))

a = 'Hello world'
b = a[0]
c = a[4]
d = a[-1]
print(a, b, c, d)
print(a[:5])
print(a[6:])
print(a[3:8])
print(a[-5:])

a = 'Hello' + 'World'
b = 'Say ' + a
print(a)
print(b)

s = 'Hello'
print(len(s))

print('e' in s)
print('x' in s)
print('hi' not in s)
print(s * 5)

s = '    Hello '
print(":", s.strip(), sep="")
print(':', s, ":", sep="")

s = "Hello"
print(s.lower())
print(s.upper())

s = 'Hello world'
print(s.replace("Hello", "Hallo"))
print(s)

x = 42
print(str(x), type(x), type(str(x)))

data = b'Hello World\r\n'
print(data)
print(len(data))
print(data[:5])
print(data.replace(b'Hello', b'Cruel'))
print(data[0])

print(data.decode('utf-8'))
print(data)
text = data.decode('utf-8')
print(text.encode('utf-8'))

rs = r'c:\newdata\test'
print(rs)

name = 'IBM'
shares = 100
price = 91.1
a = f':{name:>10s}:{shares:10d}:{price:10.2f}:'
print(a)

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
print(symbols)
print(symbols[0])
print(symbols[1])
print(symbols[2])
print(symbols[-1])
print(symbols[-2])

symbols[0] = 'a'  # TypeError: 'str' object does not support item assignment

symbols = symbols + 'GOOG'
print(symbols)

symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
symbols = symbols + ',GOOG'
print(symbols)
symbols = 'HPQ,' + symbols
print(symbols)

symbols.find('MSFT')
symbols[13:17]

symbols = symbols.replace('SCO', 'DOA')
print(symbols)
name = '      IBM  \n:'
print(name)
name = name.strip()
print(name)

name = 'IBM'
shares = 100
price = 91.1
print(f'{shares} shares of {name} at ${price:0.2f}')

text = 'Today is 3/27/2018. Tomorrow is 3/28/2018'
import re
print(re.findall(r'\d+/\d+/\d+', text))
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

s = 'hello world'
print(dir(s))
help(s.upper)

names = ['Elwood', 'Jake', 'Curtis']
nums = [39, 38, 42, 65, 111]

line = 'GOOG,100,490.10'
row = line.split(',')
print(row)

names.append('Murphy')
print(names)
names.insert(2, 'Aretha')
print(names)

s = [1, 2, 3]
t = ['a', 'b']
print(s + t)

print(names[0])
print(names[1])
print(names[2])
print(names[-1])
print(names[-2])

names[1] = 'Joliet Jake'
print(names)
print(len(names))
print('Elwood' in names)

s = [1, 2, 3]
print(s * 3)

for name in names:
    print(name)

names = ['Elwood','Jake','Curtis']
names.index('Curtis')
names.remove('Curtis')
print(names)
del names[1]
print(names)

s = [10, 1, 7, 3]
s.sort()
print(s)
s = [10, 1, 7, 3]
s.sort(reverse=True)
print(s)

s = ['foo', 'bar', 'spam']
s.sort()
print(s)

s = ['foo', 'bar', 'spam']
print(sorted(s))
print(s)

nums = [1, 2, 3, 4, 5]
nums * 2
nums + [10, 11, 12, 13, 14, 15]

symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(',')
print(symlist[0])
print(symlist[2])
symlist[2] = 'AIG'
print(symlist[2])
print(symlist[0:3])

mysyms = []
mysyms.append('GOOG')
print(mysyms)
symlist[-2:] = mysyms
print(symlist)

for s in symlist:
    print('s=', s)

symlist = ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
print('AIG' in symlist)
print('AA' in symlist)
print('CAT' not in symlist)
print(symlist)
print(symlist[:3])
print(symlist[-2:])


symlist = ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
symlist.append('RHT')
print(symlist)
symlist.insert(2, 'AA')
print(symlist)
symlist.remove('MSFT')
print(symlist)
symlist.append('YHOO')
print(symlist)
print(symlist[4])
print(symlist.index('YHOO'))
print(symlist.count('YHOO'))
symlist.remove('YHOO')
print(symlist)
symlist.sort()
print(symlist)
symlist.sort(reverse=True)
print(symlist)

a = ','.join(symlist)
print(a)
b = ':'.join(symlist)
print(b)
c = ''.join(symlist)
print(c)

nums = [101, 102, 103]
items = ['spam', symlist, nums]
print(items)
print(items[0])
print(items[0][0])
print(items[1])
print(items[1][1])
print(items[1][1][1])
print(items[2])
print(items[2][1])

f = open('./Work/Data/foo.txt', 'rt')
data = f.read()
print(data)
f.close()

g = open('./Work/Data/bar.txt', 'wt')
g.write('some text')
g.close()

filename = './Work/Data/foo.txt'
with open(filename, 'rt') as file:
    data = file.read()
print(data)

with open(filename, 'rt') as file:
    for line in file:
        print(line, end="")
print()

filename = './Work/Data/bar.txt'
with open(filename, 'wt') as out:
    out.write("Hello world\n")

with open(filename, 'wt') as out:
    print('Hello World!', file=out)

#
import os
print(os.getcwd())

# 전체 파일을 한 번에 읽어 큰 문자열을 만들어 보자.
with open('Work/Data/portfolio.csv', 'rt') as f:
    data = f.read()
print(data)

# 파일을 행 단위로 읽으려면 다음과 같이 for 루프를 사용한다.
with open('Work/Data/portfolio.csv', 'rt') as f:
    for line in f:
        print(line, end='')

# 특정한 상황에서, 텍스트의 단일 행을 읽거나 건너뛸 수 있다(예: 첫 행의 컬럼 헤더를 건너뛰고 싶을 것이다).
with open('Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    print(headers, end='')
    for line in f:
        print(line, end='')

# 파일의 행을 읽었으면 문자열을 분할하는 것과 같은 처리를 할 수 있다.
with open('Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    print(headers)
    for line in f:
        row = line.split(',')
        print(row)


def sumcount(n):
    '''
    정수 1부터 n까지의 합을 반환
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

a = sumcount(100)
print('a=', a)

#
import math
x = math.sqrt(10)
print('x=', x)

import urllib.request
u = urllib.request.urlopen('http://www.python.org/')
data = u.read()
print(data)


# 예외를 붙잡아 처리하기
import os
print(os.getcwd())
name = ''
shares = 0
price = 0
total_cost = 0
with open('Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    print(headers)
    for line in f:
        try:
            row = line.split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            total_cost = total_cost + (shares * price)
        except ValueError:
            print("Couldn't parse", line)
    print('total_cost=', total_cost)

# 예외를 일으키기
raise RuntimeError('What a kerfuffle')

# 함수의 첫 문장이 문자열이면 그것을 문서로 사용한다.
# help(greeting) 명령을 타이핑해 문서가 표시되는지 확인해 보라.
def greeting(name):
    'Issues a greeting'
    print('Hello', name)
greeting('Guido')
greeting('Paula')

#
def portfolio_cost(filename):
    name = ''
    shares = 0
    price = 0
    total_cost = 0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        print(headers)
        for line in f:
            row = line.split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            total_cost = total_cost + (shares * price)
    return total_cost

cost = portfolio_cost('Work/Data/portfolio.csv')
print('Total cost=', cost)

# 필드가 누락된 파일을 가지고 함수를 실행하면 무슨 일이 일어나는가?
cost = portfolio_cost('Work/Data/missing.csv')
print('Total cost=', cost)


#
import csv
f = open('Work/Data/portfolio.csv')
f = open('Work/Data/missing.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
for row in rows:
    print(row)
f.close()










