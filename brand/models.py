from django.db import models

# Create your models here.


class brand_project(models.Model):
    upload_image = models.ImageField(upload_to = "gallery/brand")

class Num(models.Model):
    number = models.ForeignKey(brand_project,on_delete=models.CASCADE)