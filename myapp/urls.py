from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),

    path('main/',main,name='main'),
    path('add/',add,name='add'),
    path('delate/<int:id>', delate, name='delate'),

    path('login/',my_login,name='login'),
    path('logout/',my_logout,name='logout'),
        
]
