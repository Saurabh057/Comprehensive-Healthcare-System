import numpy as np
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import operator
from disease.asach import shuffle





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
    df=pd.read_csv('disease/Training.csv', usecols=columns, header=0)
    df=df.loc[(df.iloc[:, :-1].T!=0).any()]
    # df1=pd.read_csv('disease/Testing.csv', usecols=columns, header=0)
    # df1=df1.loc[(df1.iloc[:, :-1].T!=0).any()]
    # # print(df1)
    # dic=getdic(df)
    # dic2=getdic(df1)
    train, test = train_test_split(df, test_size=0.2, random_state=42, shuffle=True)
    dic=getdic(train)
    dic2=getdic(test)

    dic=dict(sorted(dic.items(),key=operator.itemgetter(1), reverse=True))
    print(dic)
    ypred=list(dic.keys())

    
    dic2=dict(sorted(dic2.items(),key=operator.itemgetter(1), reverse=True))
    ytest=list(dic2.keys())
    print(dic2)
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
    print(dup1)
    print(dup2)

    ypred,ytest=shuffle(ypred,ytest,dup1[1:],dup2[1:])
    print()
    print(ypred)
    print(ytest)
    print()

    acc=int(accuracy_score(ypred,ytest)*100)
    print(acc)
    return [ypred[0],acc]


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
    print(ans)
    print(ytest)
    print(accuracy_score(ans,ytest))

# soln(['vomiting', 'nausea'])


