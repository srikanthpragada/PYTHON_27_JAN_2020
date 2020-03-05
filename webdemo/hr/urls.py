from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('jobs/', views.list_jobs),
    path('countries/', views.list_countries),
    path('countryinfo/', views.country_info),
    path('add_job/', views.add_job),
]

