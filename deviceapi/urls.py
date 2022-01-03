from django.urls import path

from deviceapi.models import DeviceApi
from .views import DeviceApiView,ManipulateDeviceData
urlpatterns=[
    path('deviceapi',DeviceApiView,name='DeviceApiView'),
    path('deviceapi/<int:pk>',ManipulateDeviceData,name='ManipulateDeviceData')
]