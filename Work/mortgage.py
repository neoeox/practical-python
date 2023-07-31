# mortgage.py
#
# Exercise 1.7


# 연습 문제 1.7: 데이브의 주택 담보 대출
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

print(payment * 30 * 12)

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
print('total_paid=', total_paid)

# 연습문제 1.8: 추가 납입
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment = 1000

while principal > 0:
    month = month + 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    if 1 <= month <= 12:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
print('total_paid=', total_paid, ', month=', month)

# 연습 문제 1.8: 추가 납입
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal < 0:
        total_paid = total_paid + principal
        principal = 0
    print(month, total_paid, principal)

print('total_paid=', total_paid, ', month=', month)









