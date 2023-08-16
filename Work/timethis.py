# timethis.py

import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            print('%s.%s: %f' % (func.__module__, func.__name__, end - start))
    return wrapper

# print(__name__)
if __name__ == '__main__':
    @timethis
    def countdown(n):
        while n > 0:
            n -= 1

    countdown(1000000)


#
class Foo(object):
    @staticmethod
    def bar(x):
        print('x=', x)
Foo.bar(2)

#
class Foo(object):
    def bar(self):
        print(self)
    @classmethod
    def spam(cls):
        print(cls)
f = Foo()
f.bar()
Foo.spam()

#
import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        print(cls)
        tm = time.localtime()
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)

d = Date.today()
print(d)

























