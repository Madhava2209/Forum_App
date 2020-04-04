from django.contrib import admin
from django.urls import path,include
from .views import dashboard,questions,discussion,upvote,delete_question,delete_answer
urlpatterns = [
    path('dashboard/',dashboard),
    path('questions/',questions),
    path('discussion/<int:discussion_id>/',discussion),
    path('upvote/<int:discussion_id>/',upvote),
    path('delete_question/<int:question_id>/',delete_question),
    path('delete_answer/<int:answer_id>/',delete_answer),
]
