from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

from proj.models import AddtionalDetails,Record
# _appname_=proj
profession=""
def home(request):

	return render(request,'home/healthhome.html')


def dashboard(request):
	username=request.user.username
	user_rec=AddtionalDetails.objects.filter(username=username)
	global profession
	profession=(user_rec[0].profession)
	# profession="doctor"
	
	if profession=="user":
		list1=[]
		requests=Record.objects.filter(user=username,status=0,adate__isnull=False)
		for i in requests:
			list1.append(AddtionalDetails.objects.filter(username=i.doctor))

		numbers=range(1,20)
		data1=zip(list1,requests,numbers)
		return render(request,'dashboard/user/user.html',{'data1':data1})
	elif profession=="doctor":
		return render(request,'dashboard/doctor/doctor.html')
	
	
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

@csrf_exempt
def reqdoc(request):

	if request.method=='POST':
		print(request.POST)
		username=request.user.username
		doctor=request.POST.get('id')
		print(username,doctor)
		r = Record(user=username,doctor=doctor)
		r.save()
		return HttpResponse("Requested")
	else:
		numbers=range(1,20)
		doctors=AddtionalDetails.objects.filter(profession='doctor')
		# doctors={}
		data=zip(numbers,doctors)
		return render(request,'dashboard/user/show_doc.html',{'data':data})

@csrf_exempt
def showreq(request):
	if request.method=='POST':
		print(request.POST)
		doctor=request.user.username
		user=request.POST.get('id')
		tid=request.POST.get('tid')
		print(user,doctor,tid)
		Record.objects.filter(id=tid).delete()
		
		# redirect("/docshowappo")
		return HttpResponse("Requested")
	else:
		username=request.user.username
		requests=Record.objects.filter(user=username,status=0,adate__isnull=False)
		proreq=Record.objects.filter(user=username,status=0,adate__isnull=True)
		list1=[]
		list2=[]
		for i in requests:
			list1.append(AddtionalDetails.objects.filter(username=i.doctor))
		
		for i in proreq:
			list2.append(AddtionalDetails.objects.filter(username=i.doctor))

		# print(list1)
		numbers=range(1,20)
		#zip data to display
		data1=zip(list1,requests,numbers)
		data2=zip(list2,proreq,numbers)
		print(data2)
		return render(request,'dashboard/user/show_req.html',{'data1':data1,'data2':data2})


@csrf_exempt
def docshowreq(request):
	if request.method=='POST':
		print(request.POST)
		doctor=request.user.username
		docname=request.user.first_name
		user=request.POST.get('id')
		tid=request.POST.get('tid')
		date=request.POST.get('date')
		print(user,doctor,date)
		# sdate=date.strftime("%m/%d/%Y")

		Record.objects.filter(id=tid,user=user,doctor=doctor).update(adate=date)
		r=AddtionalDetails.objects.get(username=user)
		noti=("Dr {doctor} Sceduled an appointent on {date} ".format(doctor=docname,date=date))
		r.notifications.append([noti,str(datetime.now())])
		r.save()
		return HttpResponse("Requested")

	else:
		username=request.user.username
		requests=Record.objects.filter(doctor=username,status=0,adate__isnull=True)
		proreq=Record.objects.filter(user=username,status=1)
		list1=[]
		for i in requests:
			list1.append([(AddtionalDetails.objects.filter(username=i.user)),(AddtionalDetails.objects.filter(username=i.doctor))])

		# print(list1)
		numbers=range(1,20)

		#zip data to display
		data1=zip(list1,requests,numbers)
		return render(request,'dashboard/doctor/show_req.html',{'data1':data1})

@csrf_exempt
def docshowappo(request):
	if request.method=='POST':
		print(request.POST)
		doctor=request.user.username
		user=request.POST.get('id')
		tid=request.POST.get('tid')
		print(user,doctor,tid)
		Record.objects.filter(id=tid).delete()
		
		# redirect("/docshowappo")
		return HttpResponse("Requested")

	else:

		username=request.user.username
		requests=Record.objects.filter(doctor=username,status=0,adate__isnull=False)
		proreq=Record.objects.filter(user=username,status=1)
		list1=[]
		for i in requests:
			list1.append([(AddtionalDetails.objects.filter(username=i.user)),(AddtionalDetails.objects.filter(username=i.doctor))])

		# print(list1)
		numbers=range(1,20)

		#zip data to display
		data1=zip(list1,requests,numbers)
		return render(request,'dashboard/doctor/show_appo.html',{'data1':data1})
