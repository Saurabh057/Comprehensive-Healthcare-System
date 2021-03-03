from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.files.storage import FileSystemStorage
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
			dirname="static/media/"+username
			if not os.path.exists(os.path.join(BASE_DIR, dirname)):
				os.mkdir(os.path.join(BASE_DIR, dirname))

			return HttpResponseRedirect('login')
	
	else:

		return render(request,'profile/register.html')

def showinfo(request):
	# print(request.FILES)
	if request.method == 'POST': 
		username=request.user.username
		img=request.FILES['profile_Img']
		
		img_extension = os.path.splitext(img.name)[1]

		user_folder = 'static/media/' + str(request.user.username)
		if not os.path.exists(user_folder):
			os.mkdir(user_folder)

		img_save_path =  user_folder+'/profile'+ img_extension
		with open(img_save_path, 'wb+') as f:
			for chunk in img.chunks():
				f.write(chunk)
		img_save_path =  'media/'+str(request.user.username)+'/profile'+ img_extension

		AddtionalDetails.objects.filter(username=username).update(profile=img_save_path)

		return redirect('/log/showinfo') 

	else: 
		# form = ProfileForm() 
		username=request.user.username
		details=AddtionalDetails.objects.filter(username=username)

		return render(request,'profile/showinfo.html',{'details':details})

def FileFieldView(request):
		files = request.FILES.getlist('file_field')
		print("Inside save me")
		for file in files:
			user=request.user.username
			print(user)
			file = request.FILES.get('file')
			print(file)
			filename='profile.jpeg'
			path = 'static/media/'+user+'/'+filename
			print(path)
			dest = open(path,'wb+')
			print(file.name)
			for chunk in file.chunks():
				dest.write(chunk)
			dest.close()

			fileName = ImageProcessing(path, fileName)

			path = "activities/media/" + fileName

			    ###   
		return redirect('/log/showinfo')
