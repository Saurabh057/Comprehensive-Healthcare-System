from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mobile.naivebayes import soln
from log.models import AddtionalDetails
import json

# Create your views here.
@csrf_exempt
def diagnose(request):
    data = received_json_data=json.loads(request.body)
    symptoms=data['symptoms']
    print(symptoms)
    result=soln(symptoms)
    print(result)
    return HttpResponse(json.dumps({'result':result}))

@csrf_exempt
def doclist(request):
    doctors=AddtionalDetails.objects.filter(profession='doctor')
    x=list(doctors.values())
    dic={}
    for i in range(len(x)):
        x[i]['bdate']=str(x[i]['bdate'])
        dic[i]=x[i]
    print(dic)
    return HttpResponse(json.dumps(dic))