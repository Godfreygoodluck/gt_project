from django.db import models

# Create your models here.

class our_Services(models.Model):
 services= models.TextField()

class our_Surport(models.Model):
  surport   = models.TextField()
    
class testimonials(models.Model):
  testimonial = models.TextField()
  testimonial_image = models.ImageField(upload_to = "gallery/testimonial")
  created_on = models.DateTimeField(auto_now_add=True)

class Num(models.Model):
  number = models.ForeignKey(testimonials,on_delete=models.CASCADE)

class wallpaper(models.Model):
  wallpaper_image = models.ImageField(upload_to = "gallery/testimonial")
  created_on = models.DateTimeField(auto_now_add=True)
