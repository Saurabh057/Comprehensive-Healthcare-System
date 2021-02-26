from django.contrib import admin
from django.urls import path,include
from . import views
_appname_="log"
urlpatterns = [
	path('login',views.login,name="login"),
	# path('profile',views.profile,name="Show Profile"),
	path('logout',views.logout,name="logout"),
    path('SaveMe', views.FileFieldView, name = 'SaveMe'),
	path('signup',views.signup,name="Sign Up"),
	path('showinfo',views.showinfo,name="Show Profile"),
]



