from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('', views.index, name='index'),
    path('about-me', views.about_me, name='about_me'),
]