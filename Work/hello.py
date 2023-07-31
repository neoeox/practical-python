# hello.py

print('hello world')

name = 'Jake'
print('My name is', name)

print('Hello', end=' ')
print('My name is', 'Jake')

c = 4 + True
print(c)
d = False
if d == 0:
    print('d is False')

a = 2.1 + 4.2
print(a, a == 6.3)

a = 10
b = 20
c = 30
if b >= a and b <= c:
    print('b is between a and c')
if not (b < a or b > c):
    print('b is still between a and c')

a = 3.14159
print(int(a))

b = '3.14159'
print(float(b))

print(False)
print(int(False))
print(int(True))
print(bool("False"))
print(bool("True"))
print(bool(0))








