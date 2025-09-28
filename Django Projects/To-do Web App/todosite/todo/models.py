from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField( max_length=50)
    details=models.TextField()
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

