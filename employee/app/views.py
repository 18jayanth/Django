from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_dept(request):
    DEPTNO=int(input('Enter the DeptNO:'))
    DNAME=input("Enter the Dname:")
    LOC=input("Enter the Location:")
    DPO=DEPT
