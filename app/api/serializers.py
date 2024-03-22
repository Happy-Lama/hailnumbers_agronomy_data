from rest_framework import serializers
from .models import SoilParameters

class SoilParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilParameters
        fields = '__all__'
        # fields = ['soil_temperature', 'soil_moisture', 'soil_ph', 'soil_nitrogen_content', 'soil_phosphorus_content', 'soil_potassium_content', 'soil_electrical_conductivity']