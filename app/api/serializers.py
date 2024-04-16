from rest_framework import serializers
from .models import SoilParameters, DataCollectionModule

class SoilParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilParameters
        fields = '__all__'
        



class DataCollectionModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCollectionModule
        fields = '__all__'