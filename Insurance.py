import pandas as pd

import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier

data=pd.DataFrame({
    "age":[5,45,15,55,10,3,60,68,50,70,25],
    "salary":[0,30000,0,40000,0,0,70000,100000,35000,45000,0],
    "insurance":[0,1,0,1,0,0,1,1,1,1,0]
               })

data.isnull()

data.sum()


plt.scatter(
    data['age'],
    data['salary'],
    c=data['insurance'])
plt.show()

x=data.drop('insurance',axis=1)

y=data['insurance']

knn=KNeighborsClassifier(n_neighbors=2)

knn.fit(x,y)

new=pd.DataFrame({'age':[6,15,41,63,25], 'salary':[0,0,29000,52000,22000]})

new['prediction']=knn.predict(new)

data['prediction']=knn.predict(x)
