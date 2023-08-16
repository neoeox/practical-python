# fileparse.py
#
# Exercise 3.3

import csv
from pprint import pprint


# list(dict)
def parse_csv_file(filename: str, select: list = None, types: list = None, has_headers=True, delimiter=',', silence_errors=False):
    """
    CSV 파일을 파싱해 레코드의 목록을 생성
    """
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        headers = next(rows) if has_headers else []
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:
                continue
            if select:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    return records


def parse_csv(lines, select: list = None, types: list = None, has_headers=True, delimiter=',', silence_errors=False):
    """
    CSV 파일을 파싱해 레코드의 목록을 생성
    """
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)
    headers = next(rows) if has_headers else []
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:
            continue
        if select:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    return records





"""
portfolio = parse_csv('Work/Data/portfolio.csv')
pprint(portfolio)

portfolio = parse_csv('Work/Data/portfolio.csv', select=['name', 'shares'])
pprint(portfolio)

portfolio = parse_csv('Work/Data/portfolio.csv', select=['name', 'price'], types=[str, float], has_headers=True)
portfolio = parse_csv('Work/Data/portfolio.csv', types=[str, int, float], has_headers=True)
pprint(portfolio)
print(type(portfolio))

prices = parse_csv('Work/Data/prices.csv', types=[str, float], has_headers=False)
pprint(prices)
print(type(prices))

portfolio = parse_csv('Work/Data/portfolio.dat', types=[str, int, float], delimiter=' ')
pprint(portfolio)

prices = parse_csv('Work/Data/prices.csv', select=['name', 'price'], has_headers=False)

portfolio = parse_csv('Work/Data/missing.csv', types=[str, int, float])
portfolio = parse_csv('Work/Data/missing.csv', types=[str, int, float], sirence_errors=True)
"""








