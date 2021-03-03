from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from log.models import AddtionalDetails
from proj.models import Record,Orders,Messages
from django.db.models import Q
import json
# _appname_=proj
profession=""

#home page of web
def home(request):

	return render(request,'home/healthhome.html')

@csrf_exempt
def newmsg(request):
	user=request.user.username
	receiver=request.POST.get('id')
	mesg=request.POST.get('msg')
	msg = Messages(sender=user,receiver=receiver,message=mesg)
	msg.save()
	return HttpResponse("Sucess")
@csrf_exempt
def chatting(request):
	user=request.user.username	
	if request.method=="POST":
		other=request.POST.get('id')
		msgsend=Messages.objects.filter(Q(sender=user) & Q(receiver=other))
		msgrecv=Messages.objects.filter(Q(sender=other) & Q(receiver=user))
	# msg = Messages(sender=user,receiver="pha@a.c",message="Second Message")
	# msg.save()
		messages=[]
		for i in msgrecv:
			messages.append([i.message,i.time,0])
		for i in msgsend:
			messages.append([i.message,i.time,1])
		# print(messages)
		messages.sort(key = lambda x: x[1]) 

		msgs=[]
		for i in messages:
			msgs.append([i[0],i[2]])
		return HttpResponse(json.dumps(msgs))
	else:
		# contactlist=Messages.objects.filter(Q(sender=user)| Q(receiver=user))
		# msgrecv=Messages.objects.filter(Q(receiver=user) & Q(read=0))
		# new=len(msgrecv)
		# contacts=[]
			
		# for i in msgrecv:
		# 	contacts.append(AddtionalDetails.objects.filter(username=i.sender))

		contacts=[]
		user_rec=AddtionalDetails.objects.filter(username=user)
		global profession
		profession=(user_rec[0].profession)
			
		if profession=="user":
			contactlist=Record.objects.filter(user=user)
			for i in contactlist:
				contacts.append(AddtionalDetails.objects.filter(username=i.doctor))

		elif profession=="doctor":
			contactlist=Record.objects.filter(doctor=user)
			for i in contactlist:
				contacts.append(AddtionalDetails.objects.filter(username=i.user))

		# print(contacts)
		# print(type(contactlist))
		
		return render(request,'chat/chat.html',{'data':contacts})
#dashboard common to all user
def dashboard(request):
	
	if request.user.is_authenticated:

		username=request.user.username
		user_rec=AddtionalDetails.objects.filter(username=username)
		global profession
		profession=(user_rec[0].profession)
		# profession="doctor"
		
		if profession=="user":
			list1=[]
			requests=Record.objects.filter(user=username,status=0,adate__isnull=False)[:5]
			for i in requests:
				list1.append(AddtionalDetails.objects.filter(username=i.doctor))

			numbers=range(1,20)
			data1=zip(list1,requests,numbers)
			return render(request,'dashboard/user/user.html',{'data1':data1})
		elif profession=="doctor":
			list1=[]
			requests=Record.objects.filter(doctor=username,status=0,adate__isnull=False)[:5]
			for i in requests:
				list1.append(AddtionalDetails.objects.filter(username=i.user))

			numbers=range(1,20)
			data1=zip(list1,requests,numbers)
			
			return render(request,'dashboard/doctor/doctor.html',{'data1':data1})
		
		elif profession=="pharma":
			list1=[]
			requests=Orders.objects.filter(pharma=username,status=0,adate__isnull=False)[:5]
			for i in requests:
				list1.append(AddtionalDetails.objects.filter(username=i.user))

			numbers=range(1,20)
			data1=zip(list1,requests,numbers)
			
			return render(request,'dashboard/pharma/pharma.html',{'data1':data1})

	else:
		return redirect("/log/login")
	


	#Funtion for Show Available doctors to user and request to doctor.
	
@csrf_exempt
def reqdoc(request):

	if request.method=='POST':				#Request to doctor for an appointment

		print(request.POST)
		username=request.user.username
		userfname=request.user.get_full_name()
		doctor=request.POST.get('id')
		print(username,doctor)
		r = Record(user=username,doctor=doctor)
		r.save()
		r=AddtionalDetails.objects.get(username=doctor)
		noti=(" {user} Asked for an appointment ".format(user=userfname))
		r.notifications.append([noti,str(datetime.now())])
		r.save()
		return HttpResponse("Requested")

	else:					#show available doctors
		numbers=range(1,20)
		doctors=AddtionalDetails.objects.filter(profession='doctor')
		# doctors={}
		data=zip(numbers,doctors)
		return render(request,'dashboard/user/show_doc.html',{'data':data})


	
	#funtions for show appointments of user

@csrf_exempt
def showreq(request):
	if request.method=='POST':  #to cancel appointment
		print(request.POST)
		doctor=request.user.username
		user=request.POST.get('id')
		tid=request.POST.get('tid')
		print(user,doctor,tid)
		Record.objects.filter(id=tid).delete()
		
		# redirect("/docshowappo")
		return HttpResponse("Requested")


	else:    					#to show all appointments
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


