from django.shortcuts import render,redirect
from .models import Answer,Question,Upvote
# Create your views here.


def dashboard(request):
    all_question=Question.objects.all().order_by("-timestamp")
    all_answer=Answer.objects.all().order_by("-timestamp")
    return render(request,"dashboard.html",{"question":all_question,"answer":all_answer})


def questions(request):
    all_question=Question.objects.all().order_by("-timestamp")
    if request.method=="POST":
        qstn=request.POST["question"]
        user=request.user
        quest=Question.objects.create(question=qstn,author=user)
        return redirect("/dashboard/")

    return render(request,"question.html",{"question":all_question})

def discussion(request,discussion_id):
    question_instance=Question.objects.get(pk=discussion_id)
    disc=Answer.objects.filter(question=question_instance)
    if request.method=="POST":
        answer=request.POST["answer"]
        author=request.user
        upvotes=1
        question=question_instance
        answer_instance=Answer.objects.create(
            answer=answer,
            author=author,
            question=question,
            upvotes=upvotes
        )
        return redirect(f"/discussion/{discussion_id}/")

    return render(request,"discussion.html",{"question":question_instance,"discussion":disc})

def upvote(request,discussion_id):
    answer=Answer.objects.get(pk=discussion_id)
    upvotes=Upvote.objects.filter(reader=request.user,answer=answer)
    if upvotes :
        return redirect("/dashboard/")
    answer.upvotes +=1
    answer.save()
    upvotess=Upvote.objects.create(reader=request.user,answer=answer)
    return redirect("/dashboard/")

def delete_question(request,question_id):
    question_instance=Question.objects.get(pk=question_id)
    user=request.user
    author=question_instance.author
    if author==user:
        question_instance.delete()
        return redirect("/dashboard/")
    return redirect("/dashboard/")

def delete_answer(request,answer_id):
    answer_instance=Answer.objects.get(pk=answer_id)
    user=request.user
    author=answer_instance.author
    if author==user:
        answer_instance.delete()
        return redirect("/dashboard/")
    return redirect("/dashboard/")