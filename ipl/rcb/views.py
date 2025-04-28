from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse('<h1>Rajat Patidhar is the Captain')
def vicecaptain(request):
    return HttpResponse('<h1>Devudutt Padikkal is vice captain</h1>')