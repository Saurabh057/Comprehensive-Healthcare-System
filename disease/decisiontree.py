import numpy as np
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import math
import time
import operator
from disease.asach import shuffle 
def pred(df,inp):
    print(inp)
    
    if (inp!=[]):
        i=0
        while(i<len(inp)):
            print(inp[i])
            print(inp[i+1])
            df=df.loc[df[inp[i]]==int(inp[i+1])]
            df.pop(inp[i])
            i+=2
        df=df.loc[:, (df != 0).any(axis=0)]
    col=list(df.columns)
    col.remove('prognosis')
    print(col)
    # print(len(df))
    entropy={}
    # disease_prob={}
    current_entropy=0
    dfl=len(df)
    for s in df.iloc[:,-1].unique():
        k=len(df.loc[df['prognosis']==s])
        # disease_prob[s]=k/dfl
        mul=(-k/dfl)*(math.log(k/dfl,2))
        current_entropy+=mul

    for i in col:
        entropy[i]=[[0,0]]
        psum=0
        asum=0
        for s in df.iloc[:,-1].unique():
            p=len(df.loc[(df['prognosis']==s) & (df[i]==1)])
            a=len(df.loc[(df['prognosis']==s) & (df[i]==0)])
            li=[p,a]
            entropy[i].append(li)
            psum+=p
            asum+=a
        li=[psum,asum]
        entropy[i].append(li)
    # print(entropy)
    ans={}
    for i in col:
        li=entropy[i]
        pent=0
        aent=0
        final=entropy[i][-1]
        # print(final)
        for j in range(1,len(li)-1):
            if(li[j][0]!=0):
                pent+=(-li[j][0]/final[0])*math.log((li[j][0]/final[0]),2)
            if(li[j][1]!=0):
                aent+=(-li[j][1]/final[1])*math.log((li[j][1]/final[1]),2)
        x=((pent*final[0])/dfl)
        x+=((aent*final[1])/dfl)
        fi=current_entropy-x
        ans[i]=fi
    ans=dict(sorted(ans.items(),key=operator.itemgetter(1), reverse=True))
    val=list(ans.values())
    if(val[0]==0.0):
        x=str(df.iloc[0,-1])
        return {'ans':0,x:'2'}

    # disease_prob=sorted(disease_prob.items(),key=operator.itemgetter(1), reverse=True)
    print(ans)
    # print(disease_prob)
    return ans
def decision_tree(inp):
    start_time=time.clock()
    df=pd.read_csv('disease/Training.csv', header=0)
    dic1=pred(df,inp)
    # df1=pd.read_csv('disease/Testing.csv', header=0)
    # dic2=pred(df1,inp)
    # acc=accuracy_score(list(dic1.keys()),list(dic2.keys()))
    ans=list(dic1.keys())
    # ans.append(acc)
    print(time.clock()-start_time)
    return ans


def getlist(df):
    
    dfl=len(df)
    final={}
    for s in df.iloc[:,-1].unique():
        final[s]=len(df[df["prognosis"]==s])
    ans=dict(sorted(final.items(),key=operator.itemgetter(1), reverse=True))
    count = 0
    filtered={}
    su=0
    # print('ans : ' +str(ans))
    for k,v in ans.items():
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
    # print(final)
    return final

def decisiontree(symps):
    # print("in decision tree")
    if "prognosis" in symps:
        symps.remove("prognosis")
    df=pd.read_csv('disease/Training.csv', header=0)
    # dic1=getlist(df,symps)
    for i in symps:
        if(len(df.iloc[:,-1].unique())==1):
            x=str(df.iloc[0,-1])
            return {x:100, "acc":100}
        if i in list(df.columns): 
            df=df.loc[df[i]==1]
            df=df.loc[:, (df != 0).any(axis=0)]
    train, test = train_test_split(df, test_size=0.2, random_state=42, shuffle=True)
    dic1=getlist(train)
    dic2=getlist(test)
    # print(dic1)
    ypred=list(dic1.keys())
    ytest=list(dic2.keys())
    extra=ytest
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
    acc=int(accuracy_score(ypred,ytest)*100)
    # print(acc)
    dic1['acc']=acc
    # print("desision tree: " +str(dic1))
    return dic1

# decision_tree([])
    
        


        


    