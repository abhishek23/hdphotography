from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weoffer/', views.weOffer, name='weoffer'),
]
