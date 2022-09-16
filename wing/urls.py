from django.urls import path
from . import views

urlpatterns = [
    path('', views.winglist, name='winglist'),
    path('<int:id><slug:slug>/', views.wing_detail, name='wing_detail'),
    path('search_courses', views.search_courses, name='search_courses'),   
]