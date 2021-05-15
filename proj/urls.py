from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
	#common to all users
	path('',views.home,name="index"),
	path('dashboard',views.dashboard,name="index"),
	path('chatting',views.chatting,name="chat"),
	path('newmsg',views.newmsg,name="New Message"),
	# path('videomeet',views.videomeet,name="Video Meeting"),

	#doctor urls for user 
	path('reqdoc',views.reqdoc,name="Request Doctor user"),
	path('showreq',views.showreq,name="Show Doctors available to user"),
	# path('completedreq',views.completedreq,name="Place Order"),
	
	#doctor urls
	path('docshowreq',views.docshowreq,name="Show Pending Requests to docor"),
	path('docshowappo',views.docshowappo,name="Show Appoinments of  docor"),
	# path('prescription',views.prescription,name="Write prescription"),

	#pharma urls for user
	path('reqpharma',views.reqpharma,name="place order to pharma"),
	path('showorders',views.showorders,name="Show Pharmacist available to user"),
	

	#pharma urls

	path('pharmashoworders',views.pharmashoworders,name="Show Pending Orders to Pharmacist"),
	path('pharmashowinorders',views.pharmashowinorders,name="Show In processs Orders"),
	# path('generatebill',views.generatebill,name="generatebill"),



	# path('renderpdf',views.render_pdf_view,name="Show In processs Orders"),
	path('printbill',views.printbill,name="Print bill of order"),



]

