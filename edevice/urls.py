from django.urls import path;
from .views import devicePage

urlpatterns = [
    path('homepage',devicePage)
]