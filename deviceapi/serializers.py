from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import DeviceApi

class DeviceApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceApi
        fields = '__all__'