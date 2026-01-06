from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
     path('add/', views.add_url, name='add_url'),
    path('list/', views.list_urls, name='list_urls'),
    path('edit/<int:id>/', views.edit_url, name='edit_url'),
    path('delete/<int:id>/', views.delete_url, name='delete_url'),
   path('<str:code>/', views.redirect_url),

]
