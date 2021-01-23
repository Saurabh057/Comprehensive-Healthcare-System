from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
	path('',views.home,name="index"),
	path('dashboard',views.dashboard,name="index"),
	path('login',views.login,name="login"),
	path('logout',views.logout,name="logout"),
	path('signup',views.signup,name="Sign Up"),
	path('reqdoc',views.reqdoc,name="Request Doctor user"),
	path('showreq',views.showreq,name="Show Requests user"),
	path('docshowreq',views.docshowreq,name="Show Pending Requests to docor"),
	path('docshowappo',views.docshowappo,name="Show Appoinments of  docor"),
]
