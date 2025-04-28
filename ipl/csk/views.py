from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>RutuRaj Gaikward is the Captain')
def vicecaptain(request):
    return HttpResponse('<h1>Rachin Ravindra is vice captain</h1>')