from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('staff/', views.staff, name='staff'),
    path('contact/', views.contact, name='contact'), 
    path('success/', views.success, name='success'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),

]