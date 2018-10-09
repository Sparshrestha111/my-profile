from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils import timezone
from django.http.response import HttpResponseRedirect

# Create your views here.

def home(request):
    username = request.user
    return render(request, 'prfl/base.html',{'user': username})

def projects(request):
    return HttpResponse("<p> This are my projects.</p>")

def myresume(request):
    username = request.user
    return render(request, 'prfl/myresume.html',{'user': username})

def aboutme(request):
    username = request.user
    return render(request, 'prfl/aboutme.html',{'user': username})
