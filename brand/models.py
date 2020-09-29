from django.db import models

# Create your models here.


class brand_project(models.Model):
    upload_image = models.ImageField(upload_to = "gallery/brand")
    created_on = models.DateTimeField(auto_now_add=True)

class Num(models.Model):
    number = models.ForeignKey(brand_project,on_delete=models.CASCADE)