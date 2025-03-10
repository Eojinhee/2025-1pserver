# 2025.3.10
# 프로젝트2 붓꽃분류기 만들기
# 이용희 교수님과 열심히 만들어보자
from operator import irshift

import joblib
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

iris_df = pd.read_csv('iris.csv')

y = iris_df['species']
X = iris_df.drop('species', axis=1)

kn = KNeighborsClassifier()
rfc = RandomForestClassifier()
model_kn = kn.fit(X, y)
model_rfc = rfc.fit(X, y)

joblib.dump(model_rfc, 'model_rfc.pkl')


# X_new = np.array([[3,3,3,3]])
# kn['versicolor'] [[0.  0.8 0.2]]
# rfc ['virginica'] [[0.01 0.39 0.6 ]]
X_new = np.array([[5.0,3.4,1.4,0.2]])
# kn ['setosa'] #[[1. 0. 0.]]
# rfc ['setosa'] [[1. 0. 0.]]

# X_new = np.array([[1,4.2,1.4,7]])
# kn ['versicolor'] [[0.2 0.6 0.2]]
# rfc ['setosa'] [[0.44 0.25 0.31]]

model_rfc = joblib.load('model_rfc.pkl')

# prediction = model_kn.predict(X_new)
prediction = model_rfc.predict(X_new)
print(prediction)
# probability = model_kn.predict_proba(X_new)
probability = model_rfc.predict_proba(X_new)
print(probability)