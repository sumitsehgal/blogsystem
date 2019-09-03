from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index2, name="index2"),
    path('', views.index, name='index'),
    path('post/<id>/', views.individual_post, name='individual_post')
]