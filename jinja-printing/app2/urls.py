from django.urls import path
from app2.views import *
from app2.views1 import *
app_name='something'
urlpatterns = [
    path('app2',app2,name='app1'),
    path('index2',index2,name='index1'),
]
