from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(req):
    context = {
        "users": User.objects.all()
    }
    return render(req, 'users/index.html', context)

def create(req):
    errors = User.objects.validate(req.POST)
    if len(errors) > 1:
        for error in errors:
            messages.error(req, error)
    else:
        User.objects.easy_create(req.POST)
    return redirect('/')