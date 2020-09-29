from django.db import models

# Create your models here.



class portrait_project(models.Model):
    upload_image = models.ImageField(upload_to = "gallery/portrait")
    created_on = models.DateTimeField(auto_now_add=True)

class Num(models.Model):
    number = models.ForeignKey(portrait_project,on_delete=models.CASCADE)