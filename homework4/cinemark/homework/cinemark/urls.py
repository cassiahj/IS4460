from django.urls import path, include
from .import views
from django.conf import settings

urlpatterns = [
    path('home/', views.Home.as_view(),name='home'),
    
]