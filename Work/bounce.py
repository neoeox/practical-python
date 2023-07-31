# bounce.py
#
# Exercise 1.5

height = 100
bounce_rate = 3 / 5

while height * bounce_rate > 0.5:
    height = height * bounce_rate
    # print(height)
    print(round(height, 4))
