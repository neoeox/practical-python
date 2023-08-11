# report2.py

import fileparse  # 명령행에서 실행할 때
# import fileparse  # 터미널에서 실행할 때 (venv) PS C:\dev_py\projects\practical-python> python Work/report.py Work/Data/portfolio.csv Work/Data/prices.csv
from stock import Stock
import tableformat as tableformat
from portfolio import Portfolio


def read_portfolio(filename):
    """
    주식 포트폴리오 파일을 읽어 딕셔너리의 리스트를 생성.
    name, shares, price를 키로 사용.
    """
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return Portfolio(portfolio)

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        summary = (s.name, s.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    (name, shares, price, change) 튜플의 리스트로부터 보기 좋게 포매팅한 테이블을 프린팅.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    주어진 포트폴리오와 가격 데이터 파일을 가지고 주식 보고서를 작성.
    '''
    # Read data files 데이터 파일 읽기
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out 보고서 데이터 생성
    formatter = tableformat.create_formatter(name=fmt)
    print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])

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





































