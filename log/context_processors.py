from proj.models import Record
from log.models import AddtionalDetails
from django.contrib.auth.models import User,auth
from datetime import datetime

def add_to_context(request):
      if request.user.is_authenticated:
            info = AddtionalDetails.objects.get(username=request.user.username)
            profile=info.profile
            info=info.notifications[::-1]
            list1=[]
            for i in info[:5]:
                  j=i[2:-2]
                  k=j.split("', '")
                  # print(k[1])

                  a=datetime.strptime(k[1],'%Y-%m-%d %H:%M:%S.%f')
                  diff=datetime.now()-a 
                  # k[1]=str((diff.seconds)//60)+"  minutes ago"
                  if(diff.days==0):
                        hrs=(diff.seconds)//3600
                        if hrs==0:
                              mini=(diff.seconds)//60
                              if mini==0:
                                    k[1]=str(diff.seconds)+"  Seconds ago"
                              else:
                                    k[1]=str(diff.seconds//60)+"  minutes ago"
                        else:
                              k[1]=str(hrs)+"  hours ago"

                  else:
                        k[1]=str(diff.days)+"  days ago"

                  list1.append(k)

            return {'info': list1,'profile':profile}
            
      return {'notifications': ''}