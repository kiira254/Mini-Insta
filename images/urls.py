from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.post, name = 'post'),
    
    
]
