from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("random", views.random_team),
    path('home', views.index)
    # path("search", views.search)
    
]
