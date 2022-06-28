import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
#
#
# df = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-Algorithm/ai_algorithm/data/drank.csv", encoding="euc_kr")
# print(df["city"])
# print(df["drank"])
#
#
# def barchart(xlabel, y):
#     x = np.arange(len(y))
#     plt.title("Bar Chart")
#     plt.bar(x, y)
#     plt.xticks(x, xlabel)
#     plt.yticks(sorted(y))
#     plt.xlabel("가나다")
#     plt.ylabel("빈도 수")
#     plt.ylim(12, 20)
#     plt.show()
#
#
#
#
# def barhchart(xlabel, y):
#
#     y_pos = np.arange(len(xlabel))
#     error = np.random.rand(len(xlabel))
#     plt.title("Barh Chart")
#     plt.barh(y_pos, y, alpha=0.5)
#     plt.yticks(y_pos, xlabel)
#     plt.xlabel('x 라벨')
#     plt.xlim(12, 20)
#     plt.show()
#
#
# """
# labels = ['개구리', '돼지', '개', '통나무']
# sizes = [15, 30, 45, 10]
# """
# def piechart(xlabel, y):
#     colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
#     explode = (0, 0.1, 0, 0)
#     plt.title("Pie Chart")
#     plt.pie(y, explode=explode, labels=xlabel, colors=colors,
#             autopct='%1.1f%%', shadow=True, startangle=90)
#     plt.axis('equal')
#     plt.show()
#
#
# def histogram():
#     x = np.random.randn(1000)
#     plt.title("Histogram")
#     arrays, bins, patches = plt.hist(x, bins=10)
#     plt.show()
#
#
# def countplot():
#     # 차트 배경 설정
#     sns.set_style('whitegrid')
#     # 차트 세로로 그리기
#     sns.countplot(x="class", hue="who", data=titanic)
#     plt.show()
#
#
# xlabel = df["city"]
# y = df["drank"]
# barchart(xlabel, y)
# barhchart(xlabel, y)


import matplotlib.pyplot as plt
import numpy


# multi barhchart
a = [140,256,323,456,578]
b = [520,432,343,254,165]

label = ["서울", "경기", "전북", "전남", "제주"]

plt.figure()

y = np.arange(len(label))

plt.barh(y-0.2, a, label="초중고", height=0.4, color="#3333ff", alpha=0.2)
plt.barh(y+0.2, b, label="아동보호", height=0.4, color="#0066ff")

plt.legend()
plt.ylabel("월")
plt.xlabel("아동")
# plt.xlim(0, 7)
plt.title("아동폭력줄이자")
plt.grid()
plt.show()

