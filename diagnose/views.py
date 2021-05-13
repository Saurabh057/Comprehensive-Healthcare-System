from django.shortcuts import render
from django.http import HttpResponse
from disease.paralleldt import dt
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,'diagnose/index.html')

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