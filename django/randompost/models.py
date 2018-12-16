from django.db import models
#from django.utils import timezone

# Create your models here.
class RandomPost(models.Model):
    first = models.CharField(max_length=20)
    second = models.CharField(max_length=20)
    creation_date=models.DateTimeField(auto_now=True)
    