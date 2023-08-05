# report2.py

from Work import fileparse  # 명령행에서 실행할 때
# import fileparse  # 터미널에서 실행할 때 (venv) PS C:\dev_py\projects\practical-python> python Work/report.py Work/Data/portfolio.csv Work/Data/prices.csv

def read_portfolio(filename):
    """
    주식 포트폴리오 파일을 읽어 딕셔너리의 리스트를 생성.
    name, shares, price를 키로 사용.
    """
    with open(filename) as lines:
        return fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))

def make_report_data(portfolio,prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    print_report(report)

def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)

# portfolio_report('./Work/Data/portfolio.csv', './Work/Data/prices.csv')
# portfolio_report('./Work/Data/portfolio2.csv', './Work/Data/prices.csv')
#
# files = ['./Work/Data/portfolio.csv', './Work/Data/portfolio2.csv']
# for name in files:
#     print(f'{name:-^43s}')
#     portfolio_report(name, './Work/Data/prices.csv')
#     print()





































