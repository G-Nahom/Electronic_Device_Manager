from django.db import models
from django.utils import timezone
class DeviceApi(models.Model):
    Deivice_Name = models.CharField(max_length=30)
    Device_Model = models.CharField(max_length=30)
    Production_Year = models.DateField(auto_now=timezone.now())
    IMEIL = models.IntegerField()
    Produced_By = models.CharField(max_length= 100)
    
    def __str__(self):
        return self.Deivice_Name