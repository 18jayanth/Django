from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField()
    url=models.URLField()
    email=models.EmailField(default='jayanth@gmail.com')
    
    def __str__(self):
        return str(self.name)
    
class accessrecords(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField()
    date=models.DateField(auto_now=True)
    url=models.URLField(null=True,blank=True)
    def __str__(self):
         return self.author