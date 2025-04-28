from django.shortcuts import render

# Create your views here.
def index2(request):
    d={'Roll':18,'branch':'cse'}
    return render(request,'index2.html',context=d)
