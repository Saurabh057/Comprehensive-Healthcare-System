from django.shortcuts import render
from django.http import HttpResponse
from disease.paralleldt import dt
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,'diagnose/index.html')

def diangnose(request):
  
    diseaseNaiveBAyes = "Tuberculosis" #yash bhadkahv ithe functions madhun return kr
    accNaiveBayes = 100
    diseaseKnn = "TuberCulosis"
    accKnn = 86
    diseaseDecisionTree = "Asthma"
    accDecisionTree = 94

    symptoms = ["itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering"]

    symptoms = str(symptoms).replace('[','').replace(']','').replace("'",'')

    disease = {
        'NBS' : ['Naive Bayes Classifier',diseaseNaiveBAyes, accNaiveBayes],
        'KNN' : ['K-Nearest Neighbors Algorithm',diseaseKnn, accKnn],
        'DTC' : ['Decision Tree Classifier',diseaseDecisionTree, accDecisionTree]
    }

    choosenAlgorithm =  max(disease, key=lambda x : disease[x][1])

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
        ans=dt([])
    else:
        ans=dt(x)
    if(ans[0]=='ans'):
        final='ans,'+ans[1]+','
    else:
        count=0
        final=''
        for i in ans:
            final+=i+','
            count+=1
            if(count==5):
                break
    print(final[:-1])
    return HttpResponse(final[:-1])