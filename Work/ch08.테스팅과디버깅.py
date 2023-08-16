"""
8. 테스팅과 디버깅
https://wikidocs.net/84364


"""
#
def add(x, y):
    assert isinstance(x, int), 'x Expected int'
    assert isinstance(y, int), 'y Expected int'
    return x + y
print(add(2, 3))
print(add(2, '3'))

def add(x, y):
    return x + y
assert add(2, 2) == 4
assert add('2', 2) == 4


#
import Work.report7 as report
import logging
logging.basicConfig()
logging.getLogger('fileparse2').level = logging.DEBUG
a = report.read_portfolio('Work/Data/missing.csv')
logging.getLogger('fileparse2').level = logging.CRITICAL
a = report.read_portfolio('Work/Data/missing.csv')


def spam(x):
    print('DEBUG:', repr(x))
spam(4)
spam('a')

from decimal import Decimal
x = Decimal('3.4')
print(x)
print(repr(x))
x = 'Life is too short'
print(x)
print(repr(x))












