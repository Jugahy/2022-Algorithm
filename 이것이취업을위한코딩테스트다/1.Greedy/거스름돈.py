# My Code
N = 1260
count = 0
for i in [500, 100, 50, 10]:
    while N - i >= 0:
        N = N - i
        count += 1

# Good Code
n = 1260
count = 0
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n // coin
    n %= coin


