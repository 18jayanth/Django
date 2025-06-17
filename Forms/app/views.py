from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

def insert_topic(request):
    if request.method=="POST":
        tn=request.POST["tna"]
        TTO=Topic.objects.get_or_create(topic_name=tn)
        print(TTO)
        if TTO[1]:
             LTO=Topic.objects.all()
             d={'LTO':LTO}
             return render(request,'display_topic.html',d)
        else:
            return HttpResponse('Topic already exists')
    return render(request,"insert_topic.html")


def insert_webpage(request):
    for i in Webpage.objects.all():
        print(i.id,i.name,i)
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=="POST":
        topic_name=request.POST.get("tna")
        LTO=Topic.objects.filter(topic_name=topic_name)
        if LTO:
            TO=LTO[0]
            name=request.POST["name"]
            url=request.POST["url"]
            email=request.POST["email"]
            TWO=Webpage.objects.get_or_create(topic_name=TO,url=url,name=name,email=email)
            if TWO[1]:
                LWO=Webpage.objects.all()
                d={'LWO':LWO}
                return render(request,'display_webpages.html',d)
            #return HttpResponse('Webpage is created')
            else:
                return HttpResponse('Webpage already exists')
        else:
            return HttpResponse('There is no topic with this name in parent table')
    return render(request,"insert_webpage.html",d)
    
def insert_accessrecord(request):
    for i in accessrecords.objects.all():
        print(i.id,i.name,i.author)
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        
        PK=request.POST.get("tn")
        LWO=Webpage.objects.filter(id=PK)
        print(LWO)
        if LWO:
            WO=LWO[0]
            author=request.POST["author"]
            date=request.POST["date"]
            TAO=accessrecords.objects.get_or_create(name=WO,author=author,date=date)
    
            if TAO[1]:
                LAO=accessrecords.objects.all()
                d={'LAO':LAO}
                return render(request,'display_records.html',d)
            else:
                return HttpResponse('access record already exists')
        else:
            return HttpResponse('There is no id in Webpage table')
    return render(request,"insert_accessrecord.html",d)


def select_multiple(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        ltns=request.POST.getlist('tns')
        print(ltns)
        LWO=Webpage.objects.none()
        
        for tn in ltns:
            LWO=LWO | Webpage.objects.filter(topic_name=tn)
        d1={'LWO':LWO}
        return render(request,'display_webpages.html',d1)
    return render(request,'select_multiple.html',d)

def select_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    
    return render(request,'select_topic.html',d)
    



    


    


            
    