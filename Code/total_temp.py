"""
# IBM HR Data-Set

<전처리>
1. 데이터 로드
2. 라벨 인코딩
3. 데이터 프레임 -> 넘파이 (라이브러리 사용을 위해)

<분석>
0. 기초 통계 분석
1. 차원 축소 - PCA
    차원 축소하고 상관계수가 높은 데이터들 중에서 이탈률, 퍼포먼스에 영향을 줄 것 같은 것을 골라서 -가설 세우기-
    분석 (분석 관점에서는 가설 세우기,  sample = 집의 거리가 멀수록, 직급이 낮을 수록 ? high Atrrition rate)

3. 로지스틱 회귀
4. 통계적 결론 내리기 (데분프 에서만 해당)


<분석 기반으로 위험 직원 골라내기>
# 위에서 통계 분석 기반으로 새로운 직원의 데이터가 입력되거나,
# 기존 직원의 데이터가 변경되는 경우
# 해당 직원의 이탈률 예측, 퍼포먼스 예측
"""

# 데이터 로드
# =====================================================
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing


print("\nwork space -", os.getcwd(), '\n')
file = open("C:/project-IBM/data/IBM.csv")

att = []
no_att = []
human = []
col = []
for i, a in enumerate(file):
    tmp = a.split(",")
    if i == 0:
        tmp[-1] = tmp[-1].strip()
        col = tmp
        continue
    else:
        tmp[-1] = int(str(tmp[-1]).strip())
        if tmp[1] == 'Yes':
            att.append(tmp)
        else:
            no_att.append(tmp)
        human.append(tmp)


col[0] = 'Age' # 0번째 인덱스 에러 처리
df = pd.DataFrame(data=human, columns=col)

# =====================================================
# pandas 컬럼 단위 접근방법 df.iloc[:, 0])
enc = preprocessing.LabelEncoder()
for i in range(35):
    sample = df.iloc[1, i]
    if str(sample).isdigit():
        continue
    else:
        out_enc = enc.fit_transform(df.iloc[:, i])
        df.iloc[:, i] = out_enc



att = df[df.iloc[:,1] == 1]
no_att = df[df.iloc[:,1] == 0]
"""
# numpy array for sklearn
np_df = df.values
np_att = att.values
np_no_att = no_att.values
"""
# =====================================================
# Visualization
# =====================================================
from matplotlib.colors import ListedColormap

cm3 = ListedColormap(['#0000aa', '#ff2020', '#50ff50'])

fig, axes = plt.subplots(18, 2, figsize=(10, 20))
att = df[df.iloc[:,1] == 1]
no_att = df[df.iloc[:,1] == 0]
"""
pd.plotting
ax = axes.ravel()
for i in range(35):
    _, bins = plt.hist(df.iloc[:, i], bins=50)
    ax[i].hist(att.iloc[:, i], bins=50, color="black", alpha=.5)
    ax[i].hist(no_att.iloc[:, i], bins=50, color="red", alpha=.5)
    ax[i].set_title(df.columns[i])
    ax[i].set_yticks(())

ax[0].set_xlabel("특성 크기")
ax[0].set_ylabel("빈도")
ax[0].legend(["이탈", "재직"], loc="best")
fig.tight_layout()
"""
# =====================================================
# dimension reduction
# =====================================================
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df)
X_scaled = scaler.transform(df)


from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled)


# =====================================================
# logistic regression
# =====================================================
from sklearn.linear_model import LogisticRegression

# All features
logistic = LogisticRegression(random_state = 0).fit(df, df.iloc[:,1])
logistic.predict(df)

print(logistic.predict_proba(df))
print(logistic.score(df, df.iloc[:,1]))

# PCA
logistic = LogisticRegression(random_state = 0).fit(X_pca, df.iloc[:,1])
logistic.predict(X_pca)

print(logistic.predict_proba(X_pca))
print(logistic.score(X_pca, df.iloc[:,1]))
