from django.shortcuts import render

# Create your views here.
def run(request):
    return render(request,'run.html')