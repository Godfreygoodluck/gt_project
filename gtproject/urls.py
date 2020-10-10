"""gtproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from nav import views as nav_views
from header import views as header_views
from gallery import views as gallery_views
from index import views as index_views

admin.site.site_header = "Shoot With Gt"
admin.site.site_title = "Gt Admin Portal"
admin.site.index_title  = "Welcome to Gt portal" 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
