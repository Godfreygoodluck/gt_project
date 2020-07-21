from django.urls import path
from . import views

urlpatterns = [
    path("", views.brand_index, name = "brand_index"),
]
