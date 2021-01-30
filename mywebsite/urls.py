from django.contrib import admin
from django.urls import path,include
from mywebsite import views

urlpatterns = [
     #for Socail alluth rest framwork
    path('accounts/', include('allauth.urls')),
    path('',views.index,name='index'),
    
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('configuration',views.Configuration,name='Configuration'),
    path('facilites',views.facilites,name='facilites'),
    path('profile',views.profile,name='profile'),
    path('contact',views.contact,name='contact'),
    path('updateprofile',views.updateprofile,name='updateprofile'),
    path('user_logout',views.user_logout),
    
    path('notice',views.notice),
   

]