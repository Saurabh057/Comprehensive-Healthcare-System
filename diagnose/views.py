from json import encoder
from django.shortcuts import render
from django.http import HttpResponse
from disease.paralleldt import dt
from django.views.decorators.csrf import csrf_exempt
import json
import disease.inbuilt as inbuilt
from disease.naivebayes import soln
from disease.knn import knn
from disease.decisiontree import decisiontree
# Create your views here.
def home(request):
    return render(request,'diagnose/newindex.html')


@csrf_exempt
def diangnose(request):
    symp=request.POST.get("symptoms")
    s=symp.split(',')
    sys=[]
    i=0
    while(i<len(s)):
        if(s[i+1]=='1'):
            sys.append(s[i])
        i=i+2
    print(sys)
    nb=soln(sys)
    # print(nb)
    accNaiveBayes = nb['acc']
    diseaseNaiveBAyes = list(nb.keys())[0] #yash bhadkahv ithe functions madhun return kr
    
    kn=knn(sys)
    # print(kn)
    accKnn = kn["acc"]
    diseaseKnn = list(kn.keys())[0]
    
    dt=decisiontree(sys)
    # print(dt)
    accDecisionTree = dt["acc"]
    diseaseDecisionTree = list(dt.keys())[0]
    
    
    
    
    if "prognosis" in sys:
        sys.remove("prognosis")
    symptoms = sys

    symptoms = str(symptoms).replace('[','').replace(']','').replace("'",'')

    disease = {
        'NBS' : ['Naive Bayes Classifier',diseaseNaiveBAyes, accNaiveBayes],
        'KNN' : ['K-Nearest Neighbors Algorithm',diseaseKnn, accKnn],
        'DTC' : ['Decision Tree Classifier',diseaseDecisionTree, accDecisionTree]
    }

    choosenAlgorithm =  max(disease, key=lambda x : disease[x][2])
    # print("Choosen Algorithm : ",choosenAlgorithm)

    chosen = {
        'choosenAlgorithm' : disease[choosenAlgorithm][0],
        'choosenDisease' : disease[choosenAlgorithm][1],
        'chosenAcc' : disease[choosenAlgorithm][2]
    }

    context = {'chosen':chosen, 'disease': disease, 'symptoms':symptoms}



    # multiple diseases
    encoder ={"NBS":nb, "KNN":kn, "DTC":dt} 

    top_diseases = encoder[choosenAlgorithm]

    # print("top-disease : ", top_diseases)
    top_diseases.pop("acc")

    # print("top-disease : ", top_diseases)
    keyss=list(top_diseases.keys())
    for k in keyss:
        if(top_diseases[k]<=0.01):
            del top_diseases[k]
    if(len(top_diseases)>4):
        for i in range(len(top_diseases)-4):
            top_diseases.popitem()
    print("top-disease : ", top_diseases)

    # print("Values : ", list(top_diseases.values()))
    # print("Keys : ", list(top_diseases.keys()))


    vals = [round(val,2) for val in top_diseases.values() ]
    context['top_diseases'] = {'diseases': dict(zip(list(top_diseases.keys()),vals)), 'names': json.dumps(list(top_diseases.keys())), 'scores':list(top_diseases.values())}
    print(context)
    return render(request, 'diagnose/diagnosedashextended.html', context)

def diangnose2(request):
    symp=request.POST.get("symptoms")
    s=symp.split(',')
    sys=[]
    i=0
    while(i<len(s)):
        if(s[i+1]=='1'):
            sys.append(s[i])
        i=i+2
    print(sys)
    nb=inbuilt.nb(sys)
    print(nb)
    accNaiveBayes = nb[0]
    diseaseNaiveBAyes = nb[1] #yash bhadkahv ithe functions madhun return kr
    
    kn=inbuilt.kn(sys)
    print(kn)
    accKnn = kn[0]
    diseaseKnn = kn[1]
    
    dt=inbuilt.dt(sys)
    print(dt)
    accDecisionTree = dt[0]
    diseaseDecisionTree = dt[1]
    
    
    
    
    if "prognosis" in sys:
        sys.remove("prognosis")
    symptoms = sys

    symptoms = str(symptoms).replace('[','').replace(']','').replace("'",'')

    disease = {
        'NBS' : ['Naive Bayes Classifier',diseaseNaiveBAyes, accNaiveBayes],
        'KNN' : ['K-Nearest Neighbors Algorithm',diseaseKnn, accKnn],
        'DTC' : ['Decision Tree Classifier',diseaseDecisionTree, accDecisionTree]
    }

    choosenAlgorithm =  max(disease, key=lambda x : disease[x][2])
    print(choosenAlgorithm)

    chosen = {
        'choosenAlgorithm' : disease[choosenAlgorithm][0],
        'choosenDisease' : disease[choosenAlgorithm][1],
        'chosenAcc' : disease[choosenAlgorithm][2]
    }

    context = {'chosen':chosen, 'disease': disease, 'symptoms':symptoms}

    return render(request, 'diagnose/diagnosedashextended.html', context)


@csrf_exempt
def suggest(request):
    x=request.POST.get("symptoms")
    x=list(map(str,x.split(',')))
    print(x)
    ans=[]
    if(x[0]==''):
        x=[]  
    ans=dt(x)
    final=[]
    # print(ans)
    if(ans ==[] or ans==['']):
        final=["nosymp"]
    else:
        count=0
        for i in ans:
            final.append(i)
            count+=1
            if(count==5):
                break
    print(json.dumps({"after":final, "before":x}))
    return HttpResponse(json.dumps({"after":final, "before":x}))

def analysis(request):
    return render(request,'diagnose/analysis.html')