from django.db import models

# Create your models here.
class SoilParameters(models.Model):
    soil_temperature = models.FloatField(default=0)
    soil_moisture = models.FloatField(default=0)
    soil_ph = models.FloatField(default=0)
    soil_nitrogen_content = models.FloatField(default=0)
    soil_phosphorus_content = models.FloatField(default=0)
    soil_potassium_content = models.FloatField(default=0)
    soil_electrical_conductivity = models.FloatField(default=0)