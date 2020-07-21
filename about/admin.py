from django.contrib import admin
from .models import about_company, about_photographer

# Register your models here.

admin.site.register(about_company)
admin.site.register(about_photographer)