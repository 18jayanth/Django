from django.shortcuts import render

# Create your views here.
def index1(request):
    d={'Roll':18,'branch':'cse'}
    return render(request,'index1.html',context=d)
