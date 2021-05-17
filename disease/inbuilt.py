import numpy as np
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import operator

def kn(inp):
    from sklearn.neighbors import KNeighborsClassifier
    train=pd.read_csv('Training.csv',header=0)
    xtrain=train.iloc[:,:-1]
    ytrain=train.iloc[:,-1]
    test=pd.read_csv('Testing.csv',header=0)
    xtest=test.iloc[:,:-1]
    ytest=test.iloc[:,-1]
    # acc={}
    # for k in range(2,30):
    knn=KNeighborsClassifier(19)
    knn.fit(xtrain,ytrain)
    ypred=knn.predict(xtest)
    acc=accuracy_score(ypred,ytest)
    print(acc)

    input=[]
    for i in xtrain.columns:
        if(i in inp):
            input.append(1)
        else:
            input.append(0)
    # input=input[:-1]
    # print(xtest)
    pred=knn.predict(input)
    print(pred)

kn(["vomiting","nausea"])

