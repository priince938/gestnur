from django.db import models
from django.utils import safestring

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    subject=models.CharField(max_length=500)
    message=models.CharField(max_length=2084)
    def __str__(self):
       return '%s %s' % (self.name,self.subject)





