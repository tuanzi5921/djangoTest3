from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#读取数据
df = pd.read_excel('../data/D.xlsx')
df  # data frame
df.head()
print(df)


df_学历 = df['学历'].str.get_dummies().add_prefix('学历: ')
df = pd.concat([df, df_学历], axis=1)
df.drop(columns='学历')
df

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置



matrix = df.corr()
f, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(matrix, square=True)
plt.title('offer')

# d=[(input('请输入您的GPA,项目，奖学金'))]
# d1=[list(d)]
# d=d1.reshape(-1,1)
X = df[['GPA', '项目','奖学金']].values
y = df['offer'].values.reshape(-1,1)
# X_normalizer = StandardScaler() # N(0,1)
# X_train = X_normalizer.fit_transform(X_train)
# X_test = X_normalizer.transform(X_test)
# print(X[:, 0])
# print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2003)
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# k1=clf.kneighbors(x1,return_distance=False)
# print(clf.predict(d))

plt.figure(figsize =(16,14),dpi=144)
plt.scatter(X[:,0],X[:,1],X[:,2])

# 计算准确率
from sklearn.metrics import accuracy_score
correct = np.count_nonzero((clf.predict(X_test)==y_test)==True)
#accuracy_score(y_test, clf.predict(X_test))
print ("Accuracy is: %.3f" %(correct/len(X_test)))

# 生成一些随机样本
n_points = 100
X1 = np.random.multivariate_normal([1, 50], [[1, 0], [0, 10]], n_points)
X2 = np.random.multivariate_normal([2, 50], [[1, 0], [0, 10]], n_points)
X = np.concatenate([X1, X2])
y = np.array([0] * n_points + [1] * n_points)
print(X.shape, y.shape)
# KNN模型的训练过程
clfs = []
neighbors = [1, 3, 5, 9, 11, 13, 15, 17, 19]
for i in range(len(neighbors)):
    clfs.append(KNeighborsClassifier(n_neighbors=neighbors[i]).fit(X, y))
# 可视化结果
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

f, axarr = plt.subplots(3, 3, sharex='col', sharey='row', figsize=(15, 12))
for idx, clf, tt in zip(np.product([0, 1, 2], [0, 1, 2]),
                        clfs,
                        ['KNN (k=%d)' % k for k in neighbors]):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    axarr[idx[0], idx[1]].contourf(xx, yy, Z, alpha=0.4)
    axarr[idx[0], idx[1]].scatter(X[:, 0], X[:, 1], c=y,
                                  s=20, edgecolor='k')
    axarr[idx[0], idx[1]].set_title(tt)

plt.show()