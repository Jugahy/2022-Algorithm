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


# import matplotlib.pyplot as plt
# import numpy
#
#
# multi barhchart
# a = [945, 680, 587, 726, 190, 440, 91, 486, 2282, 501, 460, 744, 781, 642, 700, 553, 165]
# b = [134, 34, 177, 342, 23, 194, 3, 59, 528, 95, 69, 79, 259, 137, 133, 48, 80]
#
# label = ["서울", "부산", "대구", "인천", "광주", "대전", "세종", "울산", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
#
# plt.figure()
#
# y = np.arange(len(label))
#
# plt.barh(y-0.2, a, label="교육기관", height=0.4, color="#3333ff", alpha=0.2)
# plt.barh(y+0.2, b, label="아동보호전문기관", height=0.4, color="#0066ff")
#
# plt.legend()
# plt.ylabel(label)
# plt.xlabel("아동")
# # plt.xlim(0, 7)
# plt.title("아동폭력줄이자")
# plt.grid()
# plt.show()

# import math
#
# a = [3837, 3334, 2208, 1745, 2576, 3208, 3746, 3523, 3430, 3480, 3116, 3428, 2184, 2383, 3500, 3866, 3542, 3278]
# ave = sum(a)/18
#
# total = 0
# for i in range(len(a)):
#     total += (a[i] - ave) ** 2
#
# print("평균 :", sum(a)/18)
# print("분산 :", (1/(len(a)-1) * total))
# print("표준편차 :", math.sqrt(1/(len(a)-1) * total))
# c = math.sqrt(1/(len(a)-1) * total)
#
# print("검정통계량 :", (ave - 2800)/(c/math.sqrt(len(a))))


import pandas as pd

import matplotlib.pyplot as plot

# Python dictionary

inflationAndGrowth = {"신고 수": [5533, 6284, 443,653,1945,216,28,367,10254,39,611,401,55,1127]}

index = ["아동본인", "부모", "형제자매", "친인척", "이웃·친구", "경찰", "종교인", "사회복지관련 종사자", "아동보호전문기관종사자", "의료사회복지사", "낯선사람", "익명", "법원", "기타"]

# Python dictionary into a pandas DataFrame

dataFrame = pd.DataFrame(data=inflationAndGrowth);

dataFrame.index = index;

dataFrame.plot.barh(rot=15, title="비신고의무자의 신고 수");

plot.show(block=True);