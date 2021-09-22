from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room>/', views.room, name='room'),
    path('checkroom', views.checkroom, name='checkroom'),
    path('send', views.send, name='send'),
    path('getmessages/<str:room>/', views.getMessages, name='getMessages'),
]