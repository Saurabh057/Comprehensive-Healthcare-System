import numpy as np
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import operator
from disease.asach import shuffle

import time



def getdic(df,inp):
    # print(inp)
    firstdic={}
    dfl=len(df)
    probsum=0
    for s in df.iloc[:,-1].unique():
        dis=df.loc[df['prognosis']==s]
        dis=dis.iloc[:,:-1]
        dislen=len(dis)
        # print(dislen)
        # print(giv)
        pdis=[]
        flag=0
        for i in dis:
            count=0
            for j in dis[i]:
                if(j==inp[j]):
                    count+=1
            if(count==0):
                flag=1
            pdis.append(count)
                # pdis*=count/dislen
            # else
                # pdis*=1/(dislen*2)
        final_prob=1
        asach=0
        # print(s)
        if(flag==0):
            for i in range(len(pdis)):
                x=pdis[i]/dislen
                # if(inp[i]==1):
                #     x*=2
                final_prob*=x
                
        else:
            dislen+=1
            for i in range(len(pdis)):
                x=(pdis[i]+1)/dislen
                # if(inp[i]==1):
                #     x*=2
                final_prob*=x
        # print(asach)
        final_prob*=dislen/dfl
        # print(pdis)
        firstdic[s]=final_prob
        probsum+=final_prob
    firstdic=dict(sorted(firstdic.items(),key=operator.itemgetter(1), reverse=True))
    print(firstdic)
    
    return firstdic

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
    return df,inp[:-1]

def soln(columns):
    start=time.clock()
    df,inp=datapreprocessing('disease/Training.csv',columns)
    # print(df.columns)
    # print(df)
    dic=getdic(df,inp)
    # print(dic)


    # df1=pd.read_csv('disease/Testing.csv', usecols=columns, header=0)
    # df1=df1.loc[(df1.iloc[:, :-1].T!=0).any()]
    # print(df1)
    
    df1,inp=datapreprocessing('disease/Testing.csv',columns)
    dic2=getdic(df1,inp)
    # print(dic2)
    # train, test = train_test_split(df, test_size=0.2, random_state=42, shuffle=True)
    # dic=getdic(train)
    # dic2=getdic(test)

    # dic=dict(sorted(dic.items(),key=operator.itemgetter(1), reverse=True))
    # print(dic)
    ypred=list(dic.keys())

    
    # dic2=dict(sorted(dic2.items(),key=operator.itemgetter(1), reverse=True))
    ytest=list(dic2.keys())
    # print(dic2)
    i=0
    extra=ytest
    while(i<len(ypred)):
        if ypred[i] not in ytest:
            # print("removed :" +ypred[i])
            dic.pop(ypred[i])
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
    for k,v in dic.items():
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
    # print()
    # print(ypred)
    # print(ytest)
    # print()

    acc=int(accuracy_score(ypred,ytest)*100)
    count = 0
    filtered={}
    su=0
    # print('ans : ' +str(ans))
    for k,v in dic.items():
        if(count>3):
            break
        filtered[k]=v
        su+=v
        count+=1
    # print("naive :  "+str(firstdic))
    for k,v in filtered.items():
        filtered[k]=(v*100)/su
        # if(ans[s]<10):
        #     ans.pop(s)
    final=dict(sorted(filtered.items(),key=operator.itemgetter(1), reverse=True))
    # print(acc)
    final['acc']=acc
    print(final)
    print(time.clock()-start)
    return final


def overallaccuracy():
    test=pd.read_csv('disease/Testing.csv', header=0)
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
        df=pd.read_csv('disease/Training.csv', usecols=inp, header=0)
        df=df.loc[(df.iloc[:, :-1].T!=0).any()]
        dic=getdic(df)
        dic=sorted(dic.items(),key=operator.itemgetter(1), reverse=True)
        
        ans.append(dic[0][0])
    # print(ans)
    # print(ytest)
    # print(accuracy_score(ans,ytest))

# soln(['fatigue','cough','loss_of_smell','headache'])


