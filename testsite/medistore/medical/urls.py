from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path("register/", views.register, name='register'),
    path('register/register', views.register, name='login'),
    path("login", views.login, name='login'),
    path("", views.home, name='home'),
    path('addrecord', views.addrecord, name='addrecord'),
    path("add", views.add, name='add'),
    path("list", views.medicinelist, name='list'),  
    path("delete/<int:id>", views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('search', views.search,  name='search'),
    path("logout", views.logout, ) 
  
]                                                                 