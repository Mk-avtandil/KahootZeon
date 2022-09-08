"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from kahoot.views import *
from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/kahoot/registration/", include('djoser.urls')),
    path("api/v1/kahoot/auth/", include('rest_framework.urls')),
    path("", include('kahoot.urls')),
]

urlpatterns += yasg_urls
