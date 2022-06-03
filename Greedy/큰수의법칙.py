m = 8
k = 3

num = [2, 4, 5, 4, 6]
answer = 0

num.sort(reverse = True)

print(num)
while m <= 8:
    while k <= 3:
        answer += num[0]
    answer += num[1]


