import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import operator

columns=['continuous_sneezing','shivering','chills', 'prognosis']
colcount=len(columns)-1
df=pd.read_csv('Training.csv', usecols=columns, header=0)
df=df.loc[(df.iloc[:, :-1].T!=0).any()]
xtrain=df.iloc[:,:-1]
ytrain=df.iloc[:,-1]
df1=pd.read_csv('Testing.csv', usecols=columns, header=0)
xtest=df.iloc[:,:-1]
ytest=df.iloc[:,-1]
labelencoder = LabelEncoder()
ytrain=labelencoder.fit_transform(ytrain)
ps = 1

psli=[]
dfl=len(df)
print(dfl)
for i in xtrain:
    count=0
    # print(df[[i]])
    # li=list(df[i])
    for j in df[i]:
        if(j==1):
            count+=1
    if(count==0):
        count=1
    psli.append(count)
    # ps*=count/dfl
    ps*=count/dfl
print(ps)
print(psli)
def probcalc(s):
    dis=df.loc[df['prognosis']==s]
    dis=dis.iloc[:,:-1]
    dislen=len(dis)
    print(dislen)
    giv=dislen/(dfl)
    print(giv)
    pdis=1
    itr=0
    for i in dis:
        count=0
        # li=list(dis[i])
        for j in dis[i]:
            if(j==1):
                count+=1
        if(count!=0):
            # pdis*=count/psli[itr]
            pdis*=count/dislen
        else:
            # pdis*=1/psli[itr]
            pdis*=1/dislen
        itr+=1
    print(pdis)
    return (pdis*giv)/ps
dic={}
for i in df.iloc[:,-1].unique():
    print(i)
    dic[i]=probcalc(i)*100
print(sorted(dic.items(),key=operator.itemgetter(1), reverse=True))




