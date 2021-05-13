import numpy as np
import pandas as pd
import time
import concurrent
# from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import math
import operator
from multiprocessing import Process,Manager

def entropycalc(i,df):
    print("starting : "+i)
    # entropy[i]=[[0,0]]
    lis=[i]
    psum=0
    asum=0
    for s in df.iloc[:,-1].unique():
        p=len(df.loc[(df['prognosis']==s) & (df[i]==1)])
        a=len(df.loc[(df['prognosis']==s) & (df[i]==0)])
        li=[p,a]
        lis.append(li)
        psum+=p
        asum+=a
    li=[psum,asum]
    lis.append(li)
    print("exiting : "+ i)
    return lis

def parallel(col,df):
    entropy={}
    executor = concurrent.futures.ProcessPoolExecutor()
    futures = [executor.submit(entropycalc, group,df) 
           for group in col]
    # concurrent.futures.wait(futures)
    for future in concurrent.futures.as_completed(futures):
        res=future.result()
        entropy[res[0]]=res
    return entropy

def pred(df,inp):
    print(inp)
    if (inp!=[]):
        i=0
        while(i<len(inp)):
            # print(inp[i])
            # print(inp[i+1])
            # print(df)
            if(inp[i] in list(df.columns)):
                if(len(df.iloc[:,-1].unique())==1):
                    x=str(df.iloc[0,-1])
                    return {'ans':0,x:'2'}
                df=df.loc[df[inp[i]]==int(inp[i+1])]
                if(inp[i] in list(df.columns)):
                    df.pop(inp[i])
            i+=2
        df=df.loc[:, (df != 0).any(axis=0)]
        
    col=list(df.columns)
    col.remove('prognosis')
    print(col)
    # print(len(df))
    # disease_prob={}
    current_entropy=0
    dfl=len(df)
    for s in df.iloc[:,-1].unique():
        k=len(df.loc[df['prognosis']==s])
        # disease_prob[s]=k/dfl
        mul=(-k/dfl)*(math.log(k/dfl,2))
        current_entropy+=mul

    # entropy=Manager().dict()
    # processes=[]
    # for i in col[:10]:
    #     p=Process(target=entropycalc,args=(df,i,entropy))  
    #     p.start() 
    #     processes.append(p)   
    # for j in processes:
    #     j.join()
    entropy=parallel(col,df)
    
    


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
    # if(val[0]==0.0):
    #     x=str(df.iloc[0,-1])
    #     return {'ans':0,x:'2'}
    # disease_prob=sorted(disease_prob.items(),key=operator.itemgetter(1), reverse=True)
    print(ans)
    # print(disease_prob)
    return ans
# def decision_tree(inp):
    
    
def dt(inp):
    start_time=time.clock()
    print(start_time)
    entropy={}
    df=pd.read_csv('disease/Training.csv', header=0)
    dic1=pred(df,inp)
    # df1=pd.read_csv('disease/Testing.csv', header=0)
    # dic2=pred(df1,inp)
    # acc=accuracy_score(list(dic1.keys()),list(dic2.keys()))
    ans=list(dic1.keys())
    print(ans)
    print(time.clock()-start_time)
    # ans.append(acc)
    return ans
    # decision_tree([])


if __name__=="__main__":
    print("in")
    # dt([])
        


        


    