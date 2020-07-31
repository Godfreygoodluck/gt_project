
from django.urls import path
from . import views


urlpatterns = [
    path('', views.company_index, name = "company_index"),
    path('', views.photographer_index, name="photographer_index"),

]
