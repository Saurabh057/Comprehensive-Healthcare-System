import numpy as np
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import time
import operator
from disease.asach import shuffle
from collections import OrderedDict
def pred(countdic,ans,k):
    
    anslen=0
    
    for key,v in countdic.items():
        # df1=df.loc[((df.iloc[:, :-1]==[inp]).sum())==collen]
        # print(df1)
        # df1l=len(df1)
        # print(anslen+df1l)
        v=dict(sorted(v.items(),key=operator.itemgetter(1), reverse=True))
        total=0
        for i in v.values():
            total+=i
        unique=list(v.keys())
        if(total+anslen<=k):
            # print(0)
            for s in unique:
                ans[s]+=v[s]
                v[s]=0
            anslen+=total
        else:
            while(anslen<k):
                # print(dict(sorted(ans.items(),key=operator.itemgetter(1), reverse=True)))
                diff=(k-anslen)//len(unique)
                if(diff==0):
                    for i in range(k-anslen):
                        if(v[unique[i]]>0):
                            ans[unique[i]]+=1
                            v[unique[i]]-=1
                            anslen+=1
                else:
                    # print(1)
                    for s in unique:
                        if(v[s]>=diff):
                            v[s]-=diff
                            ans[s]+=diff
                            anslen+=diff
                        else:
                            ans[s]+=v[s]
                            anslen+=v[s]
                            v[s]=0 
        if(anslen>=k):
            break
    ans=dict(sorted(ans.items(),key=operator.itemgetter(1), reverse=True))
    
    # print(k)
    # print(ans)
    
    return ans

def datapreprocessing(st,columns):
    df=pd.read_csv(st,header=0, usecols=columns)
    indices=list(df.index[(df.T!=0).any()])
    df=pd.read_csv(st,header=0)
    # print(df)
    df=df.iloc[indices]
    df=df.loc[:, (df != 0).any(axis=0)]
    # print(df)
    # col=list(df.columns)
    # df=pd.read_csv(st,header=0, usecols=col)
    # df=df.loc[(df.T!=0).any()]
    # print(df)

    inp=[]
    for i in df.columns:
        if i in columns:
            inp.append(1)
        else:
            inp.append(0)

    countdic={}
    for i in range(len(df)):
        x=list(df.iloc[i,:])
        count=0
        for j in range(len(inp)):
            if(inp[j]!=x[j]):
                count+=1
        dic={}
        if(count in countdic):
            dic=countdic[count]
            if(x[-1] in dic):
                dic[x[-1]]+=1
            else:
                dic[x[-1]]=1
        else:
            dic[x[-1]]=1
        countdic[count]=dic
    countdic=dict(OrderedDict(sorted(countdic.items())))
    # print()
    # print(countdic)
    ans={}
    for s in df.iloc[:,-1].unique():
        ans[s]=0
    return countdic, ans


def knn(columns):
    start=time.clock()

    
    countdic1, answer1 = datapreprocessing('disease/Training.csv',columns)
    countdic2,answer2 = datapreprocessing('disease/Testing.csv',columns)
    # train, test = train_test_split(df, test_size=0.25, random_state=42, shuffle=True)

    # collen=len(list(df.columns))-1
    max=0
    ans=[]
    d1={}
    d2={}
    finalk=0
    for kth in range(2,30): 
        # dic1=pred(train,collen,k)
        # dic2=pred(test,collen,k)
        dic1=pred(countdic1, answer1,kth)
        dic2=pred(countdic2,answer2,kth)
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
        val=-1
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
        val=-1
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
        # print(acc)
        if(acc>=max):
            finalk=kth
            d1=dic1
            d2=dic2
            max=acc
            ans=ypred
    # print(time.clock()-start)
    print(max*100)
    print(finalk)
    print(d1)
    print(d2)
    print(ans)
    count = 0
    filtered={}
    su=0
    # print('ans : ' +str(ans))
    for k,v in d1.items():
        if(count>4):
            break
        filtered[k]=v
        su+=v
        count+=1
    # print('filtered : ' +str(filtered))
    for k,v in filtered.items():
        filtered[k]=(v*100)/su
        # if(ans[s]<10):
        #     ans.pop(s)
    
    final=dict(sorted(filtered.items(),key=operator.itemgetter(1), reverse=True))
    
    final['acc']=int(max*100)
    print(final)
    return final
# knn(['vomiting','nausea'])
# print(len(df))
# print(df.loc[((df.iloc[:, :-1].T!=0).sum())==2])

    

    