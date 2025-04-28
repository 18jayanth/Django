from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1(request):
    return HttpResponse('<h1>This is <marquee>First</marquee> text</h1>')