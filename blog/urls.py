from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home-page'),
    path('myposts/',views.myposts,name='myposts-page'),
    path('createpost/',views.mypost_create,name='createpost-page'),
    path('readpost/<int:pk>/',views.mypost_read,name='readpost-page'),
    path('delete/<int:pk>/',views.myposts_delete,name='delete-page'),
    path('update/<int:pk>',views.myposts_update,name='updatepost-page')
]