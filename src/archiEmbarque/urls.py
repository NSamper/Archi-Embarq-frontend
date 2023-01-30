"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import RedirectView

from archiEmbarque import views

urlpatterns = [
    path('', RedirectView.as_view(url='device/', permanent=True)),
    path('device/', views.DeviceList.as_view(), name='deviceList'),
    path('device/<int:pk>', views.DeviceDetails.as_view(), name='deviceDetails'),
    path('digital/<int:pk>', views.Digital, name='digital'),
    path('json/device/', views.deviceListJson, name='jsonDeviceList'),
    path('json/device/<int:pk>', views.deviceItemJson, name='jsonDeviceDetails'),
]
