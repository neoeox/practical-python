# sears.py
bill_thickness = 0.11 * 0.001  # 지폐의 두께(0.11 mm)를 미터로 환산
sears_height = 442
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('day=', day)
print('num_bills=', num_bills)
print('bills height=', num_bills * bill_thickness)





