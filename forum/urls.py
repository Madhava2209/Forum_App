from django.contrib import admin
from django.urls import path,include
from .views import dashboard,questions,discussion,upvote
urlpatterns = [
    path('dashboard/',dashboard),
    path('questions/',questions),
    path('discussion/<int:discussion_id>/',discussion),
    path('upvote/<int:discussion_id>/',upvote),
]
