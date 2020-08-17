import numpy as np
import json
from sklearn.svm import SVC


f1 = open('F:\\ceshishuju\\test8.json',encoding='utf-8')
f2 = open('F:\\ceshishuju\\test9.json',encoding='utf-8')

dict1 = json.load(f1)
dict2 = json.load(f2)
print("代表流行dict数量：",len(dict1))
print("代表不流行dict数量：",len(dict2))
#c为X
c=[]
print("c的类型为：",type(c))
for index in range(len(dict1)-11):
    #temp迭代每条
    temp = dict1[index]
    a=temp['xiangliang_a']
    #print(a)
    c.append(a)
    #print(type(temp['xiangliang_a']))

for index in range(len(dict2)-14):
    #temp迭代每条
    temp = dict2[index]
    b=temp['xiangliang_a']
    #print(b)
    c.append(b)
    #print(type(temp['xiangliang_a']))

#print(c)


x=np.array(c)
#0代表流行，1代表不流行
#d为y
d=[]
for index in range(len(dict2)-14):
    d1=1
    d.append(d1)

for index in range(len(dict2)-14):
    d2=2
    d.append(d2)

print(d)
print("d的类型为：",type(d))
print("d的长度为：",len(d))
y=np.array(d)
clf=SVC()
clf.fit(x,y)

#p为要预测的标签
data=dict2[90]
p=data['xiangliang_a']
print("p的类型为：",type(p))
print("p是：",p)
print(clf.predict([p]))

