from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "first_app/index.html")

def process(request):
    print(request.POST['first_name'])
    return redirect('/')