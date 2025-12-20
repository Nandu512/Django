from django.contrib import admin
from django.urls import path
from books import views
urlpatterns = [
    path('', views.greeting,name='home'),
    path('about-us', views.aboutUs,name='about-us'),
    path('pages/<str:title>/', views.page,name='page'),
    path('count/<int:num>/', views.count,name='count')
]