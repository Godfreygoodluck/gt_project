from django.db import models

# Create your models here.
 


class about_company(models.Model):
    about = models.TextField()

class about_photographer(models.Model):
    about = models.TextField()
    photographers_image = models.ImageField(upload_to = "gallery/about")
    