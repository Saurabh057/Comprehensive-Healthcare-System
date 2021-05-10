import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import operator

columns=['continuous_sneezing','shivering','chills','prognosis']
df=pd.read_csv('Training.csv', usecols=columns, header=0)

df=df.loc[(df.iloc[:, :-1].T!=0).any()]
# print(df)
xtrain=df.iloc[:,:-1]
ytrain=df.iloc[:,-1]
df1=pd.read_csv('Testing.csv', usecols=columns, header=0)
df1=df1.loc[(df1.iloc[:, :-1].T!=0).any()]
# print(df1)
xtest=df1.iloc[:,:-1]
ytest=df1.iloc[:,-1]

labelencoder = LabelEncoder()
# ytrain=labelencoder.fit_transform(ytrain)
# ytest=labelencoder.fit_transform(ytest)

nb=MultinomialNB()
nb.fit(xtrain,ytrain)
yprednb=nb.predict(xtest)
print(yprednb)
print(ytest)
print(nb.predict([[1,1,1]]))
print(accuracy_score(ytest,yprednb))

# k_range = range(1,26)
# scores = {}
# scores_list = []
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k) 
#     knn.fit(xtrain,ytrain)
#     ypredknn=knn.predict(xtest)
#     scores[k]=accuracy_score(ytest,ypredknn)
#     scores_list.append(accuracy_score(ytest,ypredknn))
# print(scores)
# print(scores_list)
knn = KNeighborsClassifier(n_neighbors=7) 
knn.fit(xtrain,ytrain)
ypredknn=knn.predict(xtest)
print(nb.predict([[1,1,1]]))
print(accuracy_score(ytest,ypredknn))

lr = LogisticRegression()
lr.fit(xtrain,ytrain)
ypredlr = lr.predict(xtest)
print(nb.predict([[1,1,1]]))
print(accuracy_score(ytest,ypredlr))

