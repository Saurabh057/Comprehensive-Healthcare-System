from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

_appname_="log"
urlpatterns = [
	path('login',views.login,name="login"),
	# path('profile',views.profile,name="Show Profile"),
	path('logout',views.logout,name="logout"),
	path('signup',views.signup,name="Sign Up"),
	path('showinfo',views.showinfo,name="Show Profile"),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

