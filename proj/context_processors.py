from proj.models import AddtionalDetails,Record
from django.contrib.auth.models import User,auth
from datetime import datetime

def add_variable_to_context(request):
      if request.user.is_authenticated:
            info = AddtionalDetails.objects.get(username=request.user.username)

   
            list1=[]
            for i in info.notifications:
                  j=i[2:-2]
                  k=j.split("', '")
                  print(k[1])

                  a=datetime.strptime(k[1],'%Y-%m-%d %H:%M:%S.%f')
                  diff=datetime.now()-a 
                  # k[1]=str((diff.seconds)//60)+"  minutes ago"
                  hrs=(diff.seconds)//3600
                  if(diff.days==0):
                        k[1]=str(hrs)+"  hours ago"
                  elif hrs==0:
                        k[1]=str(hrs//60)+"  minutes ago"
                  else:
                        k[1]=str(diff.days)+"  days ago"

                  list1.append(k)
            return {'info': list1}
            
      return {'notifications': ''}