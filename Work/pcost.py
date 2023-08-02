# pcost.py
#
# Exercise 1.27

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
        row = line.split(',')
        name = row[0]
        shares = int(row[1])
        price = float(row[2])
        total_cost = total_cost + (shares * price)
    print('total_cost=', total_cost)


#
import gzip
with gzip.open('Work/Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')


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


#
import sys

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

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost=', cost)








