from django.contrib import admin
from django.urls import path,include
from .views import dashboard,questions
urlpatterns = [
    path('dashboard/',dashboard),
    path('questions/',questions),
]
