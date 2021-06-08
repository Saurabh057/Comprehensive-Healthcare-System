from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
	path('diagnose',views.diagnose,name='diagnose'),
	path('doclist',views.doclist,name="doclist"),
]
