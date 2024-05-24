import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\User\Downloads\child_iq.csv")
df.isnull().sum()
df.head()
df.tail()
df3=df[(df["ppvt"]<140)]
df3.shape
sns.boxplot((df3.ppvt))
df4=df3[(df["ppvt"]<=10)]

df.shape
df.describe()




import numpy as np
from sklearn.model_selection import train_test_split
y= 2*np.random.rand(400,0)
x=3*x+2+np.random.rand(400,0)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)















import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(data= df[["dis","medv"]])
df.describe()