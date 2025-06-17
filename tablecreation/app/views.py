from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def insert_topic(request):
    for i in Topic.objects.all():
        print(i,i.topic_name)
        
    
    topic_name=input('Enter Topic Name:')
    TTO=Topic.objects.get_or_create(topic_name=topic_name)
    if TTO[1]:
        LTO=Topic.objects.all()
        d={'LTO':LTO}
        return render(request,'display_topic.html',d)
        #return HttpResponse('Topic is created')
    else:
        return HttpResponse('Topic already exists')

def insert_webpage(request):
    for i in Webpage.objects.all():
        print(i.id,i.name,i)
    topic_name=input('Enter Topic Name:')
    LTO=Topic.objects.filter(topic_name=topic_name)
    if LTO:
        TO=LTO[0]
        name=input('Enter Name:')
        url=input('Enter URL:')
        email=input('Enter Mail:')
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
    
def insert_accessrecord(request):
    for i in accessrecords.objects.all():
        print(i.id,i.author)
    PK=int(input('Enter the Primary Key Of Webpage:'))
    WO=Webpage.objects.get(id=PK)
    if WO:
        author=input("Enter Name of Author:")
        date=input("Enter the date:")
        TAO=accessrecords.objects.get_or_create(name=WO,author=author,date=date)
    
        if TAO[1]:
            LAO=accessrecords.objects.all()
            d={'LAO':LAO}
            return render(request,'display_records.html',d)
        else:
            return HttpResponse('Record already exists')
    else:
         return HttpResponse('There is no id with this name in webpage table')
        
        
    
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpages(request):
    #LWO=Webpage.objects.all()
    # LWO=Webpage.objects.filter(topic_name='cricket')
    # LWO=Webpage.objects.exclude(topic_name='cricket')
    # LWO=Webpage.objects.all()[0:3:]
    # LWO=Webpage.objects.all().order_by('name')
    #LWO=Webpage.objects.filter(name__startswith="v")
    #LWO=Webpage.objects.filter(name__endswith="t")
    #LWO=Webpage.objects.filter(name__contains="v")
    LWO=Webpage.objects.annotate(name_length=Length('name')).filter(name_length__gt=1)
    #LWO=Webpage.objects.filter(name__regex="V\w+")
    #LWO=Webpage.objects.filter(topic_name='cricket',name='Dhoni')
    #LWO=Webpage.objects.filter(Q(topic_name='cricket') | Q(name='Dhoni'))
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)

def display_records(request):
    LAO=accessrecords.objects.all()
    d={'LAO':LAO}
    return render(request,'display_records.html',d)
def update_webpage(request):
    #Webpage.objects.filter(name='Virat Kohli').update(email='viratkohli@gmail.com')
    #Webpage.objects.update_or_create(topic_name="chess",defaults={"name":"Jayanth"})
    Webpage.objects.update_or_create(topic_name='Cricket',defaults={'name':'Rahul'})
    
    #BTO=Topic.objects.get(topic_name='Cricket')
    #Webpage.objects.update_or_create(name="Pavan",defaults={"topic_name":BTO})
    #Webpage.objects.update_or_create(name="Ajay",defaults={"topic_name":BTO})
    LWO=Webpage.objects.all() 
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)

def delete_records(request):
    #accessrecords.objects.filter(author="Jayanth").delete()
    accessrecords.objects.filter(name=4).delete()
    
    LAO=accessrecords.objects.all() 
    d={'LAO':LAO}
    return render(request,'display_records.html',d)
    

    


            
    