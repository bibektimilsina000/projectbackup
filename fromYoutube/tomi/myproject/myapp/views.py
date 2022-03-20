from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature




def index(request):
    features=Feature.objects.all()
    return render(request, "index.html",{'features':features})


def about(request):

    return render(request, "about.html")

def register(request):
    return render(request, 'register.html')
