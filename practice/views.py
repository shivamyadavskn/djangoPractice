from django.http import HttpResponse
from django.shortcuts import render


def HomePage(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def freelancer(request):
    return render(request,'freelancer.html')

def job(request):
    return render(request,'job.html')
