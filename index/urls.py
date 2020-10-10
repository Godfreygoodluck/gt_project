from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path('blog/', views.blog_index, name = "blog"),    
    path('weddings/', views.weddings_index, name = "weddings"),
    path('brand/', views.brand_index, name = "brand"),
    path('portrait/', views.portrait_index, name = "portrait"),
    path('testimonial/', views.testimonial_index, name = "testimonial"),
    path("<category>/", views.blog_category, name="blog_category"),
]
