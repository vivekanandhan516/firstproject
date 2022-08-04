
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('register/', views.register),
    path('insert/', views.insert),
    path('logintask/', views.logintask),
    path('home/', views.home),
]
