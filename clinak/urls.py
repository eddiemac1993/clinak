from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('clients/', views.clients, name='clients'),
    path('board/', views.board, name='board'),
]
