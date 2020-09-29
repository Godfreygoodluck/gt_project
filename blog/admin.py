from django.contrib import admin
from .models import blog_post, Category

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(blog_post,PostAdmin)
admin.site.register(Category, CategoryAdmin)


