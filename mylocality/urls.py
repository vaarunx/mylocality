from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('', views.home),
    path('test/' , views.test),
    path('random/' , views.random),
    path('maps/' , views.mappingPlaces),


]