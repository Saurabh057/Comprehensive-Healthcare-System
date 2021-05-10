import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

import operator





def getdic(df):
    firstdic={}
    dfl=len(df)
    probsum=0
    for s in df.iloc[:,-1].unique():
        dis=df.loc[df['prognosis']==s]
        dis=dis.iloc[:,:-1]
        dislen=len(dis)
        # print(dislen)
        giv=dislen/dfl
        # print(giv)
        pdis=1
        for i in dis:
            count=0
            for j in dis[i]:
                if(j==1):
                    count+=1
            if(count!=0):
                pdis*=count/dislen
            else:
                pdis*=1/(dislen*2)
        pdis*=giv
        # print(pdis)
        firstdic[s]=pdis
        probsum+=pdis

    dic={}
    for i in df.iloc[:,-1].unique():
        # print(i)
        # print(firstdic[i])
        dic[i]=(firstdic[i]/probsum)*100
    return dic

def soln(columns):
    if('prognosis' not in columns):
        columns.append('prognosis')
    df=pd.read_csv('Training.csv', usecols=columns, header=0)
    df=df.loc[(df.iloc[:, :-1].T!=0).any()]
    df1=pd.read_csv('Testing.csv', usecols=columns, header=0)
    df1=df1.loc[(df1.iloc[:, :-1].T!=0).any()]
    dic=getdic(df)


    dic=dict(sorted(dic.items(),key=operator.itemgetter(1), reverse=True))
    print(dic)
    ypred=list(dic.keys())

    dic2=getdic(df1)
    dic2=dict(sorted(dic2.items(),key=operator.itemgetter(1), reverse=True))
    ytestk=list(dic2.keys())
    print(dic2)
    print(ypred)
    print(ytestk)
    print(accuracy_score(ypred,ytestk))


def overallaccuracy():
    test=pd.read_csv('Testing.csv', header=0)
    xtest=test.iloc[:,:-1]
    ytest=test.iloc[:,-1]
    ans=[]
    for i in range(len(xtest)):
        x=pd.DataFrame(xtest.iloc[i,:])
        inp=[]
        dic=x.to_dict()
        for key,value in dic[i].items():
            # print(value)
            if(value==1):
                inp.append(key)
        inp.append('prognosis')
        df=pd.read_csv('Training.csv', usecols=inp, header=0)
        df=df.loc[(df.iloc[:, :-1].T!=0).any()]
        dic=getdic(df)
        dic=sorted(dic.items(),key=operator.itemgetter(1), reverse=True)
        
        ans.append(dic[0][0])
    print(ans)
    print(ytest)
    print(accuracy_score(ans,ytest))

soln(['itching', 'skin_rash'])


