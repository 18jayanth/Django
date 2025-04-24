from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>Hardik Pandhya is the Captain')
def vicecaptain(request):
    return HttpResponse('<h1>Surya Kumar Yadav is vice captain</h1>')