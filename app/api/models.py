from django.db import models
from django.utils import timezone 

# Create your models here.
class SoilParameters(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    soil_temperature = models.FloatField(default=0)
    soil_moisture = models.FloatField(default=0)
    soil_ph = models.FloatField(default=0)
    soil_nitrogen_content = models.FloatField(default=0)
    soil_phosphorus_content = models.FloatField(default=0)
    soil_potassium_content = models.FloatField(default=0)
    soil_electrical_conductivity = models.FloatField(default=0)