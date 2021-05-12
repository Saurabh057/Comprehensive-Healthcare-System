import numpy as np
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import operator

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
    return list(final.keys())

def knn(columns):
    max=0
    ans=[]
    if('prognosis' not in columns):
        columns.append('prognosis')
    collen=len(columns)-1
    df=pd.read_csv('Training.csv',usecols=columns,header=0)
    df=df.loc[(df.iloc[:, :-1].T!=0).any()]
    # train, test = train_test_split(df, test_size=0.25, random_state=42, shuffle=True)
    for k in range(2,30):
        
        # ypred=pred(train,collen,k)
        # ytest=pred(test,collen,k)

        ypred=pred(df,collen,k)
        df2=pd.read_csv('Testing.csv',usecols=columns,header=0)
        df2=df2.loc[(df2.iloc[:, :-1].T!=0).any()]
        ytest=pred(df2,collen,k)
        acc=accuracy_score(ypred,ytest)
        # print(acc)
        if(acc>=max):
            max=acc
            ans=ypred
    print(max*100)
    print(ans)
knn(['itching','red_spots_over_body'])
# print(len(df))
# print(df.loc[((df.iloc[:, :-1].T!=0).sum())==2])

    

    