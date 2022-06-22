import matplotlib.pyplot as plt


def f(x):
    return x ** 2 - 4 * x + 7


def df(x):
    return 2 * x - 4


x = 5.0  # 초기 근사해
tol = 1e-6  # 허용오차
eta = 0.2  # 학습률

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

for i in range(40):
    x = x - 0.2 * f(x) / df(x)
    if df(x) < 0:
        print("음수",i)
    else:
        print("양수",i)
    print(x)