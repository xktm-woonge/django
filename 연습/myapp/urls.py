from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('creat/', views.create),
    path('read/<id>', views.read)
]