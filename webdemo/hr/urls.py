from django.contrib import admin
from django.urls import path
from . import views, books_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('jobs/', views.list_jobs),
    path('countries/', views.list_countries),
    path('countryinfo/', views.country_info),
    path('add_job/', views.add_job),
    path('delete_job/', views.delete_job),
    path('update_job/', views.update_job),
    path('books/home/', books_views.book_home),
    path('books/list/', books_views.book_list),
    path('books/add/', books_views.book_add),
    path('books/delete/<int:id>', books_views.book_delete),
    path('books/edit/<int:id>', books_views.book_edit),

]

