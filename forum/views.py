from django.shortcuts import render,redirect
from .models import Answer,Question,Upvote
# Create your views here.


def dashboard(request):
    all_question=Question.objects.all()
    all_answer=Answer.objects.all()
    return render(request,"dashboard.html",{"question":all_question,"answer":all_answer})


def questions(request):
    all_question=Question.objects.all()
    if request.method=="POST":
        qstn=request.POST["question"]
        user=request.user
        quest=Question.objects.create(question=qstn,author=user)
        return redirect("/dashboard/")

    return render(request,"question.html",{"question":all_question})