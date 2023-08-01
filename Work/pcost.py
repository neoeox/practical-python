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




