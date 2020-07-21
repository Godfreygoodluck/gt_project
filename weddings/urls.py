from django.urls import path
from . import views

urlpatterns = [
    path("", views.weddings_index, name = "weddings_index"),
]
