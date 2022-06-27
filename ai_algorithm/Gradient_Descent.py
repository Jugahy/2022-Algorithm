import matplotlib.pyplot as plt

def f(x):
    return x ** 2 - 4 * x + 7


def df(x):
    return 2 * x - 4
#
#
#
# tol = 1e-6  # 허용오차
# eta = 0.2  # 학습률

# for k in range(300):
#
#     g0 = df(x0)
#
#     if abs(g0) <= tol:
#         print("알고리즘 성공!")
#         break
#
#     x0 = x0 - eta * g0
#
#     print("x* =", x0)
#     print("|g*| =", abs(g0))
#     print("f(x*) =", f(x0))
#     print("반복 횟수 =", k + 1)
# x = 5.0  # 초기 근사해
# for i in range(10):
#     x = x - 0.2 * f(x) / df(x)
#     print(i+1, x)
#
#     print()
# import sys
# import pandas as pd
# sys.maxsize
#
# x_old = 0
# x_new = 5 # The algorithm starts at x=6
# eps = 0.2 # step size
# precision = 0.7
#
# def f_prime(x):
#
#     return x ** 2 - 4 * x + 7
#
#
# while abs(x_new - x_old) > precision:
#     x_old = x_new
#     x_new = x_old - eps * f_prime(x_old)
#     print(1,x_old)
#     print(2,x_new)
#
# print(f"Local minimum occurs at: {x_new}")

x0 = 5.0  # 초기 근사해
tol = 0.1  # 허용오차
eta = 0.2  # 학습률

for k in range(300):

    g0 = df(x0)

    if abs(g0) <= tol:
        print("알고리즘 성공!")
        break

    x0 = x0 - eta * g0

    print(k)
    print("x* =", x0)
    print("|g*| =", abs(g0))
    print()

