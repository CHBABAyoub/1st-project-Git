from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.Index,name='index'),
]