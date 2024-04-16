from django.db import models
from django.utils import timezone 

# 16/04/2024: added Datacollection Module and ForeignKey to soil parameters

class DataCollectionModule(models.Model):
    module_id = models.CharField(primary_key=True, max_length=256)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)


class SoilParameters(models.Model):
    module_id = models.ForeignKey(DataCollectionModule, on_delete=models.SET_NULL, default=None, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    soil_temperature = models.FloatField(default=0)
    soil_moisture = models.FloatField(default=0)
    soil_ph = models.FloatField(default=0)
    soil_nitrogen_content = models.FloatField(default=0)
    soil_phosphorus_content = models.FloatField(default=0)
    soil_potassium_content = models.FloatField(default=0)
    soil_electrical_conductivity = models.FloatField(default=0)


