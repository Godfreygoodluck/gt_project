from django.db import models

# Create your models here.



class contact(models.Model):
    Address = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Email= models.EmailField()
    
