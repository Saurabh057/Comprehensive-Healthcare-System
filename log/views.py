from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from log.models import AddtionalDetails

def login(request):

	if(request.method=='POST'):
		username=request.POST.get('usrid')
		password=request.POST.get('pass')
		print(username,password)
		user=authenticate(request,username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect("/dashboard")
				
		else:
			messages.info(request,'Invalid Credentials..')
			return redirect("login")			
		
	else:
		return render(request,'profile/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
	
	if request.method=="POST":
		username=request.POST.get('usrid')
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		phone=request.POST.get('phone')
		bdate=request.POST.get('bdate')
		address=request.POST.get('address')
		city=request.POST.get('city')
		pin=request.POST.get('pin')
		gender=request.POST.get('gender')
		profession=request.POST.get('profession')
		password=request.POST.get('pass')
		noti=[]
		name=first_name+" "+last_name
		if(User.objects.filter(username=username).exists()):
			messages.info(request,'Username already Taken')
			return HttpResponseRedirect("signup")
		else:
			user = User.objects.create_user(username=username, password=password,email=username, first_name =first_name, last_name = last_name)
			user.save()

			details = AddtionalDetails(username=username,name=name,phone=phone,bdate=bdate,address=address,city=city,pin=pin,gender=gender,profession=profession,notifications=noti)
			details.save()
			return HttpResponseRedirect('login')
	
	else:

		return render(request,'profile/register.html')

def showinfo(request):

	username=request.user.username
	details=AddtionalDetails.objects.filter(username=username)
	print(details)
	return render(request,'profile/showinfo.html',{'details':details})

def FileFieldView(request):
		files = request.FILES.getlist('file_field')

		if True:
			for f in files:
				fileName = f.name 
				path = 'static/media/'+fileName
				dest = open(path,'wb+')

				for chunk in f.chunks():
				    dest.write(chunk)
				dest.close()

				fileName = ImageProcessing(path, fileName)

				path = "activities/media/" + fileName
				# imageBlob = bucket.blob("image.jpg")
				# imageBlob.upload_from_filename(path)
				# print(imageBlob)
				#path=ImageProcessing(path, fileName)
				recentUploads.append(path)


				#adding image path and datetime in database..
				global db
				datee = datetime.datetime.now()
				x = (str(datee.year)+str(datee.month)+str(datee.day))
				upData = {
				    u'path' : path,
				    u'date' : x
				}
				db.collection('activities').document('csf').collection('Gallery').add(upData)
      
                ###   
			return redirect('../studentAdmin_dashboard_galary')
