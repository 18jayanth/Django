from django.db import models

# Create your models here.
class  DEPT(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models.CharField(max_length=100,unique=True)
    LOC=models.CharField(max_length=100)
    def __str__(self):
        return str(self.DEPTNO)+' '+self.DNAME
    
class  EMP(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models.CharField(max_length=100)
    JOB=models.DecimalField(max_digits=10,decimal_places=2)
    COMM=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    HIREDATE=models.DateField()
    DEPTNO=models.ForeignKey('DEPT',on_delete=models.CASCADE)
    MGR=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return str(self.DEPTNO)+' '+self.ENAME
    
class SALGRADE(models.Model):
    GRADE=models.IntegerField()
    LOSAL=models.DecimalField(max_digits=10,decimal_places=2)
    HISAL=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return str(self.GRADE)
    
    