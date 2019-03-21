from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lecture

# Create your views here.
def index(req):
    context = {
        "courses": Lecture.objects.all()
    }
    return render(req, 'lectures/index.html', context)

def show(req, lecture_id):
    context = {
        "course": Lecture.objects.get(id=lecture_id)
    }
    return render(req, 'lectures/show.html', context)

def create(req):
    errors = Lecture.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
    else:
        Lecture.objects.easy_create(req.POST)
    return redirect('lectures:index')

def edit(req, lecture_id):
    context = {
        'course': Lecture.objects.get(id=lecture_id)
    }
    return render(req, "lectures/edit.html", context)

def update(req, lecture_id):
    errors = Lecture.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect("/" + lecture_id + "/edit")
    else:
        Lecture.objects.easy_update(req.POST, lecture_id)
    return redirect('lectures:index')
    # return redirect(f"/{lecture_id}/edit")
    # return redirect("lectures:edit", lecture_id=lecture_id)

def destroy(req, lecture_id):
    lecture = Lecture.objects.get(id=lecture_id)
    lecture.delete()
    return redirect('lectures:index')