#fuction for make appointment with user 
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




#funtion for show appointments of Doctor

@csrf_exempt
def docshowappo(request):

	if request.method=='POST': #to  cancel the appointment
		print(request.POST)
		doctor=request.user.username
		user=request.POST.get('id')
		tid=request.POST.get('tid')
		print(user,doctor,tid)
		Record.objects.filter(id=tid).delete()
		
		# redirect("/docshowappo")
		return HttpResponse("Requested")

	else:  #to show all appointments

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




#Funtion of pharmacist

@csrf_exempt
def reqpharma(request):

	if request.method=='POST':				#Request to doctor for an appointment

		print(request.POST)
		username=request.user.username
		userfname=request.user.get_full_name()
		pharma=request.POST.get('id')
		# print(username,doctor)
		r = Orders(user=username,pharma=pharma,medicines="List of medi")
		r.save()
		r=AddtionalDetails.objects.get(username=pharma)
		noti=(" {user} Placed an Order ".format(user=userfname))
		r.notifications.append([noti,str(datetime.now())])
		r.save()
		return HttpResponse("Requested")

	else:					#show available doctors
		numbers=range(1,20)
		pharmas=AddtionalDetails.objects.filter(profession='pharma')
		# doctors={}
		data=zip(numbers,pharmas)
		return render(request,'dashboard/user/show_pharma.html',{'data':data})


	
	#funtions for show appointments of user

@csrf_exempt
def showorders(request):
	if request.method=='POST':  #to cancel appointment
		print(request.POST)
		pharma=request.user.username
		user=request.POST.get('id')
		tid=request.POST.get('tid')
		print(user,pharma,tid)
		Orders.objects.filter(id=tid).delete()
		
		# redirect("/docshowappo")
		return HttpResponse("Requested")


	else:    					#to show all appointments
		username=request.user.username
		requests=Orders.objects.filter(user=username,status=0,adate__isnull=False)
		proreq=Orders.objects.filter(user=username,status=0,adate__isnull=True)
		list1=[]
		list2=[]
		for i in requests:
			list1.append(AddtionalDetails.objects.filter(username=i.pharma))
		
		for i in proreq:
			list2.append(AddtionalDetails.objects.filter(username=i.pharma))

		# print(list1)
		numbers=range(1,20)
		#zip data to display
		data1=zip(list1,requests,numbers)
		data2=zip(list2,proreq,numbers)
		print(data2)
		return render(request,'dashboard/user/show_orders.html',{'data1':data1,'data2':data2})





#fuction for make Schedule order with user 
@csrf_exempt
def pharmashoworders(request):
	if request.method=='POST':
		print(request.POST)
		pharma=request.user.username
		pharmaname=request.user.first_name
		user=request.POST.get('id')
		tid=request.POST.get('tid')
		date=request.POST.get('date')
		print(user,pharma,date)
		# sdate=date.strftime("%m/%d/%Y")

		Orders.objects.filter(id=tid,user=user,pharma=pharma).update(adate=date)
		r=AddtionalDetails.objects.get(username=user)
		noti=(" Ph.{pharma} Expect delivery of medicines on {date} ".format(pharma=pharmaname,date=date))
		r.notifications.append([noti,str(datetime.now())])
		r.save()
		return HttpResponse("Requested")

	else:
		username=request.user.username
		requests=Orders.objects.filter(pharma=username,status=0,adate__isnull=True)
		proreq=Orders.objects.filter(user=username,status=1)
		list1=[]
		for i in requests:
			list1.append([(AddtionalDetails.objects.filter(username=i.user)),(AddtionalDetails.objects.filter(username=i.pharma))])

		# print(list1)
		numbers=range(1,20)

		#zip data to display
		data1=zip(list1,requests,numbers)
		return render(request,'dashboard/pharma/show_req.html',{'data1':data1})




#funtion for show Orders (pharma function)

@csrf_exempt
def pharmashowinorders(request):

	if request.method=='POST': #to  cancel the appointment
		print(request.POST)
		pharma=request.user.username
		user=request.POST.get('id')
		tid=request.POST.get('tid')
		print(user,pharma,tid)
		Orders.objects.filter(id=tid).delete()
		
		# redirect("/docshowappo")
		return HttpResponse("Requested")

	else:  #to show all appointments

		username=request.user.username
		requests=Orders.objects.filter(pharma=username,status=0,adate__isnull=False)
		proreq=Orders.objects.filter(user=username,status=1)
		list1=[]
		for i in requests:
			list1.append([(AddtionalDetails.objects.filter(username=i.user)),(AddtionalDetails.objects.filter(username=i.pharma))])

		# print(list1)
		numbers=range(1,20)

		#zip data to display
		data1=zip(list1,requests,numbers)
		return render(request,'dashboard/pharma/show_orders.html',{'data1':data1})
