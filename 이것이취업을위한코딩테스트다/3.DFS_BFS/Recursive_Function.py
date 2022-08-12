# 재귀 함수


# basic of recursive function!
def recursive():
    print("재귀 함수는 자기 자신을 불러옵...")
    recursive()


# My Code
def factorial(n):
    answer = 1

    while n != 1:
        answer *= n
        n -= 1

    return answer


# Good Code (use recursive function)
def factorial1(n):
    if n == 1:
        return 1
    return n * factorial1(n - 1)
