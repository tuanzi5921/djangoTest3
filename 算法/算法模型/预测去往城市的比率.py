import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

#读取数据
df = pd.read_excel("twoline.xlsx")
df  # data frame
df.head()
print(df)

# 将数据分为训练数据和测试数据
X = df[['cha', 'from']]
y = df['to'].values.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=41)

X_normalizer = StandardScaler() # N(0,1)
X_train = X_normalizer.fit_transform(X_train)
X_test = X_normalizer.transform(X_test)

y_normalizer = StandardScaler()
y_train = y_normalizer.fit_transform(y_train)
y_test = y_normalizer.transform(y_test)

knn = KNeighborsRegressor(n_neighbors=2)
knn.fit(X_train, y_train.ravel())
#Now we can predict prices:
y_pred = knn.predict(X_test)
y_pred_inv = y_normalizer.inverse_transform(y_pred)
y_test_inv = y_normalizer.inverse_transform(y_test)

x1=[[2,0.0025]]
print(knn.predict(x1))


# Now add the perfect prediction line
diagonal = np.linspace(0, 1, 100)
plt.plot(diagonal, diagonal, '-r')
plt.xlabel('from')
plt.ylabel('to')
plt.show()
print(y_pred_inv)

pred = knn.predict(X_test)
pred

X = df['from'].values.reshape(-1,1)
y = df['to'].values.reshape(-1,1)

reg = LinearRegression()
reg.fit(X, y)

print('a = {:.5}'.format(reg.coef_[0][0]))
print('b = {:.5}'.format(reg.intercept_[0]))

print("线性模型为: Y = {:.5}X + {:.5} ".format(reg.coef_[0][0], reg.intercept_[0]))

predictions = reg.predict(X)
x1=[[0.002]]
print(reg.predict(x1))

plt.figure(figsize=(16, 8))
plt.scatter(df['from'], df['to'], c ='black')
plt.plot(df['from'], predictions,c ='blue', linewidth=2)
plt.xlabel("from")
plt.ylabel("to")
plt.show()