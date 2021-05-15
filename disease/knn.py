import numpy as np
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import time
import operator
from disease.asach import shuffle
def pred(df, collen, k):
    anslen=0
    ans={}
    for s in df.iloc[:,-1].unique():
        ans[s]=0
    while(collen>0 and anslen<=k):
        df1=df.loc[((df.iloc[:, :-1].T!=0).sum())==collen]
        df1l=len(df1)
        # print(anslen+df1l)
        unique=df1.iloc[:,-1].unique()
        collen-=1
        if(df1l+anslen<k):
            for s in unique:
                ans[s]+=len(df1.loc[df1['prognosis']==s])
            anslen+=df1l
        else:
            dic={}
            for s in unique:
                dic[s]=len(df1.loc[df1['prognosis']==s])
            while(anslen<k):
                # print(dict(sorted(ans.items(),key=operator.itemgetter(1), reverse=True)))
                diff=(k-anslen)//len(unique)
                if(diff==0):
                    for i in range(k-anslen):
                        if(dic[unique[i]]>0):
                            ans[unique[i]]+=1
                    anslen=k
                else:
                    for s in unique:
                        if(dic[s]>=diff):
                            dic[s]-=diff
                            ans[s]+=diff
                            anslen+=diff
                        else:
                            ans[s]+=dic[s]
                            anslen+=dic[s]
                            dic[s]=0
            
    for s in df.iloc[:,-1].unique():
        ans[s]=(ans[s]*100)/k
        # if(ans[s]<10):
        #     ans.pop(s)
    final=dict(sorted(ans.items(),key=operator.itemgetter(1), reverse=True))
    # print(final)
    return final

def knn(columns):
    max=0
    ans=[]
    if('prognosis' not in columns):
        columns.append('prognosis')
    collen=len(columns)-1
    df=pd.read_csv('disease/Training.csv',usecols=columns,header=0)
    df=df.loc[(df.iloc[:, :-1].T!=0).any()]
    df2=pd.read_csv('disease/Testing.csv',usecols=columns,header=0)
    df2=df2.loc[(df2.iloc[:, :-1].T!=0).any()]
    train, test = train_test_split(df, test_size=0.25, random_state=42, shuffle=True)
    start=time.clock()
    d1={}
    d2={}
    finalk=0
    for k in range(2,30): 
        dic1=pred(train,collen,k)
        dic2=pred(test,collen,k)
        # dic1=pred(df,collen,k)
        # dic2=pred(df2,collen,k)
        ypred=list(dic1.keys())
        ytest=list(dic2.keys())
        extra=ytest
        # print(ypred)
        # print(ytest)
        i=0
        while(i<len(ypred)):
            if ypred[i] not in ytest:
                # print("removed :" +ypred[i])
                dic1.pop(ypred[i])
                ypred.remove(ypred[i])
                # print(ypred)
                # print(i)
                
            else:
                # print("extra : "+ypred[i])
                extra.remove(ypred[i])
                i+=1
        # print(extra)
        for i in extra:
            # print(i)
            ytest.remove(i)
            dic2.pop(i)
        dup1=[]
        li=[]
        val=0
        for k,v in dic1.items():
            if(val!=v):
                dup1.append(li)
                li=[k]
                val=v
            else:
                li.append(k)
        if(li!= dup1[-1]):
            dup1.append(li)

        dup2=[]
        li=[]
        val=0
        for k,v in dic2.items():
            if(val!=v):
                dup2.append(li)
                li=[k]
                val=v
            else:
                li.append(k)
        if(li != dup2[-1]):
            dup2.append(li)
        # print(dup1)
        # print(dup2)

        ypred,ytest=shuffle(ypred,ytest,dup1[1:],dup2[1:])

        acc=accuracy_score(ypred,ytest)
        print(acc)
        if(acc>=max):
            finalk=k
            d1=dic1
            d2=dic2
            max=acc
            ans=ypred
    print(time.clock()-start)
    print(max*100)
    print(finalk)
    print(dic1)
    print(dic2)
    print(ans)
    return [ans[0], int(max*100)]
# knn(['vomiting','nausea'])
# print(len(df))
# print(df.loc[((df.iloc[:, :-1].T!=0).sum())==2])

    

    