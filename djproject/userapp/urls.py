
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index),
    path('studentinfo', views.studentinfo),
    path('index/', views.index),
    path('register/', views.register),
    path('insert/', views.insert),
    path('logintask/', views.logintask),
    path('delete/', views.delete),
    path('deletetask/', views.deletetask), 
    path('edit/', views.edit),
    path('update/', views.update),
]
