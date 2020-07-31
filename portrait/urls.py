from django.urls import path
from . import views

urlpatterns = [
    path("", views.portrait_index, name = "portrait_index"),
    path("", views.aboutCompany_index, name = "aboutCompany_index"),
    path("", views.aboutPhotographer_index, name = "aboutPhotographer_index"),
    
]
 