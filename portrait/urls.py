from django.urls import path
from . import views

urlpatterns = [
    path("", views.portrait_index, name = "portrait_index"),
    
]
