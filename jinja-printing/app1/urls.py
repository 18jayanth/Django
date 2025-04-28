from django.urls import path
from app1.views import *
from app1.views1 import *
app_name='something'
urlpatterns = [
    path('app1',app1,name='app1'),
    path('index1',index1,name='index1'),
]
