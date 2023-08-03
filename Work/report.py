# report.py
#
# Exercise 2.4

import csv

def read_porfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

filename = "Work/Data/portfolio.csv"
portfolio = read_porfolio(filename)
print(portfolio)
print(portfolio[0])

total = 0.0
for name, shares, price in portfolio:
    total += shares * price
print(total)


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

filename = "Work/Data/portfolio.csv"
portfolio = read_portfolio(filename)
print(portfolio)
total = 0.0
for s in portfolio:
    total += s['shares'] * s['price']
print(total)

from pprint import pprint
pprint(portfolio)

prices = {}
prices['IBM'] = 92.45
prices['MSFT'] = 45.12
print(prices)
print(prices['AAPL'])
print('AAPL' in prices)



def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row):
                # stock = {
                #     row[0]: float(row[1]),
                # }
                # prices.append(stock)
                prices[row[0]] = float(row[1])
    return prices

filename = "Work/Data/prices.csv"
prices = read_prices(filename)
pprint(prices)


#
def make_report(portfolio, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

portfolio = read_portfolio('Work/Data/portfolio.csv')
prices = read_prices('Work/Data/prices.csv')
report = make_report(portfolio, prices)
pprint(report)
print('%10s %10s %10s %10s' % ('name', 'shares', 'price', 'change'))
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {format(price):>10.2f} {change:>10.2f}')

print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {format(price):>10s} {change:>10.2f}')
















