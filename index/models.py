from django.db import models

# Create your models here.

class our_Services(models.Model):
     services= models.TextField()

class our_Surport(models.Model):
  surport   = models.TextField()
    
class testimonials(models.Model):
    testimonial = models.TextField()
    testimonial_image = models.ImageField(upload_to = "gallery/testimonial")
