from django.urls import path
from django.contrib import admin
from workout import views 

app_name = 'workout'

urlpatterns = [
	path('', views.index, name='index.html'), # Index url

]