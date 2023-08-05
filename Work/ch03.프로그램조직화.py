"""
3. 프로그램 조직화
나중에 재사용하려면 이름을 붙여둬야 한다.
순서가 중요하다. 변수와 함수의 정의를 항상 위쪽에 둬야 한다.
단일 작업에 관련된 코드를 한 곳에 모아두는 것이 현명하다. 함수 사용하기.
함수는 문장의 시퀀스에 이름을 붙인 것이다.
함수 내에 모든 파이썬 문장을 사용할 수 있다.

"""

#
def square(x):
    return x * x
a = 42
b = a + 2
z = square(b)

#
import csv
from pprint import pprint


def read_prices(filename: str):
    """
    CSV 파일에서 이름과 가격 데이터를 읽음
    """
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            # print('row=', row, type(row))
            if len(row) == 0:
                continue
            prices[row[0]] = float(row[1])
    return prices


prices = read_prices('Work/Data/prices.csv')
pprint(prices)

#
# import os
# print(os.getcwd())
# os.chdir('./Work')
from pprint import pprint
from Work import fileparse

portfolio = fileparse.parse_csv('Work/Data/portfolio.csv', select=['name', 'shares', 'price'], types=[str, int, float])
pprint(portfolio)
pricelist = fileparse.parse_csv('Work/Data/prices.csv', types=[str, float], has_headers=False)
pprint(pricelist)
prices = dict(pricelist)
pprint(prices)
print(prices['IBM'])
print(prices['XOM'])


from Work.report2 import portfolio_report

portfolio_report('./Work/Data/portfolio.csv', './Work/Data/prices.csv')
portfolio_report('./Work/Data/portfolio2.csv', './Work/Data/prices.csv')

files = ['./Work/Data/portfolio.csv', './Work/Data/portfolio2.csv']
for name in files:
    print(f'{name:-^43s}')
    portfolio_report(name, './Work/Data/prices.csv')
    print()

# 연습 문제 3.15: main() 함수
import Work.report2 as report
report.main(['report.py', './Work/Data/portfolio.csv', './Work/Data/prices.csv'])

import Work.pcost as pcost
pcost.main(["pcost.py", "Work/Data/portfolio.csv"])

import Work.fileparse as fileparse
portfolio = fileparse.parse_csv_file('Work/Data/portfolio.csv', types=[str, int, float])
print(portfolio)

# import Work.fileparse as fileparse
# import gzip
# with gzip.open('Work/Data/portfolio.csv', 'rt') as f:
#     portfolio = fileparse.parse_csv(f, types=[str, int, float])
# print(portfolio)

lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
port = fileparse.parse_csv(lines, types=[str,int,float])
print(port)





