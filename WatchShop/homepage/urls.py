from django.contrib import admin
from django.urls import path
from .views import get_watches,create_watch

urlpatterns = [
    path('api/watches/', get_watches, name='watches-list' ),
    path('api/watches/create/', create_watch, name='create-watches-list' ),
]
