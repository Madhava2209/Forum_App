from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    question=models.CharField(max_length=200)
    timestamp=models.DateTimeField(auto_now=True)

class Answer(models.Model):
    answer=models.TextField()
    timestamp=models.DateTimeField(auto_now=True)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    upvotes=models.IntegerField(default=1)

class Upvote(models.Model):
    reader=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE,null=True,blank=True)

