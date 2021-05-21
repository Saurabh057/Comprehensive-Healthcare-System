import pandas as pd
import operator
def pie():
    df=pd.read_csv("Training.csv",header=0)
    dic={}
    for i in list(df.columns)[:-1]:
        x=len(df.loc[df[i]==1])
        dic[i]=x
    dic=dict(sorted(dic.items(),key=operator.itemgetter(1), reverse=True))
    count=0
    final={}
    sum=0
    for k,v in dic.items():
        sum+=v
        final[k]=v
        if(count>4):
            break
        count+=1
    for k,v in final.items():
        final[k]=(v*100)/sum
    print(final)

def who():
    df=pd.read_csv('WHO.csv',header=0)
    for i in list(df.columns):
        print(list(df[i])[:16])
def india():
    df=pd.read_csv('india.csv', header=0,usecols=['Date', 'Cured', 'Deaths', 'Confirmed'])
    df=df.groupby('Date').sum()
    print(list(df.index))
    for i in df.columns:
        x=list(df[i])
        sum=0
        ans=[]
        for j in x:
            j-=sum
            ans.append(j)
            sum+=j
        print(ans)

    print(df)
who()

    