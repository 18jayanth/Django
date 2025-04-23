from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jayanth(response):
    return HttpResponse('Jayanth is a innnocent boy')

def pavan(response):
    return HttpResponse("<div><h1>Hello world</h1></div> <div><a href='https://www.google.com'>Google</a></div><div><img/ src='https://www.shutterstock.com/image-photo/waterfall-hidden-tropical-jungle-600nw-460505092.jpg'style='border-radius:50%' alt='it is an image'/></div>")