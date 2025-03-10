# 2025.3.10
# 프로젝트2 붓꽃분류기 만들기
# 이용희 교수님과 열심히 만들어보자

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

iris_df = pd.read_csv('iris.csv')

y = iris_df['species']
X = iris_df.drop('species', axis=1)

kn = KNeighborsClassifier()
model_kn = kn.fit(X, y)

#X_new = np.array([[3,3,3,3]])
# kn['versicolor'] [[0.  0.8 0.2]]
#X_new = np.array([[5.0,3.4,1.4,0.2]])
# kn ['setosa'] #[[1. 0. 0.]]
X_new = np.array([[1,4.2,1.4,7]])
# kn ['versicolor'] [[0.2 0.6 0.2]]
prediction = model_kn.predict(X_new)
print(prediction)
probability = model_kn.predict_proba(X_new)
print(probability)