from django.shortcuts import render

# Create your views here.

d={'name':'jayanth','name1':'Pavan','age':24}
def index(request):
    return render(request,'index.html',context=d)