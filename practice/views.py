from django.http import HttpResponse
from django.shortcuts import render


def HomePage(request):
    return render(request,'index.html')

def contact(request):
    name=request.GET['name']
    return render(request,'contact.html',{"names":name})

def topicListing(request):
    return render(request,'topics-listing.html')

