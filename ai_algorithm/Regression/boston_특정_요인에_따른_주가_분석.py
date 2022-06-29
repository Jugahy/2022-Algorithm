from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# drank,price,nomarrie,hitkid
boston = load_boston()
hit = pd.read_csv("C:/Users/jugah/PycharmProjects/2022-Algorithm/ai_algorithm/data/hit.csv", encoding="euc_kr")
hit_dic = {"drank":list(hit["drank"]), "price":list(hit["price"]), "nomarrie":list(hit["nomarrie"]), "hitkid":list(hit["hitkid"])}
hit_df = pd.DataFrame(hit_dic.data, index=["서울", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주", "세종"])

# df_boston = pd.DataFrame(boston.data, columns = boston.feature_names)

hit_df["hitkid"] = hit.target

# 선형회귀 모델 생성을 위한 라이브러리 임포트
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 학습에 사용할 데이터 준비
y_target = hit["hitkid"]
X_data = hit.drop(['hitkid'], axis=1, inplace=False)

# train, test 세트 분리
X_train, X_test, y_train, y_test = train_test_split(X_data, y_target, test_size=0.3, random_state = 156)



ridge_alphas = [0, 0.1, 1, 10, 100, 150, 200, 300]




import matplotlib.pyplot as plt
import seaborn as sns

# 각 alhpa값에 따른 회귀 계수 값 시각화
fig, axes = plt.subplots(figsize=(18, 6), nrows=1, ncols=len(ridge_alphas))

# 각 alpha에 따른 회귀 계수 값을 데이터로 저장하기 위한 DF
coeff_df = pd.DataFrame()

# alphas 리스트 값을 차례로 입력해 회귀 계수 값 시각화, pos는 axis의 위치
for pos, ridge_alpha in enumerate(ridge_alphas):
    ridge = Ridge(alpha=ridge_alpha)
    ridge.fit(X_data, y_target)

    # alhpa 값에 따른 피처별 회귀 계수를 Sereis로 변환하고 DF 칼럼으로 추가
    coeff = pd.Series(data=ridge.coef_, index=X_data.columns)
    colname = 'alpha:' + str(ridge_alpha)
    coeff_df[colname] = coeff

    # barplot으로 각 alhpa값에서의 회귀 계수를 시각화
    coeff = coeff.sort_values(ascending=False)
    axes[pos].set_title(colname)
    axes[pos].set_xlim(-3, 6)
    sns.barplot(x=coeff.values, y=coeff.index, ax=axes[pos])

plt.show()