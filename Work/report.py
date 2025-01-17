# report.py
import csv
from pprint import pprint


def read_portfolio(filename):
    """
    주식 포트폴리오 파일을 읽어 딕셔너리의 리스트를 생성.
    name, shares, price를 키로 사용.
    """
    portfolio = []
    types = [str, int, float]
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            converted = {name: func(val) for name, func, val in zip(headers, types, row)}
            portfolio.append(converted)
    return portfolio


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report_data(portfolio, prices):
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


def print_report(reportdata):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)


def portfolio_report(portfoliofile, pricefile):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    print_report(report)


portfolio_report('./Work/Data/portfolio.csv', './Work/Data/prices.csv')
portfolio_report('./Work/Data/portfolio2.csv', './Work/Data/prices.csv')

files = ['./Work/Data/portfolio.csv', './Work/Data/portfolio2.csv']
for name in files:
    print(f'{name:-^43s}')
    portfolio_report(name, './Work/Data/prices.csv')
    print()




