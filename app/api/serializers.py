from rest_framework import serializers
from .models import SoilParameters

class SoilParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilParameters
        fields = '__all__'
        