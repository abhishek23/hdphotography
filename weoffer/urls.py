from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='weoffer'),
    path('slider/', views.slider, name='weoffer_slider'),
    path('events/<int:eventId>', views.eventDetail, name='event_detail'),
    path('events/stories/<int:featuredId>', views.stories, name='featured_stories'),
]
