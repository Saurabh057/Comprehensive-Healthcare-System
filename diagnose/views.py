from django.shortcuts import render
from django.http import HttpResponse
from disease.paralleldt import dt,decisiontree
from django.views.decorators.csrf import csrf_exempt
import json

from disease.naivebayes import soln
from disease.knn import knn
# Create your views here.
def home(request):
    return render(request,'diagnose/index.html')
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
    diseaseNaiveBAyes = nb[0] #yash bhadkahv ithe functions madhun return kr
    accNaiveBayes = nb[1]
    kn=knn(sys)
    diseaseKnn = kn[0]
    accKnn = kn[1]
    dt=decisiontree(sys)
    diseaseDecisionTree = dt[0]
    accDecisionTree = dt[1]
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

    return render(request, 'diagnose/diagnoseDash.html', context)



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
    if(ans[0]=='ans'):
        final=ans
    else:
        count=0
        for i in ans:
            final.append(i)
            count+=1
            if(count==5):
                break
    # print(json.dumps({"after":ans, "before":x}))
    return HttpResponse(json.dumps({"after":final, "before":x}))